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
        name='model_1',
        dim=1,
        type='text',
        path='model_1.h5',
    ),
)

