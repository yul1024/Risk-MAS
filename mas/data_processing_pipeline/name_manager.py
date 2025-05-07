"""

"""

from pathlib import Path


class NameManager:
    """

    """
    def __init__(self):
        ...

    def get_document_store_relative_path(
        self,
        document_store_type: str,
        pdf_name: str,
        loading_method: str,
    ) -> Path:
        """
        获取document-store的相对路径。

        Args:
            document_store_type:
            pdf_name:
            loading_method:

        Returns:
            基于数据的根文件夹的相对路径。
        """
        relative_path = Path('document_store') / f"{document_store_type}" / f"{loading_method}--{pdf_name}.json"
        return relative_path

    def get_vector_store_name(
        self,
        document_store_type: str,
        pdf_name: str,
        loading_method: str,
        embedding_method: str,
    ) -> str:
        """
        获得vector-store-path。

        具体的，这里是vector-store的名字。

        Args:
            document_store_type:
            pdf_name:
            loading_method:
            embedding_method:

        Returns:
            vector-store中的collection-name。
        """
        return f"{document_store_type}--{embedding_method}--{loading_method}--{pdf_name}"

    def get_index_store_relative_path(
        self,
        pdf_name: str,
        modality_type: str,
        loading_method: str,
        embedding_method: str,
    ) -> Path:
        relative_path = Path('index_store') / f"{modality_type}" / f"{loading_method}--{embedding_method}--{pdf_name}.json"
        return relative_path


if __name__ == '__main__':
    pass
