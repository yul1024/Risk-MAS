"""
生成embedding model的工厂。
"""

from llama_index.embeddings.openai_like import OpenAILikeEmbedding

from llama_index.core.embeddings import BaseEmbedding

import os

from typing import Annotated


class EmbeddingModelFactory:
    """
    各种embedding-model的工厂。

    实现方法有:
        - OpenAILikeEmbedding，云API请求。
        - HuggingFaceEmbedding，本地推理。
        - BaseEmbeddingModel，我具体实现。
    """
    def __init__(self):
        ...

    def get_qwen_embedding_model(
        self,
        model_name: Annotated[str, "qwen上的embedding_model的名字"] = 'text-embedding-v3',
    ) -> BaseEmbedding:
        embedding_model = OpenAILikeEmbedding(
            model_name=model_name,
            api_base=os.environ['DASHSCOPE_API_BASE_URL'],
            api_key=os.environ['DASHSCOPE_API_KEY'],
        )
        return embedding_model

    def get_embedding_model_by_key(
        self,
        model_key: str,
    ) -> BaseEmbedding:
        ...


if __name__ == '__main__':
    pass
