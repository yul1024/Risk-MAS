
# path
BASE_PATH = rf""
ORIGINAL_PDF_DIR = rf"{BASE_PATH}"
BASE_IMAGE_PDF_DIR = rf"{BASE_PATH}"
DOCUMENT_STORE_DIR = rf"{BASE_PATH}"
PIPELINE_CACHE_DIR = rf"{BASE_PATH}"
VECTOR_STORE_DIR = rf"{BASE_PATH}"


# pdf
TEXT_LOADING_MODE = ['rule', 'ocr', 'vlm', ]
TEXT_PARSING_MODE = ['markdown', ]
IMAGE_PARSING_MODE = ['none', ]


# milvus
URI = "http://localhost:19530"


# IngestionPipeline cache
PIPELINE_CACHE=dict(
    text=dict(
        parsing=['markdown'],
        embedding=['', ],
    ),
    image=dict(
        parsing=['none'],
        embedding=['', ],
    )
)

