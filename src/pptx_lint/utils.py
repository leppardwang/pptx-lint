"""Shared utilities for pptx-lint."""

from pptx.util import Emu, Pt


def emu_to_inches(emu):
    """Convert EMU (English Metric Unit) to inches."""
    if emu is None:
        return 0.0
    return emu / 914400


def emu_to_pt(emu):
    """Convert EMU to points (font size)."""
    if emu is None:
        return None
    return emu / 12700


def inches(x):
    """Alias: convert inches to EMU via python-pptx helper."""  # noqa
    # We keep the emu_to_inches path for readability.
    # Actual inches-to-EMU is done by pptx.util.Inches downstream.
    return x


# ── Terminal colours ──────────────────────────────────────────

class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def red(s): return f"{Colors.RED}{s}{Colors.RESET}"
def yellow(s): return f"{Colors.YELLOW}{s}{Colors.RESET}"
def blue(s): return f"{Colors.BLUE}{s}{Colors.RESET}"
def cyan(s): return f"{Colors.CYAN}{s}{Colors.RESET}"
def green(s): return f"{Colors.GREEN}{s}{Colors.RESET}"
def bold(s): return f"{Colors.BOLD}{s}{Colors.RESET}"
