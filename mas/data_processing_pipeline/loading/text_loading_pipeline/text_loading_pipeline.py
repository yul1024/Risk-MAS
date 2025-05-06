"""
从pdf文档到document对象的pipeline。
"""

from mas.data_processing_pipeline.loading.text_loading_pipeline.text_loader import PymupdfTextLoader

from llama_index.core import Document

from pathlib import Path


class TextLoadingPipeline:
    """
    原始pdf至document的完整流程。
    """
    def __init__(
        self,
        original_pdf_path: str | Path,
    ):
        self.original_pdf_path = Path(original_pdf_path)

    def run(
        self,
        loading_method: str
    ) -> list[Document]:
        """
        主要方法。

        Returns:
            对于方法的text加载器。
        """
        if loading_method == 'rule':
            return self.load_pdf_by_rule()
        elif loading_method == 'ocr':
            return self.load_pdf_by_ocr()
        elif loading_method == 'vlm':
            return self.load_pdf_by_vlm()

    def load_pdf_by_rule(self) -> list[Document]:
        """
        基于规则的方式加载pdf。

        Returns:
            list[Document]，将整个pdf的文档作为一个Document对象的结果。
        """
        text_loader = PymupdfTextLoader(self.original_pdf_path)
        text_loader.set_rule_loader()
        text_documents = text_loader.run()
        return text_documents

    def load_pdf_by_ocr(self) -> list[Document]:
        """
        使用ocr强化的方法加载pdf。

        Returns:
            list[Document]，将整个pdf的文档作为一个Document对象的结果。
        """
        text_loader = PymupdfTextLoader(self.original_pdf_path)
        text_loader.set_ocr_loader()
        text_documents = text_loader.run()
        return text_documents

    def load_pdf_by_vlm(self) -> list[Document]:
        """
        使用vlm强化的方法加载pdf。

        Returns:
            list[Document]，将整个pdf的文档作为一个Document对象的结果。
        """
        text_loader = PymupdfTextLoader(self.original_pdf_path)
        text_loader.set_vlm_loader()
        text_documents = text_loader.run()
        return text_documents


if __name__ == '__main__':
    pass

