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


class NomicEmbedVisionV15(YuBaseMultiModalEmbedding):
    processor: Optional[AutoImageProcessor] = Field(default=None)
    vision_model: Optional[AutoModel] = Field(default=None)
    tokenizer: Optional[AutoTokenizer] = Field(default=None)
    text_model: Optional[AutoModel] = Field(default=None)

    def __init__(
        self,
        vision_model_path: str,
        text_model_path: str,
        **kwargs,
    ):
        # 为了冗余，这样调用。但实际不会传入参数。
        super().__init__(**kwargs)
        # image embedding model
        self.processor = AutoImageProcessor.from_pretrained(vision_model_path, trust_remote_code=True)
        self.vision_model = AutoModel.from_pretrained(vision_model_path, trust_remote_code=True)
        # text embedding model
        self.tokenizer = AutoTokenizer.from_pretrained(text_model_path, trust_remote_code=True)
        self.text_model = AutoModel.from_pretrained(text_model_path, trust_remote_code=True)

    def _embed(
        self,
        inputs: list,
        prompt_name: str,
    ) -> list[float]:
        def _mean_pooling(model_output, attention_mask):
            token_embeddings = model_output[0]
            input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

        if prompt_name == 'text':
            encoded_input = self.tokenizer(inputs, padding=True, truncation=True, return_tensors='pt')
            with torch.no_grad():
                model_output = self.text_model(**encoded_input)
            text_embeddings = _mean_pooling(model_output, encoded_input['attention_mask'])
            text_embeddings = F.layer_norm(text_embeddings, normalized_shape=(text_embeddings.shape[1],))
            text_embeddings = F.normalize(text_embeddings, p=2, dim=1)
            return text_embeddings.tolist()[0]
        elif prompt_name == 'image':
            image = Image.open(inputs[0])
            inputs = self.processor(image, return_tensors="pt")
            img_emb = self.vision_model(**inputs).last_hidden_state
            img_embeddings = F.normalize(img_emb[:, 0], p=2, dim=1)
            return img_embeddings.tolist()[0]


if __name__ == '__main__':
    pass
