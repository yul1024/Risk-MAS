"""
存储中间文档读取结构的manager。
"""

from llama_index.core.storage.docstore import SimpleDocumentStore

from llama_index.core import Document
from llama_index.core.schema import BaseNode

from pathlib import Path


class DocumentStoreManager:
    """
    llama-index中的document对象的IO操作。

    使用SimpleDocumentStore，在本地以json格式进行持久化。
    """
    def __init__(self):
        ...

    def save_nodes(
        self,
        documents: list[Document],
        path_to_save: str | Path,
    ) -> None:
        """
        将documents持久化到指定路径。

        Args:
            documents: 在内存中的documents。
            path_to_save: 指定保存的路径。需要指定.json扩展名。

        Returns:
            打印保存位置。
        """
        document_store = SimpleDocumentStore()
        document_store.add_documents(documents)
        document_store.persist(persist_path=path_to_save)
        print(f"Documents are persisted to {path_to_save}")

    def load_nodes(
        self,
        document_store_path: str | Path,
    ) -> list[Document] | list[BaseNode]:
        """
        从指定路径加载document-store至内存。

        会将原始存储的nodes完全还原为list。

        Args:
            document_store_path: 指定加载的路径。

        Returns:
            list[BaseNode]，最初保存的nodes的原始形式。
        """
        document_store = SimpleDocumentStore.from_persist_path(
            persist_path=str(document_store_path)
        )
        documents: list[BaseNode] = list(document_store.docs.values())  # dict_values的list方法。
        return documents


if __name__ == '__main__':
    pass
