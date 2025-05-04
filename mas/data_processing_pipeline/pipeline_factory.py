"""
由documents到vector-store的pipeline。

使用llama-index内置的IngestionPipeline，使用缓存以加速和节省资源。
"""

from llama_index.core.ingestion import IngestionPipeline


class PipelineFactory:
    def __init__(self):
        ...

    def get_text_only_pipeline(self):
        """
        仅提取pdf中文本的部分。

        Returns:

        """

    def get_ocr_pipeline(self):
        """
        使用ocr工具，提取pdf中布局的信息。

        Returns:

        """
        # return DocumentPipeline(
        #     node_parser=MarkdownNodeParser(),
        #     embedding_model=,
        #     vector_store=,
        # )

    def get_multi_modal_pipeline(self):
        ...


if __name__ == '__main__':
    pass

