"""
直接进行分析的workflow。
"""

from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
    Context
)


class AnalysisWorkflow(Workflow):
    ...


if __name__ == '__main__':
    pass
