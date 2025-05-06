"""
文件从原始的pdf格式，到可以接入RAG的vector-store。

两个阶段:
    加载:
        - pdf --pipeline--> documents
    编码和存储:
        - documents --embedding_model--> vector-store

为了加速，
    - 文件预加载为document-store。
    - 所有pipeline进行预构建，并持久化所有缓存。
"""

from .global_setting_init_method import pre_load_pdf, init_pipeline_cache

from .loading.pre_pdf_loader import PrePdfLoader



