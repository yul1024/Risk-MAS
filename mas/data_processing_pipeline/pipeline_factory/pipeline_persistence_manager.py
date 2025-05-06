"""
pipeline持久化工具类。
"""

from llama_index.core.ingestion import IngestionPipeline

from pathlib import Path


class PipelinePersistenceManager:
    """
    pipeline持久化方法管理器。

    无状态的工具类，需要自行管理路径和pipeline的对应。
    """
    def __init__(
        self,
    ):
        ...

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

    def load_pipeline_with_check(
        self,
        pipeline: IngestionPipeline,
        pipeline_cache_path: str | Path,
    ) -> IngestionPipeline | None:
        if not pipeline_cache_path.exists():
            print(f"{pipeline_cache_path} does not exist")
            return
        pipeline.load(pipeline_cache_path)
        return pipeline


if __name__ == '__main__':
    pass
