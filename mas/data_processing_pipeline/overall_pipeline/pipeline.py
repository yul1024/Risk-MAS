"""
完整的pipeline。从选择pdf到构建好已持久化的index。

输入pdf的路径，配置相关参数，后就

2段分离pipeline，3处数据。

"""
from llama_index.core.schema import BaseNode

from mas.data_processing_pipeline.overall_pipeline.base_pipeline import BasePipeline

from llama_index.core import Document

from pathlib import Path


class Pipeline(BasePipeline):
    def run(
        self,
        pdf_path: str | Path,
        modality_type: str,
        loading_method: str,
        embedding_method: str,
    ):
        # 加载文档。
        documents = self.load_documents(
            pdf_path=pdf_path,
            modality_type=modality_type,
            loading_method=loading_method,
        )
        # 处理文档。
        if modality_type == "text":
            nodes = self.run_pipeline(nodes=documents)
        else:
            nodes = documents
        # 构建index，并存储。
        index = self.build_and_save_index(
            nodes=nodes,
            pdf_path=pdf_path,
            modality_type=modality_type,
            loading_method=loading_method,
            embedding_method=embedding_method,
        )
        return index


if __name__ == '__main__':
    pass
