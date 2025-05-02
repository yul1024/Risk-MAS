"""
决策模块之间的通讯协议。
"""

from llama_index.core.workflow import Event
from llama_index.core.bridge.pydantic import Field, PrivateAttr


class StrategyEvent(Event):
    """
    整体把握，对于战略系统的定位。
    """
    content: str = Field(description="对于公司战略的识别。")
    confidence: float = Field(description="对于提交结果的置信度。")
    metadata: dict


class RiskModelingEvent(Event):
    """
    对于风险传导的推理，进行风险建模。
    """
    content: str = Field(description="对于公司风险传导的建模。")
    confidence: float = Field(description="对于提交结果的置信度。")
    metadata: dict


class FinalDecisionEvent(Event):
    """
    整个MAS最终推理和判断的结果。
    """
    content: str = Field(description="最终的分析结果。")
    confidence: float = Field(description="对于提交结果的置信度。")
    metadata: dict

