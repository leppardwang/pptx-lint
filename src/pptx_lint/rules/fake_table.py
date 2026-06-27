"""Fake-table rule: detect multiple text boxes arranged as a grid
that should probably be a proper ``Table`` object instead.
"""

EPSILON = 0.25  # inches — alignment tolerance


def check(shapes_info):
    """Return list of fake-table issues (warning severity).

    Detection criteria:
    * at least 4 text-carrying shapes
    * shapes can be grouped into ≥2 rows (by Y-centre)
    * at least 2 of those rows have ≥2 shapes each
    """
    text_shapes = []
    for info in shapes_info:
        l, t, w, h, r, b = info['bounds']
        if w > 0.3 and h > 0.2 and info['texts'] and l >= 0 and t >= 0:
            text_shapes.append({
                'idx': info['idx'],
                'left': l, 'top': t, 'w': w, 'h': h,
                'cx': l + w / 2, 'cy': t + h / 2,
                'texts': info['texts'],
            })

    if len(text_shapes) < 4:
        return []

    # Group by row (similar Y-centre)
    rows = []
    used = set()
    for ts in text_shapes:
        if ts['idx'] in used:
            continue
        row = [ts]
        used.add(ts['idx'])
        for ts2 in text_shapes:
            if ts2['idx'] in used:
                continue
            if abs(ts2['cy'] - ts['cy']) < EPSILON:
                row.append(ts2)
                used.add(ts2['idx'])
        rows.append(row)

    if len(rows) < 2:
        return []

    multi_col = [r for r in rows if len(r) >= 2]
    if len(multi_col) < 2:
        return []

    total = sum(len(r) for r in multi_col)
    samples = []
    for r in multi_col[:2]:
        for ts in r[:2]:
            if ts['texts']:
                samples.append(ts['texts'][0][:30])

    return [{
        'shape_count': total,
        'rows': len(multi_col),
        'sample_texts': samples[:3],
        'severity': 'WARN',
    }]
