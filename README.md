# pptx-lint

**Lint / quality checker for python-pptx presentations.**

[![PyPI](https://img.shields.io/pypi/v/pptx-lint)](https://pypi.org/project/pptx-lint/)
[![Python](https://img.shields.io/pypi/pyversions/pptx-lint)](https://pypi.org/project/pptx-lint/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Why?

If you generate PowerPoint files with [python-pptx](https://python-pptx.readthedocs.io/),
you've probably run into these problems:

- 🔴 **Overflow** — Text boxes or tables exceeding slide boundaries
- 🟡 **Overlap** — Shapes covering each other because of hard-coded coordinates
- 🟡 **Fake tables** — Multiple text boxes trying (and failing) to look like a table
- ℹ️ **Small fonts** — Text too small to read
- 🔴 **Empty slides** — Slides without any content

**pptx-lint** automatically detects all of these, giving you a clear report
so you can fix them *before* presenting.

---

## Quick start

```bash
pip install pptx-lint

# Check a single file
pptx-lint presentation.pptx

# Check all files in a directory
pptx-lint ./output/
```

---

## Example output

```
======================================================================
  pptx-lint report
  File: my_presentation.pptx
======================================================================
  Slides: 12  |  Empty: 0
  Errors: 3  |  Warnings: 5  |  Infos: 2
======================================================================

[Slide 4]
  Content: Performance Metrics | Results
  ✗ [Overflow] Shape#3 (Performance table): right overflow (r=12.80" > 10.00")
  ▲ [FakeTable] 6 text boxes form a grid (e.g.: Precision, Recall)

[Slide 7]
  Content: System Architecture Overview
  ▲ [Overlap] Shape#2 overlaps Shape#4 — overlap area: 2.30 sq.in.

[Slide 9]
  Content: References
  i [SmallFont] Shape#1: 'Acknowledgements' font = 7pt (< 8pt)
```

---

## Checks

| Rule | Severity | What it detects |
|------|----------|-----------------|
| **Overflow** | 🔴 Error | Shapes whose `left`/`top` < 0 or `right`/`bottom` > slide dimensions |
| **Empty slide** | 🔴 Error | Slides with zero shapes |
| **Overlap** | 🟡 Warning | Two shapes overlapping > 50% of the smaller shape's area |
| **Fake table** | 🟡 Warning | ≥4 text boxes arranged in a ≥2×2 grid (should use `add_table()`) |
| **Small font** | ℹ️ Info | Text smaller than 8 pt |

---

## Use as a library

```python
from pptx_lint.checker import check_pptx

results, filename = check_pptx("my_slides.pptx")
for slide in results:
    for err in slide['errors']:
        print(f"Slide {slide['slide_num']}: {err['detail']}")
```

---

## Development

```bash
git clone https://github.com/YOUR_USERNAME/pptx-lint.git
cd pptx-lint
pip install -e ".[dev]"
pytest
```

---

## Related

- [python-pptx](https://python-pptx.readthedocs.io/) — the library that creates `.pptx` files
- [python-pptx-table](https://pypi.org/project/python-pptx-table/) — helpers for Table objects

---

## License

MIT
