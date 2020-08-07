"""
See "Search strategies for rectangle packing" by H. Simonis and B. O'Sullivan, CP 2008.
See CP papers on short supports.

Example of Execution:
  python3 RectPacking.py -data=RectPacking_perfect-001.json
"""

import math

from pycsp3 import *

width, height = data.container
boxes = data.boxes
nBoxes = len(boxes)

# x[i] is the x-coordinate where is put the ith rectangle
x = VarArray(size=nBoxes, dom=range(width))

# y[i] is the y-coordinate where is put the ith rectangle
y = VarArray(size=nBoxes, dom=range(height))

satisfy(
    # unary constraints on x
    [x[i] + boxes[i].width <= width for i in range(nBoxes)],

    # unary constraints on y
    [y[i] + boxes[i].height <= height for i in range(nBoxes)],

    # no overlap on boxes
    NoOverlap(origins=[(x[i], y[i]) for i in range(nBoxes)], lengths=[(w, h) for (w, h) in boxes]),

    # tag(symmetry-breaking)
    [x[- 1] <= math.floor((width - boxes[- 1].width) // 2.0), y[- 1] <= x[- 1]] if width == height else None
)
