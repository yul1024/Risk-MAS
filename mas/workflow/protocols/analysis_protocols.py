"""
分析模块之间的通讯协议。
"""

from llama_index.core.workflow import Event
from llama_index.core.bridge.pydantic import Field, PrivateAttr


class AnalysisEvent(Event):
    content: str = Field(description="对于公司战略的识别。")
    confidence: float = Field(description="对于提交结果的置信度。")
    metadata: dict

