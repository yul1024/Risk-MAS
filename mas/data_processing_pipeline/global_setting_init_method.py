"""
初始化pipeline-cache的函数。

不指定kwargs的情况下，以全局设定初始化。
"""

from mas.global_config import ORIGINAL_PDF_DIR, BASE_IMAGE_PDF_DIR, DOCUMENT_STORE_DIR
from mas.global_config import PIPELINE_CACHE_DIR, PIPELINE_CACHE_CONTENT

from mas.data_processing_pipeline.loading import PrePdfLoader
from mas.data_processing_pipeline.pipeline_factory import PipelineBuilder

from pathlib import Path


def pre_load_pdf(
    loading_methods: list[str] = None,
    is_need_convert: bool = True,

    pdf_dir: str | Path = ORIGINAL_PDF_DIR,
    base_image_pdf_dir: str | Path = BASE_IMAGE_PDF_DIR,
    document_store_dir: str | Path = DOCUMENT_STORE_DIR,
):
    """
    使用全局设定的预加载方法。

    如果重复运行，text部分不会受影响，图片需要指定为false以加速。

    Args:
        loading_methods: text加载的方法。
        is_need_convert: 是否转换pdf为image。
        pdf_dir: 原始pdf文件的保存文件夹。默认使用全局设定。
        base_image_pdf_dir: 图片文件的保存文件夹。默认使用全局设定。
        document_store_dir: document-store的保存文件夹。默认使用全局设定。

    Returns:
        完成全部的转换。
    """
    # 默认执行所有加载方法。
    if loading_methods is None:
        loading_methods = ['rule', 'ocr', 'vlm']
    # 预加载器。
    pre_pdf_loader = PrePdfLoader(
        pdf_dir=pdf_dir,
        base_image_pdf_dir=base_image_pdf_dir,
        document_store_dir=document_store_dir,
    )
    # 进行预加载。先处理图片是因为没有调用vlm不易出错。
    pre_pdf_loader.batch_process_image(is_need_convert=is_need_convert)
    pre_pdf_loader.batch_process_text(loading_methods=loading_methods)


def init_pipeline_cache(
    cache_dir: str | Path = PIPELINE_CACHE_DIR,
    pipeline_cache_content: dict[str, list[str]] = PIPELINE_CACHE_CONTENT,
):
    """
    使用全局设定的初始化pipeline-cache方法。

    这个方法在修改处理方法的时候进行增减也可随意重复运行。

    Args:
        cache_dir: cache的保存路径。默认使用全局设定。
        pipeline_cache_content: pipeline的类型。默认使用全局设定。

    Returns:
        初始化所有cache。
    """
    pipeline_builder = PipelineBuilder(
        cache_dir=cache_dir,
        pipeline_cache_content=pipeline_cache_content,
    )
    pipeline_builder.init_parsing_pipeline()
    pipeline_builder.init_embedding_pipeline()


if __name__ == '__main__':
    init_pipeline_cache()
    pre_load_pdf()
