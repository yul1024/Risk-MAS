"""

"""

from mas.models.yu_models._yu_base_multi_modal_embedding import YuBaseMultiModalEmbedding

from transformers import AutoTokenizer, AutoModel, AutoImageProcessor
import torch
import torch.nn.functional as F

from llama_index.core.base.embeddings.base import Embedding
from llama_index.core.schema import ImageType
from llama_index.core.bridge.pydantic import Field

from PIL import Image
import asyncio

from typing import Optional


if __name__ == '__main__':
    pass
