"""
获取vector-store的工厂。
"""

from llama_index.vector_stores.milvus import MilvusVectorStore


class VectorStoreFactory:
    def __init__(
        self,
        vector_store_uri: str = "http://localhost:19530"
    ):
        self.vector_store_uri = vector_store_uri

    def get_milvus_vector_store(
        self,
        dim: int,
        collection_name: str,
    ):
        vector_store = MilvusVectorStore(
            uri=self.vector_store_uri,
            collection_name=collection_name,
            dim=dim
        )
        return vector_store

    def _get_embedding_model_dim(
        self,
        embedding_model_name: str,
    ) -> int:
        return 768


if __name__ == '__main__':
    pass
