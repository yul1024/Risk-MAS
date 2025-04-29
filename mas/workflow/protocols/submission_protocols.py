"""
分析模块和决策模块之间的交互协议。
"""

from llama_index.core.workflow import Event
from llama_index.core.bridge.pydantic import Field, PrivateAttr


class SubmissionEvent(Event):
    """
    分析模块给决策模块提交的分析结果。
    """
    content: str = Field(description="提交给决策层的内容。")
    confidence: float = Field(description="对于提交结果的置信度。")
    metadata: dict
