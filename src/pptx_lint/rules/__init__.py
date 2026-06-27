"""Lint rules for pptx-lint."""

from . import overflow
from . import overlap
from . import fake_table
from . import font_size

__all__ = ['overflow', 'overlap', 'fake_table', 'font_size']
