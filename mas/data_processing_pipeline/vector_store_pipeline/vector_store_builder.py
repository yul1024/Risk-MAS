"""

"""

from mas.data_processing_pipeline.pipeline_factory import PipelineLoader

from llama_index.core.ingestion import IngestionPipeline

from pathlib import Path


class VectorStoreBuilder:
    def __init__(
        self,
        base_dir: str | Path,
    ):
        self.base_dir = Path(base_dir)
        self.cache_dir = self.base_dir / 'cache_dir'

        self.pipeline_loader = PipelineLoader(cache_dir=self.cache_dir)

    def get_vector_store_pipeline(
        self,
        model_key: str,
    ):
        vector_store_pipeline = self.pipeline_loader.load_embedding_model_pipeline(model_key=model_key)

    def build_text_vector_store(
        self,
        pdf_name: str,
        loading_method: str,
        embedding_method: str,
    ):
        ...

    def build_image_vector_store(
        self,
        pdf_name: str,
        embedding_method: str,
    ):
        ...

    def get_document_store_path(
        self,
        document_store_type: str,
        pdf_name: str,
        loading_method: str,
    ) -> Path:
        relative_path = Path('document_store') / f"{document_store_type}" / f"{loading_method}--{pdf_name}.json"
        return relative_path

    def get_vector_store_path(
        self,
        document_store_type: str,
        pdf_name: str,
        loading_method: str,
        embedding_method: str,
    ) -> str:
        return f"{document_store_type}--{embedding_method}--{loading_method}--{pdf_name}"


if __name__ == '__main__':
    pass
