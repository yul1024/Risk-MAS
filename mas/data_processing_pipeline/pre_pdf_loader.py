"""
为了加速和分离，实际中并不集中消耗IO加载和处理pdf。
"""

from mas.utils import DocumentStoreManager
from mas.data_processing_pipeline.text_loading_pipeline import TextLoadingPipeline
from mas.data_processing_pipeline.image_loading_pipeline import ImageLoadingPipeline

from llama_index.core import Document

from pathlib import Path


class PrePdfLoader:
    def __init__(
        self,
        pdf_dir: str | Path,
        base_image_pdf_dir: str | Path,
        document_store_dir: str | Path,
    ):
        self.document_store_manager = DocumentStoreManager()

        self.pdf_dir = Path(pdf_dir)
        self.base_image_pdf_dir = Path(base_image_pdf_dir)
        self.document_store_dir = Path(document_store_dir)

        self.document_store_dir.mkdir(exist_ok=True, parents=True)

        self.pdf_path_list = list(self.pdf_dir.glob('*.pdf'))

    def batch_process_text(
        self,
        modes: list[str],
    ):
        """

        Args:
            modes:

        Returns:

        """
        for mode in modes:
            for pdf_path in self.pdf_path_list:
                path_to_save = self.document_store_dir / 'text' / f"{mode}--{pdf_path.name}.json"
                if path_to_save.exists():
                    continue
                self.load_and_save_text_documents(
                    original_pdf_path=pdf_path,
                    mode=mode,
                    path_to_save=path_to_save,
                )
            print(f"Text {mode} pdf document store done.")

    def batch_process_image(
        self,
        is_need_convert: bool = True,
    ):
        """

        Args:
            is_need_convert:

        Returns:

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
        mode: str,
        path_to_save: str | Path,
    ) -> list[Document]:
        """

        Args:
            original_pdf_path:
            mode:
            path_to_save:

        Returns:

        """
        # 加载文档
        text_loading_pipeline = TextLoadingPipeline(original_pdf_path=original_pdf_path)
        text_documents = text_loading_pipeline.run(mode=mode)
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

        Args:
            original_pdf_path:
            base_image_pdf_path:
            is_need_convert:
            path_to_save:

        Returns:

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
