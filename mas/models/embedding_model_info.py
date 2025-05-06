"""
所有相关的embedding-model
"""

from pydantic import BaseModel


class EmbeddingModel(BaseModel):
    name: str
    dim: int
    type: str
    path: str


EMBEDDING_MODEL_INFO = dict(
    model_1=EmbeddingModel(
        name='nomic-embed-text-v1.5',
        dim=768,
        type='text',
        path='nomic-ai/nomic-embed-text-v1.5',
    ),
    model_2=EmbeddingModel(
        name='nomic-embed-vision-v1.5',
        dim=768,
        type='image',
        path='nomic-ai/nomic-embed-vision-v1.5',
    ),
    model_3=EmbeddingModel(
        name='clip-vit-large-patch14',
        dim=1,
        type='image',
        path='openai/clip-vit-large-patch14',
    ),
    model_4=EmbeddingModel(
        name='colnomic-embed-multimodal-3b',
        dim=1,
        type='image',
        path='omic-ai/colnomic-embed-multimodal-3b',
    ),
)

