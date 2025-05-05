"""
将documents或nodes进行编码，存储到vector-store中。
"""

from mas.models.embedding_model_factory import EmbeddingModelFactory
from mas.data_processing_pipeline.overall_pipeline.vector_store_factory import VectorStoreFactory

from llama_index.core.ingestion import IngestionPipeline

from llama_index.core.embeddings import BaseEmbedding
from llama_index.core.vector_stores.types import BasePydanticVectorStore


class EmbeddingPipelineFactory:
    def __init__(self):
        self.embedding_model_factory = EmbeddingModelFactory()

    def get_embedding_pipeline(
        self,
        mode: str,
    ) -> IngestionPipeline:
        """
        策略模式封装的文档解析pipeline。

        Args:
            mode (str): 将documents或nodes进行编码并存储进vector-store的方法。

        Returns:

        """
        # if mode == 'nomic-embed-vision-v1.5':
        #     return self.get




if __name__ == '__main__':
    pass
