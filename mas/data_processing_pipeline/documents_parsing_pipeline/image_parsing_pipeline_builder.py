"""

"""

from llama_index.core.ingestion import IngestionPipeline

from pathlib import Path


class ImageParsingPipelineBuilder:
    def __init__(
        self,
        pipeline_cache_dir: str | Path,
    ):
        self.pipeline_cache_dir = Path(pipeline_cache_dir)

    def build(
            self,
    ):
        ...

    def build_pipeline(
            self,
    ):
        pipeline = IngestionPipeline(
            transformations=[]
        )


if __name__ == '__main__':
    pass
