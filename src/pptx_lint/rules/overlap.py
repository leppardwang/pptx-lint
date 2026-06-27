"""Overlap rule: detect shapes that overlap each other."""


def check(shapes_info):
    """Return list of overlap issues (warning severity)."""
    issues = []
    rects = []

    for info in shapes_info:
        l, t, w, h, r, b = info['bounds']
        if w == 0 or h == 0:
            continue
        rects.append((info['idx'], l, t, r, b, info['texts'], w * h))

    if not rects:
        return issues

    max_area = max(a for (_, _, _, _, _, _, a) in rects)

    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            idx1, l1, t1, r1, b1, t1s, a1 = rects[i]
            idx2, l2, t2, r2, b2, t2s, a2 = rects[j]

            # Skip full-slide background shapes (no text, huge area)
            if a1 > max_area * 0.8 and not t1s:
                continue
            if a2 > max_area * 0.8 and not t2s:
                continue

            ox = max(0.0, min(r1, r2) - max(l1, l2))
            oy = max(0.0, min(b1, b2) - max(t1, t2))

            if ox > 0 and oy > 0:
                oa = ox * oy
                threshold = min(a1, a2) * 0.5
                if oa > threshold:
                    name1 = t1s[0] if t1s else f"Shape {idx1}"
                    name2 = t2s[0] if t2s else f"Shape {idx2}"
                    issues.append({
                        'shapes': (idx1, idx2),
                        'names': (name1, name2),
                        'overlap_area': f"{oa:.2f} sq.in.",
                        'severity': 'WARN',
                        'texts': (t1s, t2s),
                    })

    return issues
