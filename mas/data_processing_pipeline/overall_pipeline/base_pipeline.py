"""
完整pipeline基础功能。

实现:
    - 文档加载。
    - 文档存储。
"""

from mas.data_processing_pipeline.name_manager import NameManager
from mas.data_processing_pipeline.metadata_manager import MetadataManager
from mas.utils import DocumentStoreManager
from mas.data_processing_pipeline.pipeline_factory import PipelineLoader
from mas.data_processing_pipeline.index_pipeline import VectorStoreBuilder, IndexPipeline
from mas.models import EmbeddingModelFactory

from llama_index.core.ingestion import IngestionPipeline

from llama_index.core import Document
from llama_index.core.schema import BaseNode
from llama_index.core.indices.base import BaseIndex

from typing import Sequence

from pathlib import Path


class BasePipeline:
    """
    pdf_path --load-documents--> documents --choose-pipeline--> nodes --build-index--> index
    """
    def __init__(
        self,
        base_dir: str | Path,
    ):
        """"""
        self.base_dir = Path(base_dir)
        self.cache_dir = self.base_dir / "pipeline_cache"
        self.name_manager = NameManager()

        self.document_store_manager = DocumentStoreManager()
        self.pipeline_loader = PipelineLoader(cache_dir=self.cache_dir)
        self.vector_store_builder = VectorStoreBuilder(cache_dir=self.cache_dir)

        self.metadata_manager = MetadataManager()
        self.index_pipeline = IndexPipeline()

        self.embedding_model_factory = EmbeddingModelFactory()

    def load_documents_from_document_store(
        self,
        document_store_path: str | Path,
    ) -> list[Document]:
        """
        从文档存储中加载文档。

        使用我通用的document-store管理工具加载。

        Args:
            document_store_path: 文档存储的路径。

        Returns:
            原始存储进document-store的list[BaseNode]。
        """
        nodes = self.document_store_manager.load_nodes(document_store_path=document_store_path)
        return nodes

    def load_documents(
        self,
        pdf_path: str | Path,
        modality_type: str,
        loading_method: str,
    ):
        pdf_name = Path(pdf_path).name
        document_store_relative_path = self.name_manager.get_document_store_relative_path(
            document_store_type=modality_type,
            pdf_name=pdf_name,
            loading_method=loading_method,
        )
        document_store_path = self.base_dir / document_store_relative_path
        nodes = self.load_documents_from_document_store(document_store_path=document_store_path)
        return nodes

    def choose_pipeline(
        self,
        pipeline_type: str = 'parsing',
        key: str = 'markdown',
    ) -> IngestionPipeline:
        """
        选择pipeline。

        这里实际上仅有text的markdown解析方法。

        Args:
            pipeline_type: pipeline的类型。['parsing', 'embedding']
            key: 选择pipeline传递的参数。

        Returns:
            可运行的pipeline。
        """
        if pipeline_type == 'parsing':
            pipeline = self.pipeline_loader.load_parsing_pipeline(
                parsing_method=key,
            )
            return pipeline
        elif pipeline_type == 'embedding':
            pipeline = self.pipeline_loader.load_embedding_model_pipeline(
                model_key=key,
            )
            return pipeline

    def run_pipeline(
        self,
        nodes: list[BaseNode],
        pipeline_type: str = 'parsing',
        key: str = 'markdown',
    ) -> list[BaseNode]:
        """
        加载并运行pipeline，然后保存。

        这里进行了简化，因为仅有markdown的pipeline。

        Args:
            nodes:
            pipeline_type:
            key:

        Returns:

        """
        nodes = self.pipeline_loader.run_and_save_parsing_pipeline(
            parsing_method=key,
            nodes=nodes,
        )
        return list(nodes)

    def build_and_save_index(
        self,
        nodes: list[BaseNode],
        pdf_path: str | Path,
        modality_type: str,
        loading_method: str,
        embedding_method: str,
    ) -> BaseIndex:
        # 获取结果保存路径。
        index_relative_dir = self.name_manager.get_index_store_relative_path(
            pdf_name=Path(pdf_path).name,
            modality_type=modality_type,
            loading_method=loading_method,
            embedding_method=embedding_method,
        )
        index_dir = self.base_dir / index_relative_dir
        # 获取embedding-model。
        embedding_model = self.embedding_model_factory.get_embedding_model_by_key(model_key=embedding_method)
        # 在进行存储前，添加pipeline的metadata。
        nodes = self.metadata_manager.add_pipeline_metadata_to_nodes(
            nodes=nodes,
            pdf_path=pdf_path,
            modality_type=modality_type,
            loading_method=loading_method,
            embedding_method=embedding_method,
        )
        # 构建并持久化index。
        if modality_type == 'text':
            vector_store = self.vector_store_builder.build_text_vector_store(
                pdf_name=Path(pdf_path).name,
                loading_method=loading_method,
                embedding_method=embedding_method,
            )
        else:  # modality_type == 'image'
            vector_store = self.vector_store_builder.build_image_vector_store(
                pdf_name=Path(pdf_path).name,
                embedding_method=embedding_method,
            )
        # 构建index。
        index = self.index_pipeline.build_and_save_index(
            modality_type=modality_type,
            nodes=nodes,
            embedding_model=embedding_model,
            vector_store=vector_store,
            dir_to_save=index_dir,
        )
        return index


if __name__ == '__main__':
    pass
