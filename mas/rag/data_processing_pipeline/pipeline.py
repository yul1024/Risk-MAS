"""
集成所有构建外部可索引知识库的操作。
"""

from llama_index.core.ingestion import IngestionPipeline


class PipelineFactory:
    def __init__(self):
        ...

    def get_default_pipeline(self):
        pipeline = IngestionPipeline(
            transformations=[],
        )


if __name__ == '__main__':
    pass
