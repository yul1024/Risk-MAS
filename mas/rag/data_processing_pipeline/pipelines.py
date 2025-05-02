"""
集成所有构建外部可索引知识库的操作。
"""

from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import NodeParser
from llama_index.core.embeddings import BaseEmbedding
from llama_index.core.vector_stores.types import BasePydanticVectorStore


class DocumentPipeline:
    """
    将一个Document对象处理为vector-store的pipeline。

    封装了llama-index提供的IngestionPipeline。
    """
    def __init__(
        self,
        node_parser: NodeParser,
        embedding_model: BaseEmbedding,
        vector_store: BasePydanticVectorStore,
    ):
        self.node_parser = node_parser
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def get_pipeline(self) -> IngestionPipeline:
        pipeline = IngestionPipeline(
            transformations=[
                self.node_parser,
                self.embedding_model,
            ],
            vector_store=self.vector_store,
        )
        return pipeline


class PDFPipeline:
    """
    将一个pdf处理为vector-store的pipeline。
    """
    def __init__(self, pipeline: IngestionPipeline):
        ...


if __name__ == '__main__':
    pass

