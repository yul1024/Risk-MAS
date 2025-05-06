"""
为了加速和分离，实际中并不集中消耗IO加载和处理pdf。
"""

from mas.utils import DocumentStoreManager
from mas.data_processing_pipeline.loading.text_loading_pipeline import TextLoadingPipeline
from mas.data_processing_pipeline.loading.image_loading_pipeline import ImageLoadingPipeline

from llama_index.core import Document

from pathlib import Path


class PrePdfLoader:
    """
    pdf预加载工具。
    原始pdf文件无论模态，加载为document-store。

    文件树组织结构为:
        - original_pdf_dir
            - .pdf
        - image_pdf_dir
            - pdf_dir
                - .png
        - document_store_dir
            - text_dir
                - .json
            - image_dir
                - .json
    一级文件夹可自定义。
    转换结果文件夹以原始pdf文件名命名，包括.pdf扩展名。
    document_store_dir下的2个子文件夹自动构建，不指定需要增加文件命名复杂度。
    """
    def __init__(
        self,
        pdf_dir: str | Path,
        base_image_pdf_dir: str | Path,
        document_store_dir: str | Path,
    ):
        """
        批量处理方法，仅指定文件夹。
            - 会批量处理所有文件。
            - 会自动检查并跳过存在情况。

        Args:
            pdf_dir: 存放原始pdf文件的文件夹。
            base_image_pdf_dir: 打算存放将pdf转换为image的文件夹。
            document_store_dir: 打算存放之后进行处理的document-store的文件夹。
        """
        self.document_store_manager = DocumentStoreManager()

        self.pdf_dir = Path(pdf_dir)
        self.base_image_pdf_dir = Path(base_image_pdf_dir)
        self.document_store_dir = Path(document_store_dir)

        self.document_store_dir.mkdir(exist_ok=True, parents=True)

        self.pdf_path_list = list(self.pdf_dir.glob('*.pdf'))

    def batch_process_text(
        self,
        loading_methods: list[str],
    ):
        """
        批量处理text形式的pdf。

        Args:
            loading_methods:  加载方法，有['rule', 'ocr', 'vlm']。可以进行指定，仅选择其中的几个。

        Returns:
            每个pdf完成document-store，会打印输出。
        """
        for loading_method in loading_methods:
            for pdf_path in self.pdf_path_list:
                path_to_save = self.document_store_dir / 'text' / f"{loading_method}--{pdf_path.name}.json"
                if path_to_save.exists():
                    continue
                self.load_and_save_text_documents(
                    original_pdf_path=pdf_path,
                    loading_method=loading_method,
                    path_to_save=path_to_save,
                )
            print(f"Text {loading_method} pdf document store done.")

    def batch_process_image(
        self,
        is_need_convert: bool = False,
    ):
        """
        批量处理text形式的pdf。

        Args:
            is_need_convert: 是否将原始的pdf转换为image。不会进行覆盖检查。默认为True，可以在第一次进行转换，之后根据情况进行覆盖。

        Returns:
            每个pdf完成document-store，会打印输出。
        """
        for pdf_path in self.pdf_path_list:
            path_to_save = self.document_store_dir / 'image' / f"none--{pdf_path.name}.json"
            if path_to_save.exists():
                continue
            self.load_and_save_image_documents(
                original_pdf_path=pdf_path,
                base_image_pdf_path=self.base_image_pdf_dir,
                is_need_convert=is_need_convert,
                path_to_save=path_to_save,
            )
        print(f"Image pdf document store done.")

    def load_and_save_text_documents(
        self,
        original_pdf_path: str | Path,
        loading_method: str,
        path_to_save: str | Path,
    ) -> list[Document]:
        """
        加载并保存text形式是pdf。

        封装了我构建的text-loading-pipeline和document-store-manager的方法，组合加载和保存。

        Args:
            original_pdf_path: 原始pdf的路径。
            loading_method: 加载方法，有['rule', 'ocr', 'vlm']。
            path_to_save: 保存document-store的位置，以json格式。

        Returns:
            加载的documents。不是主要功能，documents已经进行了持久化。
        """
        # 加载文档
        text_loading_pipeline = TextLoadingPipeline(original_pdf_path=original_pdf_path)
        text_documents = text_loading_pipeline.run(loading_method=loading_method)
        # 保存文档
        self.document_store_manager.save_nodes(
            documents=text_documents,
            path_to_save=path_to_save
        )
        return text_documents

    def load_and_save_image_documents(
        self,
        original_pdf_path: str | Path,
        base_image_pdf_path: str | Path,
        is_need_convert: bool,
        path_to_save: str | Path,
    ) -> list[Document]:
        """
        加载并保存image形式是pdf。

        封装了我构建的image-loading-pipeline和document-store-manager的方法，组合加载和保存。

        Args:
            original_pdf_path: 原始pdf的路径。
            base_image_pdf_path: 存储image的基础路径。因为一个pdf有多个image，因此images是放在一个文件夹中的。
            is_need_convert: 是否将原始的pdf转换为image。不会进行覆盖检查。
            path_to_save: 保存document-store的位置，以json格式。

        Returns:
            加载的documents。不是主要功能，documents已经进行了持久化。
        """
        # 加载文档
        image_loading_pipeline = ImageLoadingPipeline(
            original_pdf_path=original_pdf_path,
            base_image_pdf_dir=base_image_pdf_path,
            is_need_convert=is_need_convert
        )
        image_documents = image_loading_pipeline.run()
        # 保存文档
        self.document_store_manager.save_nodes(
            documents=image_documents,
            path_to_save=path_to_save
        )
        return image_documents


if __name__ == '__main__':
    pass
