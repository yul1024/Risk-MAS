"""
生成embedding model的工厂。
"""

from llama_index.embeddings.openai_like import OpenAILikeEmbedding
import os

from typing import Annotated


class EmbeddingModelFactory:
    def __init__(self):
        ...

    def get_qwen_embedding_model(
        self,
        model_name: Annotated[str, "qwen上的embedding_model的名字"] = 'text-embedding-v3',
    ) -> OpenAILikeEmbedding:
        embedding_model = OpenAILikeEmbedding(
            model_name=model_name,
            api_base=os.environ['DASHSCOPE_API_BASE_URL'],
            api_key=os.environ['DASHSCOPE_API_KEY'],
        )
        return embedding_model


if __name__ == '__main__':
    pass
