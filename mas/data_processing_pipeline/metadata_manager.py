"""

"""

from llama_index.core.schema import BaseNode

from pathlib import Path


class MetadataManager:
    def __init__(self):
        ...

    def add_metadata_to_nodes(
        self,
        nodes: list[BaseNode],
        metadata: dict,
    ) -> list[BaseNode]:
        """
        在node的metadata字段中，添加一个自定义的dict。

        Args:
            nodes: 原本的nodes。
            metadata: 需要添加的字段，在已有的metadata上添加。更新的方式，会覆盖原有的dict。

        Returns:
            添加了metadata的nodes，这个操作实际上是原地的。
        """
        for node in nodes:
            node.metadata.update(metadata)
        return nodes

    def add_pipeline_metadata_to_nodes(
        self,
        nodes: list[BaseNode],
        pdf_path: str | Path,
        modality_type: str,
        loading_method: str,
        embedding_method: str,
    ) -> list[BaseNode]:
        """
        本项目设计的metadata的内容。

        添加至yu_metadata，与原本的metadata不冲突，也方便筛选。

        Args:
            nodes:
            pdf_path:
            modality_type:
            loading_method:
            embedding_method:

        Returns:
            更新过后的nodes。实际这个更新是原地的。
        """
        pdf_name = Path(pdf_path).name
        pipeline_metadata = dict(
            modality_type=modality_type,
            loading_method=loading_method,
            embedding_method=embedding_method,
            pdf_name=pdf_name,
            # pdf_path=str(pdf_path),
        )
        nodes = self.add_metadata_to_nodes(
            nodes=nodes,
            metadata=dict(yu_metadata=pipeline_metadata)
        )
        return nodes


if __name__ == '__main__':
    pass
