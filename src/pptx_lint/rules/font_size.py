"""Font-size rule: detect text smaller than a minimum threshold."""

MIN_FONT_SIZE = 8  # points


def check(shapes_info):
    """Return list of font-size issues (info severity)."""
    issues = []
    for info in shapes_info:
        for fi in info.get('font_info', []):
            if fi['size'] is not None and fi['size'] < MIN_FONT_SIZE:
                issues.append({
                    'shape_idx': info['idx'],
                    'text': fi['text'][:40],
                    'font_size': fi['size'],
                    'severity': 'INFO',
                })
    return issues
