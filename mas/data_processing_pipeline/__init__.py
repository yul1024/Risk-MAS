"""
文件从原始的pdf格式，到可以接入RAG的vector-store。

两个sub-pipeline:
    - pdf --pipeline--> documents
编码和存储:
    - documents --embedding_model--> vector-store
"""

