"""
完整pipeline基础功能。

实现:
    - 文档加载。
    - 文档存储。
"""

from mas.utils import DocumentStoreManager

from llama_index.core import Document

from pathlib import Path


class BasePipeline:
    """

    """
    def __init__(
        self,
    ):
        """"""

        self.document_store_manager = DocumentStoreManager()

    def load_documents_from_document_store(
        self,
        document_store_path: str | Path,
    ) -> list[Document]:
        """
        从文档存储中加载文档。

        使用我通用的document-store管理工具加载。

        Args:
            document_store_path:

        Returns:

        """
        nodes = self.document_store_manager.load_nodes(document_store_path=document_store_path)
        return nodes


if __name__ == '__main__':
    pass
