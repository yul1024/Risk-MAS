
# pdf
TEXT_LOADING_MODE = ['rule', 'ocr', 'vlm']
TEXT_PARSING_MODE = ['markdown', ]


# milvus
URI = "http://localhost:19530"


# IngestionPipeline cache
PIPELINE_CACHE=dict(
    text=dict(
        parsing=[],
        embedding=[],
    ),
    image=dict(
        parsing=[],
        embedding=[],
    )
)

