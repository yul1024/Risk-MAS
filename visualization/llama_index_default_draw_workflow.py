"""
llama-index内置默认的workflow可视化工具。
"""

from llama_index.utils.workflow import draw_all_possible_flows
from llama_index.core.workflow import Workflow

from typing import Annotated


def draw_workflow(
    workflow: Annotated[Workflow, "由llama-index构建的workflow"],
    path_to_save: Annotated[str, "workflow可视化保存的路径，需要是html扩展名。"],
):
    draw_all_possible_flows(workflow, path_to_save)


if __name__ == '__main__':
    pass
