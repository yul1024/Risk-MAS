
# path
BASE_PATH = rf""
ORIGINAL_PDF_DIR = rf"{BASE_PATH}/original_pdf"
BASE_IMAGE_PDF_DIR = rf"{BASE_PATH}/image_pdf"
DOCUMENT_STORE_DIR = rf"{BASE_PATH}/document_store"
PIPELINE_CACHE_DIR = rf"{BASE_PATH}/pipeline_cache"
VECTOR_STORE_DIR = rf"{BASE_PATH}/vector_store"


# pdf
TEXT_LOADING_MODE = ['rule', 'ocr', 'vlm', ]
TEXT_PARSING_MODE = ['markdown', ]
IMAGE_PARSING_MODE = ['none', ]


# milvus
URI = "http://localhost:19530"


# IngestionPipeline cache
# PIPELINE_CACHE=dict(
#     text=dict(
#         parsing=['markdown'],
#         embedding=['', ],
#     ),
#     image=dict(
#         parsing=['none'],
#         embedding=['', ],
#     )
# )

PIPELINE_CACHE_CONTENT = dict(
    parsing=['markdown', ],
    embedding=['model_1', 'model_2', 'model_3', 'model_4', ]
)


# vector store pipeline
VECTOR_STORE_PIPELINE = [
    ['text', 'rule', 'model_1'],
    ['text', 'ocr', 'model_1'],
    ['text', 'vlm', 'model_1'],
    ['image', 'none', 'model_2'],
    ['image', 'none', 'model_3'],
    ['image', 'none', 'model_4'],
]

