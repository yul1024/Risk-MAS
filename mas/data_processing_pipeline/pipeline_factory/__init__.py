"""
pipeline的构建、缓存、加载。

所有pipeline在使用前会被预构建并缓存。
pipeline的使用都是通过加载。
"""

from .pipeline_builder import PipelineBuilder
from .pipeline_loader import PipelineLoader


