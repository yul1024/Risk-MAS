"""
已经构建的pipeline获取方法。

仅pipeline本身，不考虑持久化。
"""

from mas.models import EmbeddingModelFactory

from llama_index.core.ingestion import IngestionPipeline

from llama_index.core.node_parser import MarkdownNodeParser


class PipelineFactory:
    """
    不考虑持久化，获取各种pipeline的方法。

    用策略模式封装了pipeline的选择。
    """
    def __init__(
        self,
    ):
        # 这里没使用依赖注入，embedding-model的工厂已经够完整封装了。
        self.embedding_model_factory = EmbeddingModelFactory()

    def get_parsing_pipeline(
        self,
        parsing_method: str,
    ) -> IngestionPipeline:
        """
        获取parsing-pipeline的方法。

        本项目的原因，实际仅text方法有，且仅为markdown解析方法。

        Args:
            parsing_method: 解析的方法。实际仅为['markdown']

        Returns:
            可使用的pipeline。不带有初始缓存。
        """
        if parsing_method == 'markdown':
            pipeline = self._get_markdown_pipeline()
            return pipeline

    def get_embedding_model_pipeline(
        self,
        model_key: str,
    ) -> IngestionPipeline:
        """
        获取embedding-model-pipeline的方法。

        本项目的原因，我以键值映射避免指定embedding-model的复杂。这样可以灵活增减选择embedding-model。

        Args:
            model_key: 模型的键，例如['model_1', 'model_2', ...]

        Returns:
            可使用的pipeline。不带有初始缓存。
        """
        embedding_model = self.embedding_model_factory.get_embedding_model_by_key(model_key)
        pipeline = IngestionPipeline(
            transformations=[embedding_model],
        )
        return pipeline

    def _get_markdown_pipeline(self) -> IngestionPipeline:
        """
        获取使用markdown解析的pipeline。

        这个方法写在这里很丑陋，但是仅有这一个方法，所以暂时写在这里。

        Returns:
            可使用的pipeline。不带有初始缓存。
        """
        markdown_pipeline = IngestionPipeline(
            transformations=[MarkdownNodeParser()]
        )
        return markdown_pipeline


if __name__ == '__main__':
    pass
