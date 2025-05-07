"""
测试pipeline初始化构建器的运行。
"""

from mas.data_processing_pipeline.pipeline_factory import PipelineBuilder


def test_pipeline_builder():
    pipeline_builder = PipelineBuilder(
        cache_dir=r"D:\dataset\risk_mas_t/pipeline_cache",
        pipeline_cache_content=dict(
            parsing=['markdown', ],
            embedding=['model_1', 'model_2', 'model_3', 'model_4', ]
        ),
    )
    pipeline_builder.init_parsing_pipeline()


if __name__ == '__main__':
    test_pipeline_builder()
