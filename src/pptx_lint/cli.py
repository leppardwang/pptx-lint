"""Command-line interface for pptx-lint."""

import sys
import os

from . import __version__
from .checker import check_pptx
from .reporters.console import print_report


def collect_targets(args):
    """Resolve CLI args to a list of .pptx file paths."""
    files = []
    for arg in args:
        if os.path.isdir(arg):
            for f in os.listdir(arg):
                if f.endswith('.pptx'):
                    files.append(os.path.join(arg, f))
        elif os.path.isfile(arg) and arg.endswith('.pptx'):
            files.append(arg)
        else:
            print(f"[pptx-lint] Skipping: {arg} (not a .pptx file)")
    return files


def main():
    if len(sys.argv) < 2:
        print(f"pptx-lint v{__version__}")
        print()
        print("Usage:  pptx-lint <file.pptx> [file.pptx ...]")
        print("        pptx-lint <directory>")
        print()
        print("Examples:")
        print("  pptx-lint my_presentation.pptx")
        print("  pptx-lint ./output/")
        sys.exit(1)

    targets = collect_targets(sys.argv[1:])
    if not targets:
        print("[pptx-lint] No .pptx files found.")
        sys.exit(1)

    print(f"\n{'=' * 70}")
    print(f"  pptx-lint v{__version__}  —  {len(targets)} file(s)")
    print(f"{'=' * 70}")

    grand_total = {'errors': 0, 'warnings': 0, 'infos': 0}

    for fpath in targets:
        results, name = check_pptx(fpath)
        total_e = sum(len(r['errors']) for r in results)
        total_w = sum(len(r['warnings']) for r in results)
        total_i = sum(len(r['infos']) for r in results)
        grand_total['errors'] += total_e
        grand_total['warnings'] += total_w
        grand_total['infos'] += total_i

        print_report(results, name)

    print(f"{'=' * 70}")
    print(f"  Grand total across all files:")
    print(f"    🔴  {grand_total['errors']} errors")
    print(f"    🟡  {grand_total['warnings']} warnings")
    print(f"    ℹ️   {grand_total['infos']} infos")
    print(f"{'=' * 70}\n")

    if grand_total['errors'] > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
