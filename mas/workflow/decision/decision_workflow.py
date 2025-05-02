"""
进行最终推理和决策的workflow。
"""

from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
    Context
)


class DecisionWorkflow(Workflow):
    @step
    def identify_strategy(self):
        """

        Returns:

        """

    @step
    def project_risk(self):
        """

        Returns:

        """

    @step
    def submit_result(self):
        """

        Returns:

        """


if __name__ == '__main__':
    pass
