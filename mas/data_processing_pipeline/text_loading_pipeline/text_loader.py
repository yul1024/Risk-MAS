"""
由langchain中支持的loader实现加载文档。
"""

from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_community.document_loaders.parsers import RapidOCRBlobParser
from langchain_community.document_loaders.parsers import LLMImageBlobParser

from langchain_openai import ChatOpenAI

from llama_index.core import Document

from langchain_core.language_models import BaseChatModel
from langchain_core.documents import Document as LCDocument

import os
from pathlib import Path


class PymupdfTextLoader:
    """
    pymupdf不同加载pdf的方法。
    3种方法对应不同精细程度的加载方法。
    """
    def __init__(
        self,
        pdf_path: str | Path,
    ):
        self.pdf_path = Path(pdf_path)
        self.loader = None

    def run(self) -> list[Document]:
        """
        主要方法。

        Returns:
            llama-index中的Document对象。已经从langchain的Document进行了转换。
            我的默认设置使得加载结果是markdown格式的一个文本对象，会在之后被node-parser处理。
        """
        lc_documents: list[LCDocument] = self.loader.load()
        return [Document.from_langchain_format(document) for document in lc_documents]

    def set_text_only_loader(self):
        """
        仅提取文档中的文字。
        """
        loader = PyMuPDF4LLMLoader(
            file_path=self.pdf_path,
            mode='single',
            table_strategy='lines',
        )
        self.loader = loader

    def set_ocr_loader(self):
        """
        使用ocr强化文档识别。
        """
        loader = PyMuPDF4LLMLoader(
            file_path=self.pdf_path,
            mode='single',
            extract_images=True,
            images_parser=RapidOCRBlobParser(),
            table_strategy='lines',
        )
        self.loader = loader

    def set_vlm_loader(self):
        """
        使用VLM强化文档识别。
        """
        loader = PyMuPDF4LLMLoader(
            file_path=self.pdf_path,
            mode='single',
            extract_images=True,
            images_parser=LLMImageBlobParser(
                model=self._get_vlm()
            ),
            table_strategy='lines',
        )
        self.loader = loader

    def _get_vlm(self) -> BaseChatModel:
        """
        获取VLM，用于识别pdf文档。
        仅在set_vlm_loader中使用。

        Returns:
            VLM。这里用的是qwen最好的VLM。
        """
        vlm = ChatOpenAI(
            model='qwen-vl-max',
            base_url=os.environ['DASHSCOPE_API_BASE_URL'],
            api_key=os.environ['DASHSCOPE_API_KEY'],
        )
        return vlm


if __name__ == '__main__':
    pass
