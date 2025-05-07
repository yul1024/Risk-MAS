"""

"""

from mas.data_processing_pipeline.overall_pipeline import Pipeline


def test_pipeline_1():
    pipeline = Pipeline(
        base_dir=r"D:\dataset\risk_mas_t"
    )
    pipeline.run(
        pdf_path=r"D:\dataset\risk_mas_t\original_pdf\1910.13461v1.pdf",
        modality_type='text',
        loading_method='rule',
        embedding_method='model_1',
    )


def test_pipeline_2():
    pipeline = Pipeline(
        base_dir=r"D:\dataset\risk_mas_t"
    )
    pipeline.run(
        pdf_path=r"D:\dataset\risk_mas_t\original_pdf\1910.13461v1.pdf",
        modality_type='image',
        loading_method='none',
        embedding_method='model_1',
    )


if __name__ == '__main__':
    # test_pipeline_1()
    test_pipeline_2()
