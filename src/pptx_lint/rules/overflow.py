"""Overflow rule: detect shapes that exceed slide boundaries."""

from ..utils import emu_to_inches


def check(slide_width, slide_height, shapes_info):
    """Return list of overflow issues.

    Each issue dict:
        shape_idx, shape_name, bounds, issues (list of str), texts
    """
    issues = []
    sw = slide_width   # already in inches
    sh = slide_height

    TOLERANCE = 0.05  # inches, small positive margin

    for info in shapes_info:
        left, top, width, height, right, bottom = info['bounds']
        name = (info['texts'][0] if info['texts']
                else f"Shape {info['idx']}")

        overflow_msgs = []
        if left < 0:
            overflow_msgs.append(f"left overflow ({left:.2f}\")")
        if top < 0:
            overflow_msgs.append(f"top overflow ({top:.2f}\")")
        if right > sw + TOLERANCE:
            overflow_msgs.append(
                f"right overflow (r={right:.2f}\" > {sw:.2f}\")")
        if bottom > sh + TOLERANCE:
            overflow_msgs.append(
                f"bottom overflow (b={bottom:.2f}\" > {sh:.2f}\")")

        if overflow_msgs:
            issues.append({
                'shape_idx': info['idx'],
                'shape_name': name,
                'bounds': (left, top, width, height),
                'issues': overflow_msgs,
                'severity': 'ERROR',
                'texts': info['texts'],
            })

    return issues
