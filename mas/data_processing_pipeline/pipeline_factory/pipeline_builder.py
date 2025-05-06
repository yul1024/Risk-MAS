"""
初始化，构建所有的pipeline的缓存。
"""

from mas.data_processing_pipeline.pipeline_factory.pipeline_persistence_manager import PipelinePersistenceManager
from mas.data_processing_pipeline.pipeline_factory.pipeline_factory import PipelineFactory

from pathlib import Path


class PipelineBuilder:
    """
    初始化所有pipeline，使得可以在本地加载缓存。

    默认文件树结构:
        - cache_dir
            - parsing
                - parsing_method
            - embedding
                - embedding_method
    """
    def __init__(
        self,
        cache_dir: str | Path,
        pipeline_cache_content: dict[str, list[str]],
    ):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True, parents=True)

        self.pipeline_cache_content = pipeline_cache_content

        self.pipeline_persistence_manager = PipelinePersistenceManager()
        self.pipeline_factory = PipelineFactory()

    def init_parsing_pipeline(self):
        """
        初始化所有的parsing部分的pipeline。

        Returns:
            - 如果已经存在，就跳过。
            - 如果不存在，就新建。
        """
        for parsing_method in self.pipeline_cache_content['parsing']:
            cache_path = self.cache_dir / 'parsing' / parsing_method
            if cache_path.exists():
                print(f"existing parsing method {parsing_method}")
                continue
            pipeline = self.pipeline_factory.get_parsing_pipeline(parsing_method=parsing_method)
            pipeline.persist(persist_dir=str(cache_path))
            print(f"init parsing pipeline {parsing_method}")

    def init_embedding_pipeline(self):
        """
        初始化所有的embedding部分的pipeline。

        Returns:
            - 如果已经存在，就跳过。
            - 如果不存在，就新建。
        """
        for embedding_method in self.pipeline_cache_content['embedding']:
            cache_path = self.cache_dir / 'embedding' / embedding_method
            if cache_path.exists():
                print(f"existing embedding method {embedding_method}")
                continue
            pipeline = self.pipeline_factory.get_embedding_model_pipeline(model_key=embedding_method)
            pipeline.persist(persist_dir=str(cache_path))
            print(f"init embedding pipeline {embedding_method}")


if __name__ == '__main__':
    pass
