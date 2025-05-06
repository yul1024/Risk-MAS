"""

"""

from llama_index.core.ingestion import IngestionPipeline

from llama_index.core.node_parser import MarkdownNodeParser

from llama_index.core.embeddings import BaseEmbedding
from llama_index.core.schema import BaseNode
from llama_index.core.vector_stores.types import BasePydanticVectorStore

from pathlib import Path


class PipelineFactory:
    def __init__(
        self,
        cache_dir: str | Path,
    ):
        self.cache_dir = Path(cache_dir)

    def get_nodes_parsing_pipeline(
        self,
        mode: str,
    ):
        if mode == 'markdown':
            return self.get_markdown_pipeline()

    def get_embedding_model_pipeline(
        self,
        embedding_model: str,
    ) -> IngestionPipeline:
        ...

    def get_markdown_pipeline(self) -> IngestionPipeline:
        markdown_pipeline = IngestionPipeline(
            transformations=[MarkdownNodeParser()]
        )
        return markdown_pipeline


if __name__ == '__main__':
    pass
