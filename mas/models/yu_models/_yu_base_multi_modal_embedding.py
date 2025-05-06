"""
我对于llama-index中MultiModalEmbedding的异步Interface实现的简化。

模仿langchain中的runnable的设计。
"""

from llama_index.core.embeddings import MultiModalEmbedding

from abc import abstractmethod


class YuBaseMultiModalEmbedding(MultiModalEmbedding):
    """
    我对于MultiModalEmbedding的简单实现:
        - 异步interface: 仅直接调用同步方法。
        - 同步interface: 一个通用的_embed方法，可以指定encode类型，然后使用本地的transformers进行运算。

    因为llama-index工程的不稳定，简化指定:
        - Embedding直接使用list[float]。
        - ImageType直接使用str的image_path。

    子类建议实现流程:
        - init方法，初始化hf的model和processor。
        - 对于pydantic中类变量，声明init中的变量。简单方法例如: Optional[AutoModel] = Field(default=None)。
    """
    @abstractmethod
    def _embed(self, inputs: list, prompt_name: str) -> list[float]:
        """
        需要实现的方法。

        建议使用huggingface上的模型，查看示例代码直接修改。
        模型调用在init中调用，需要额外的处理。

        Args:
            inputs: transformers中常用的输入，因为常以batch处理，所以输入为list，相关调用方法已实现处理。
            prompt_name: 处理类型，['text', 'image']。

        Returns:
            llama-index中的embedding。可能需要额外转换，如text_embeddings.tolist()[0]
        """

    # ------异步方法------
    async def _aget_query_embedding(self, query: str) -> list[float]:
        return self._get_query_embedding(query)

    async def _aget_image_embedding(self, img_file_path: str) -> list[float]:
        return self._get_image_embedding(img_file_path)

    # ------同步方法------
    def _get_query_embedding(self, query: str) -> list[float]:
        return self._embed([query], prompt_name='text')

    def _get_text_embedding(self, text: str) -> list[float]:
        return self._embed([text], prompt_name='text')

    def _get_image_embedding(self, img_file_path: str) -> list[float]:
        return self._embed([img_file_path], prompt_name='image')


if __name__ == '__main__':
    pass
