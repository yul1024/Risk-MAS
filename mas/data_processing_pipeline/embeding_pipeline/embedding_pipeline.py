from llama_index.core.ingestion import IngestionPipeline

from llama_index.core.embeddings import BaseEmbedding
from llama_index.core.schema import BaseNode
from llama_index.core.vector_stores.types import BasePydanticVectorStore


class EmbeddingPipeline:
    def __init__(
        self,
        embedding_model: BaseEmbedding,
        vector_store: BasePydanticVectorStore,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def run(
        self,
        nodes: list[BaseNode],
    ):
        ...

    def get_base_embedding_pipeline(
        self,
    ) -> IngestionPipeline:
        """

        Returns:

        """
        pipeline = IngestionPipeline(
            transformations=[self.embedding_model],
            vector_store=self.vector_store,
        )
        return pipeline


if __name__ == '__main__':
    pass
