"""
测试LLM和embedding_model是否可以正常请求。
"""

from mas.utils import LLMFactory, EmbeddingModelFactory


def test_llm():
    llm_factory = LLMFactory()


def test_embedding_model():
    embedding_model_factory = EmbeddingModelFactory()


if __name__ == '__main__':
    pass
