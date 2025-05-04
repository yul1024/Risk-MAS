"""
llama-index中集成的加载图片文档的方法。
"""

from llama_index.core import SimpleDirectoryReader

from llama_index.core import Document

from pathlib import Path


class SimpleImageLoader:
    """
    使用llama-index的集成方法加载图片。
    """
    def __init__(
        self,
        pdf_images_dir: str | Path,
    ):
        self.pdf_images_dir = Path(pdf_images_dir)

    def run(self) -> list[Document]:
        """
        主要方法。
        使用简单的集成方法进行加载。

        Returns:
            图片文档对象的list。
        """
        loader = SimpleDirectoryReader(self.pdf_images_dir)
        image_documents = loader.load_data()
        return image_documents


if __name__ == '__main__':
    pass
