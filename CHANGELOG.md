# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- JSON output format (`--format json`) - planned for v0.2.0
- HTML output format (`--format html`) - planned for v0.2.0
- Auto-fix capability (`--fix`) - planned for v0.2.0
- Configuration file support (`.pptxlint.yml`) - planned for v0.2.0

## [0.1.0] - 2026-06-27

### Added
- Initial release with core linting functionality
- **Overflow detection**: Detects shapes exceeding slide boundaries (left, top, right, bottom)
- **Overlap detection**: Identifies overlapping shapes (>50% overlap threshold, excludes background)
- **Fake table detection**: Finds text boxes arranged in grids that should use proper `Table` objects
- **Small font detection**: Warns about text smaller than 8pt
- **Empty slide detection**: Flags slides with zero content
- CLI tool with colored terminal output (`pptx-lint <file.pptx>` or `<directory>/`)
- Library API for programmatic use (`from pptx_lint.checker import check_pptx`)
- pytest test suite covering all detection rules
- GitHub Actions CI workflow for Python 3.9–3.13
- Comprehensive README with usage examples
- MIT license

### Technical Details
- Slide dimensions: 10" × 7.5" (16:9 widescreen)
- Coordinate system: inches-based with EMU conversion (1 inch = 914,400 EMU)
- Overflow tolerance: ±0.05" margin for edge cases
- Overlap threshold: 50% of smaller shape's area
- Fake table criteria: ≥4 shapes, ≥2 rows, ≥2 columns per row
- Font size threshold: minimum 8pt

### Known Limitations
- No automatic fixing yet (manual intervention required)
- No configuration file support (hard-coded thresholds)
- Terminal output only (no JSON/HTML reports)
- Limited to python-pptx generated files (not tested on arbitrary .pptx)
