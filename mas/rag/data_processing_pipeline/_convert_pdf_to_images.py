"""
将pdf转换为图片的方法。
"""

import fitz

from pathlib import Path


def convert_pdf_to_images(
    pdf_path: str | Path,
    output_folder: str | Path = None
) -> None:
    """
    使用pymupdf将pdf进行转换。

    Args:
        pdf_path: 待转换的pdf的路径。
        output_folder: 转换后图片的保存路径。如果不提供，默认以pdf同名保存至同一路径下。

    Returns:
        转换，保存结果。
    """
    pdf_path = Path(pdf_path)
    output_folder = pdf_path.parent / pdf_path.stem if output_folder is None else Path(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)
    # 读取文件。
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        # 加载每一页
        page = pdf_document.load_page(page_num)
        # 将每一页转换为图片 (pixmap)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        # 设置图片保存路径
        image_path = output_folder / f'{page_num + 1}.png'
        # 保存为PNG文件
        pix.save(image_path)
    # 关闭PDF文件
    pdf_document.close()
    print(f"{pdf_path.name} have been saved as images in {output_folder}.")


if __name__ == '__main__':
    pass
