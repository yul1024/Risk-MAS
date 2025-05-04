"""
从pdf文档到document对象的pipeline。
"""

from mas.data_processing_pipeline.image_loading_pipeline.image_loader import SimpleImageLoader
from mas.data_processing_pipeline.image_loading_pipeline.pdf_image_converter import PdfImageConverter

from llama_index.core import Document

from pathlib import Path


class ImageLoadingPipeline:
    """
    原始pdf至image_document的完整流程。

    可以检测是否已经转换为图片避免重复转换。
    """
    def __init__(
        self,
        original_pdf_path: str | Path,
        base_image_pdf_dir: str | Path,
        is_need_convert: bool = True,
    ):
        self.original_pdf_path = Path(original_pdf_path)
        self.base_image_pdf_dir = Path(base_image_pdf_dir)
        self.is_need_convert = is_need_convert

        self.image_pdf_dir = self.base_image_pdf_dir / self.original_pdf_path.name

    def run(self) -> list[Document]:
        """
        主要方法。

        Returns:
            图片文档对象的list。
        """
        image_documents = self.load_image()
        return image_documents

    def load_image(self) -> list[Document]:
        """
        加载图片，进行指定的检查。

        Returns:
            图片文档对象的list。
        """
        if self.is_need_convert:
            # 指定进行转换，不进行检测，如果存在就覆盖原有结果。
            self._convert_pdf_to_images(self.original_pdf_path, self.image_pdf_dir)
        else:
            if not self.image_pdf_dir.exists():
                # 不进行转换，但是之前并没有进行转换。需要执行转换才能继续。
                self._convert_pdf_to_images(self.original_pdf_path, self.image_pdf_dir)
        image_loader = SimpleImageLoader(pdf_images_dir=self.image_pdf_dir)
        image_documents = image_loader.run()
        return image_documents

    def _convert_pdf_to_images(
        self,
        pdf_path: Path,
        image_pdf_dir: Path,
    ) -> None:
        """
        将pdf转换为图片，保存至指定文件夹。

        Args:
            pdf_path: 原始pdf文档路径。
            image_pdf_dir: 指定结果保存路径。

        Returns:
            进行转换，保存结果。
        """
        # 使用我构建的转换工具进行转换。
        pdf_image_converter = PdfImageConverter()
        pdf_image_converter.convert_pdf_to_images(
            pdf_path=pdf_path,
            output_folder=image_pdf_dir,
        )


if __name__ == '__main__':
    pass
