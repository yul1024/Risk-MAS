"""
测试pdf预加载工具的运行。
"""

from mas.data_processing_pipeline import PrePdfLoader


def test_pre_pdf_loader():
    pre_pdf_loader = PrePdfLoader(
        pdf_dir=r"D:\dataset\risk_mas_t\original_pdf",
        base_image_pdf_dir=r"D:\dataset\risk_mas_t\image_pdf",
        document_store_dir=r"D:\dataset\risk_mas_t\document_store",
    )
    pre_pdf_loader.batch_process_text(loading_methods=['rule'])
    pre_pdf_loader.batch_process_image(is_need_convert=True)


if __name__ == '__main__':
    test_pre_pdf_loader()
