"""

"""

from mas.data_processing_pipeline.metadata_manager import MetadataManager
from mas.data_processing_pipeline.index_pipeline.index_manager import IndexManager

from llama_index.core.indices import MultiModalVectorStoreIndex

from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.schema import BaseNode, Document
from llama_index.core.vector_stores.types import BasePydanticVectorStore
from llama_index.core.indices.base import BaseIndex

from pathlib import Path


class IndexPipeline:
    def __init__(self):
        self.index_manager = IndexManager()

    def build_and_save_index(
        self,
        nodes: list[BaseNode],
        modality_type: str,
        embedding_model: BaseEmbedding,
        vector_store: BasePydanticVectorStore,
        dir_to_save: str | Path,
    ) -> BaseIndex:
        if modality_type == 'text':
            index = self.index_manager.build_index_from_nodes(
                nodes=nodes,
                embedding_model=embedding_model,
                vector_store=vector_store,
            )
            self.index_manager.save_index(
                index=index,
                dir_to_save=dir_to_save,
            )
            return index
        elif modality_type == 'image':
            index = self.index_manager.build_multimodal_index(
                nodes=nodes,
                embedding_model=embedding_model,
                vector_store=vector_store,
            )
            self.index_manager.save_index(
                index=index,
                dir_to_save=dir_to_save,
            )
            return index


if __name__ == '__main__':
    pass
