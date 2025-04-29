"""
将原始pdf转换为markdown，进行拆分，构建为node。
"""

from llama_index.readers.file import PyMuPDFReader
from llama_index.readers.docling import DoclingReader
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
from llama_index.readers.llama_parse import LlamaParse


class PDFReader:
    def __init__(self):
        ...

    def get_simple_pdf_reader(self):
        """
        最简单的默认pdf-reader。
        只会按页、按照规则解析。

        Returns:
            pymupdf reader。
        """
        return PyMuPDFReader()

    def get_docling_reader(self):
        """
        docling在llama-index中集成的reader。
        有用于解析的LLM支持，会整合多页的文本内容。

        Returns:
            docling reader。
        """
        return DoclingReader()

    def get_smart_pdf_loader(self):
        """

        Returns:

        """
        return SmartPDFLoader()

    def get_llama_parse(self):
        """
        使用最强的llama_parser。
        在llama

        Returns:

        """
        return LlamaParse(preserve_layout_alignment_across_pages=True, save_images=True)


class PDFToMD:
    """
    将原始的pdf转换成md格式文件。
    """
    def __init__(self):
        ...

    def get_simple_reader(self):
        """

        Returns:

        """


if __name__ == '__main__':
    pass
