"""
从documents到nodes的pipeline。
"""

from llama_index.core.ingestion import IngestionPipeline

from llama_index.core.node_parser import MarkdownNodeParser

from llama_index.core.node_parser import NodeParser
from llama_index.core import Document

from pathlib import Path


class DocumentParsingPipelineFactory:
    def __init__(self):
        ...

    def get_parsing_pipeline(
        self,
        mode: str = 'markdown',
    ) -> IngestionPipeline:
        """
        策略模式封装的文档解析pipeline。

        Args:
            mode (str): 将documents解析为nodes的方法。

        Returns:
            可运行的IngestionPipeline的实例。
            输入documents，输出nodes。
        """
        if mode == "markdown":
            return self.get_markdown_parsing_pipeline()

    def get_base_parsing_pipeline(
        self,
        node_parsers: list[NodeParser],
    ) -> IngestionPipeline:
        """
        使用IngestionPipeline，封装文档解析过程。
        自定义node-parser的组合。

        Args:
            node_parsers (list): transformations，将documents进行处理的一系列流程。

        Returns:
            可运行的IngestionPipeline的实例。
        """
        pipeline = IngestionPipeline(
            transformations=[*node_parsers],
        )
        return pipeline

    def get_markdown_parsing_pipeline(self) -> IngestionPipeline:
        """
        markdown解析pipeline。

        Returns:
            可运行的IngestionPipeline的实例。
            这个方法返回的是对基于markdown格式的document仅使用markdown对应的解析方法。
        """
        markdown_pipeline = self.get_base_parsing_pipeline(
            node_parsers=[MarkdownNodeParser()],
        )
        return markdown_pipeline


if __name__ == '__main__':
    pass
