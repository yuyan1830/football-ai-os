"""
Football AI OS

Core Validator Service

Version:
V1.0
"""


from .validation_result import ValidationResult

from .data_validator import (
    validate_file,
    validate_exists,
    validate_size
)


__all__ = [

    "ValidationResult",

    "validate_file",

    "validate_exists",

    "validate_size"

]