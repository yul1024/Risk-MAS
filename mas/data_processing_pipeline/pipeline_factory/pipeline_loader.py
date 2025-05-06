"""
实际使用时的pipeline加载器。
"""

from mas.data_processing_pipeline.pipeline_factory.pipeline_persistence_manager import PipelinePersistenceManager
from mas.data_processing_pipeline.pipeline_factory.pipeline_factory import PipelineFactory

from llama_index.core.ingestion import IngestionPipeline

from pathlib import Path


class PipelineLoader:
    """
    加载pipeline，并使用已有cache。

    这里类与pipeline-builder绑定。
    使用这个类需要已经运行过pipeline-builder。
    """
    def __init__(
        self,
        cache_dir: str | Path,
    ):
        """
        仅指定cache目录即可，文件树与pipeline-builder的统一。

        Args:
            cache_dir: pipeline-cache的目录。
        """
        self.cache_dir = Path(cache_dir)
        self.pipeline_persistence_manager = PipelinePersistenceManager()
        self.pipeline_factory = PipelineFactory()

    def load_parsing_pipeline(
        self,
        parsing_method: str,
    ) -> IngestionPipeline:
        """
        获取parsing-pipeline的方法。

        本项目的原因，实际仅text方法有，且仅为markdown解析方法。

        Args:
            parsing_method: 解析的方法。实际仅为['markdown']

        Returns:
            可使用的pipeline。
            带有缓存，使用完之后需要再次持久化。
        """
        pipeline = self.pipeline_factory.get_parsing_pipeline(parsing_method=parsing_method)
        self.pipeline_persistence_manager.load_pipeline(
            pipeline=pipeline,
            pipeline_cache_path=self.cache_dir / 'parsing' / parsing_method,
        )
        return pipeline

    def load_embedding_model_pipeline(
        self,
        model_key: str,
    ) -> IngestionPipeline:
        """
        获取embedding-model-pipeline的方法。

        本项目的原因，我以键值映射避免指定embedding-model的复杂。这样可以灵活增减选择embedding-model。

        Args:
            model_key: 模型的键，例如['model_1', 'model_2', ...]

        Returns:
            可使用的pipeline。
            带有缓存，使用完之后需要再次持久化。
        """
        pipeline = self.pipeline_factory.get_embedding_model_pipeline(model_key=model_key)
        self.pipeline_persistence_manager.load_pipeline(
            pipeline=pipeline,
            pipeline_cache_path=self.cache_dir / 'embedding' / model_key,
        )
        return pipeline


if __name__ == '__main__':
    pass
