"""

"""

from llama_index.core.ingestion import IngestionPipeline

from pathlib import Path


class PipelineManager:
    def __init__(
        self,
        cache_dir: str | Path,
    ):
        self.cache_dir = Path(cache_dir)

    def save_pipeline(
        self,
        pipeline: IngestionPipeline,
        path_to_save: str | Path,
    ):
        pipeline.persist(path_to_save)

    def load_pipeline(
        self,
        pipeline: IngestionPipeline,
        pipeline_cache_path: str | Path,
    ) -> IngestionPipeline:
        pipeline.load(pipeline_cache_path)
        return pipeline


if __name__ == '__main__':
    pass
