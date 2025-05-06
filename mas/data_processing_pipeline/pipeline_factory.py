"""
由documents到vector-store的pipeline。

使用llama-index内置的IngestionPipeline，使用缓存以加速和节省资源。
"""

from mas.global_config import PIPELINE_CACHE_CONTENT

from llama_index.core.ingestion import IngestionPipeline


class PipelineFactory:
    def __init__(self):
        ...


if __name__ == '__main__':
    pass

