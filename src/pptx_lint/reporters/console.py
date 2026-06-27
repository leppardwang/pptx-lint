"""Console (terminal) reporter for pptx-lint."""

from ..utils import red, yellow, cyan, blue, green, bold


def print_report(all_results, filename):
    """Print a colourised per-file report to stdout."""
    total_e = sum(len(r['errors']) for r in all_results)
    total_w = sum(len(r['warnings']) for r in all_results)
    total_i = sum(len(r['infos']) for r in all_results)
    total_slides = len(all_results)
    empty = sum(1 for r in all_results if r['is_empty'])

    print(f"\n{'=' * 70}")
    print(f"  {bold('pptx-lint report')}")
    print(f"  File: {blue(filename)}")
    print(f"{'=' * 70}")
    print(f"  Slides: {total_slides}  |  Empty: {empty}")
    print(f"  {red(f'Errors: {total_e}')}  "
          f"{yellow(f'Warnings: {total_w}')}  "
          f"{cyan(f'Infos: {total_i}')}")
    print(f"{'=' * 70}")

    for result in all_results:
        sn = result['slide_num']
        if not (result['errors'] or result['warnings'] or result['infos']):
            continue

        label = f'[Slide {sn}]'
        empty_label = ' (EMPTY)' if result['is_empty'] else ''
        print(f"\n{green(label)}{empty_label}")

        if result['text_content']:
            preview = ' | '.join(result['text_content'][:2])
            if len(preview) > 80:
                preview = preview[:80] + '...'
            print(f"  {blue('Content:')} {preview}")

        for e in result['errors']:
            et = e['type']
            print(f"  {red('  ✗ [' + et + ']')} {e['detail']}")

        for w in result['warnings']:
            wt = w['type']
            print(f"  {yellow('  ▲ [' + wt + ']')} {w['detail']}")

        for i in result['infos']:
            it = i['type']
            print(f"  {cyan('  i [' + it + ']')} {i['detail']}")

    # Summary line
    if total_e == 0 and total_w == 0:
        print(f"\n  {green('✓ No issues found!')}")
    elif total_e == 0:
        print(f"\n  {yellow('⚠ Warnings only, no errors.')}")
    else:
        print(f"\n  {red('✗ Errors detected — review above.')}")
    print()
