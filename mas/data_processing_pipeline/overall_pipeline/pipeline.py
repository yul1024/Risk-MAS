"""
完整的pipeline。

2段分离pipeline，3处数据。
"""

from mas.data_processing_pipeline.overall_pipeline.base_pipeline import BasePipeline

from llama_index.core import Document


class TextPipeline(BasePipeline):
    ...



class ImagePipeline(BasePipeline):
    ...


if __name__ == '__main__':
    pass
