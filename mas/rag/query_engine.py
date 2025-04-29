"""
基于llama-index构建的query engine。
"""

from llama_index.core.tools import QueryEngineTool
from llama_index.core.base.base_query_engine import BaseQueryEngine

from llama_index.core.query_engine import RouterQueryEngine


class QueryEngineFactory:
    def __init__(self):
        ...

    def get_query_engine(self):
        ...


def get_query_engine_tool(
    query_engine: BaseQueryEngine,
    description: str
) -> QueryEngineTool:
    """
    将构建的query_engine转换为所有agent可以使用的tool。

    Args:
        query_engine: 通过RAG部分构建的query-engine。
        description: 工具的描述。用于异构数据路由使用。

    Returns:
        已经处理过的tool。
    """
    tool = QueryEngineTool.from_defaults(
        query_engine=query_engine,
        description=description,
    )
    return tool


if __name__ == '__main__':
    pass
