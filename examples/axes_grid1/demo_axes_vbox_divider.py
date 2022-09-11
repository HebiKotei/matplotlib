"""
===================
`.VBoxDivider` demo
===================

Using an `.VBoxDivider` to arrange subplots.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import VBoxDivider
import mpl_toolkits.axes_grid1.axes_size as Size


def make_widths_equal(fig, rect, ax1, ax2, pad):
    # pad in inches
    divider = VBoxDivider(
        fig, rect,
        horizontal=[Size.AxesX(ax1), Size.Scaled(1), Size.AxesX(ax2)],
        vertical=[Size.AxesY(ax1), Size.Fixed(pad), Size.AxesY(ax2)])
    ax1.set_axes_locator(divider.new_locator(0))
    ax2.set_axes_locator(divider.new_locator(2))


if __name__ == "__main__":

    arr1 = np.arange(20).reshape((4, 5))
    arr2 = np.arange(20).reshape((5, 4))

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.imshow(arr1)
    ax2.imshow(arr2)

    make_widths_equal(fig, 111, ax1, ax2, pad=0.5)

    fig.text(.5, .5,
             "Both axes' location are adjusted\n"
             "so that they have equal widths\n"
             "while maintaining their aspect ratios",
             va="center", ha="center", rotation=90,
             bbox=dict(boxstyle="round, pad=1", facecolor="w"))

    plt.show()
