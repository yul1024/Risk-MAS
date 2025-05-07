"""
index的控制。
"""

from llama_index.core.settings import Settings

from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex
from llama_index.core.indices import MultiModalVectorStoreIndex

from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.schema import BaseNode, Document
from llama_index.core.vector_stores.types import BasePydanticVectorStore
from llama_index.core.indices.base import BaseIndex

from pathlib import Path


class IndexManager:
    """
    基础的llama-index中index的创建和持久化相关方法。
    """
    def __init__(self):
        # 我很讨厌llama-index的自动处理。每个类调用避免自动处理。
        Settings.transformations = []

    def save_index(
        self,
        index: BaseIndex,
        dir_to_save: str | Path,
    ):
        """
        将完整的index的信息全部存储在本地。

        Args:
            index: 可直接使用的索引。
            dir_to_save: 所有index相关的信息全部存储在本地的文件夹。

        Returns:
            打印完成持久化。
        """
        index.storage_context.persist(persist_dir=dir_to_save)
        print(f"index saved to {dir_to_save}")

    def load_index_from_storage(
        self,
        index_storage_dir: str | Path,
    ):
        """
        从本地加载index。

        Args:
            index_storage_dir: 所有index相关的信息全部存储在本地的文件夹。

        Returns:
            打印完成读取。
        """
        index_storage = StorageContext.from_defaults(persist_dir=str(index_storage_dir))
        index = load_index_from_storage(index_storage)
        print(f"index loaded from {index_storage_dir}")
        return index

    def build_index_from_nodes(
        self,
        nodes: list[BaseNode],
        embedding_model: BaseEmbedding,
        vector_store: BasePydanticVectorStore,
    ):
        """
        使用nodes创建index。

        文档有些混乱，这里不确定是否输入documents是否可以正常执行。
        源代码中有异常检查，但是ImageDocument是正常运行的。

        Args:
            nodes: 待处理list[node]，从document-store加载或经pipeline处理的输出。
            embedding_model: embedding-model。测试过后可以是多模态的。
            vector_store: vector-store。这里执行注入是为了以不同的backend以及自行指定collection-name。

        Returns:
            可直接使用的index。
        """
        index = VectorStoreIndex(
            nodes=nodes,
            embed_model=embedding_model,
            vector_store=vector_store,
            transformations=[],
        )
        return index

    def build_index_from_documents(
        self,
        documents: list[BaseNode],
        embedding_model: BaseEmbedding,
        vector_store: BasePydanticVectorStore,
    ):
        """
        使用documents创建index。

        为了避免自动转换，我默认指定transformations=[]。

        Args:
            documents: 从document-store加载的结果。
            embedding_model: embedding-model。测试过后可以是多模态的。
            vector_store: vector-store。这里执行注入是为了以不同的backend以及自行指定collection-name。

        Returns:
            可直接使用的index。
        """
        index = VectorStoreIndex.from_documents(
            documents=documents,
            embed_model=embedding_model,
            vector_store=vector_store,
            transformations=[],
        )
        return index

    def build_multimodal_index(
        self,
        nodes: list[Document],
        vector_store: BasePydanticVectorStore,
        embedding_model: BaseEmbedding,
    ):
        storage_context = StorageContext.from_defaults(image_store=vector_store)
        index = MultiModalVectorStoreIndex.from_documents(
            documents=nodes,
            storage_context=storage_context,
            embed_model=embedding_model,
            image_embed_model=embedding_model,
            image_store=vector_store,
            transformations=[],
        )
        return index

    def load_index_from_vector_store(
        self,
        vector_store: BasePydanticVectorStore,
        embedding_model: BaseEmbedding,
    ):
        """
        从vector-store加载index。

        这段代码是官方文档的。
        实际中没有使用，原因是storage-context中有太多默认的情况，对于多模态不友好。

        Args:
            vector_store: 这里执行注入是为了以不同的backend以及自行指定collection-name。
            embedding_model: embedding-model。测试过后可以是多模态的。

        Returns:
            可直接使用的index。
        """
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex.from_vector_store(
            vector_store,
            embed_model=embedding_model,
            storage_context=storage_context,
        )
        return index


if __name__ == '__main__':
    pass
