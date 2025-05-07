"""
vector-store构建器。
"""

from mas.global_config import URI

from mas.data_processing_pipeline.name_manager import NameManager
from mas.data_processing_pipeline.pipeline_factory import PipelineLoader
from mas.models import EmbeddingModelInfoManager

from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core.ingestion import IngestionPipeline

from llama_index.core.vector_stores.types import BasePydanticVectorStore

from pathlib import Path


class VectorStoreBuilder:
    """
    构建vector-store的工具。

    主要使用milvus的工具。
    这个实现将分别存储每个pdf的每种流程，所有信息在collection-name中体现。
    """
    def __init__(
        self,
        cache_dir: str | Path,
        uri: str = None,
    ):
        self.cache_dir = Path(cache_dir)
        # uri其实有全局默认值，因为milvus使用的是self-host方案。
        if uri is None:
            self.uri = URI

        self.pipeline_loader = PipelineLoader(cache_dir=self.cache_dir)

        self.name_manager = NameManager()
        self.embedding_model_info_manager = EmbeddingModelInfoManager()

    def get_simple_vector_store(
        self,
    ) -> BasePydanticVectorStore:
        ...

    def get_milvus_vector_store(
        self,
        collection_name: str,
        dim: int,
        uri: str,
    ) -> BasePydanticVectorStore:
        vector_store = MilvusVectorStore(
            uri=uri,
            # collection_name=collection_name,
            dim=dim,
        )
        return vector_store

    def load_simple_vector_store(
        self,
        vector_store,
        document_store,
    ) -> BasePydanticVectorStore:
        ...

    def get_embedding_model_pipeline(
        self,
        model_key: str,
    ) -> IngestionPipeline:
        vector_store_pipeline = self.pipeline_loader.load_embedding_model_pipeline(model_key=model_key)
        return vector_store_pipeline

    def build_text_vector_store(
        self,
        pdf_name: str,
        loading_method: str,
        embedding_method: str,
    ) -> BasePydanticVectorStore:
        text_vector_store_name = self.name_manager.get_vector_store_name(
            document_store_type='text',
            pdf_name=pdf_name,
            loading_method=loading_method,
            embedding_method=embedding_method,
        )
        vector_store = self.get_milvus_vector_store(
            collection_name=text_vector_store_name,
            dim=self.embedding_model_info_manager.get_dim(model_key=embedding_method),
            uri=self.uri,
        )
        return vector_store

    def build_image_vector_store(
        self,
        pdf_name: str,
        embedding_method: str,
    ) -> BasePydanticVectorStore:
        image_vector_store_name = self.name_manager.get_vector_store_name(
            document_store_type='image',
            pdf_name=pdf_name,
            loading_method='none',
            embedding_method=embedding_method,
        )
        vector_store = self.get_milvus_vector_store(
            collection_name=image_vector_store_name,
            dim=self.embedding_model_info_manager.get_dim(model_key=embedding_method),
            uri=self.uri,
        )
        return vector_store


if __name__ == '__main__':
    pass
