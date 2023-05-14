# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:27:44 2022

@author: Bisar
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.projections import PolarAxes
from mpl_toolkits.axisartist.floating_axes import GridHelperCurveLinear, FloatingSubplot
import mpl_toolkits.axisartist.grid_finder as gf


def generate_polar_axes():
    polar_trans = PolarAxes.PolarTransform()

    # Setup the axis, here we map angles in degrees to angles in radius
    phi_degree = np.arange(0, 90, 10)
    tlocs = phi_degree * np.pi / 180
    gl1 = gf.FixedLocator(tlocs)  # Positions
    tf1 = gf.DictFormatter(dict(zip(tlocs, map(str, phi_degree))))

    # Standard deviation axis extent
    radius_min = 0
    radius_max = 1

    # Set up the axes range in the parameter "extremes"
    ghelper = GridHelperCurveLinear(polar_trans, extremes=(0, np.pi / 2,  # 1st quadrant
                                                           radius_min, radius_max),
                                    grid_locator1=gl1,
                                    tick_formatter1=tf1,
                                    )

    figure = plt.figure()

    floating_ax = FloatingSubplot(figure, 111, grid_helper=ghelper)
    figure.add_subplot(floating_ax)

    # Adjust axes
    floating_ax.axis["top"].set_axis_direction("bottom")  # "Angle axis"
    floating_ax.axis["top"].toggle(ticklabels=True, label=True)
    floating_ax.axis["top"].major_ticklabels.set_axis_direction("top")
    floating_ax.axis["top"].label.set_axis_direction("top")
    floating_ax.axis["top"].label.set_text("angle (deg)")

    floating_ax.axis["left"].set_axis_direction("bottom")  # "X axis"
    floating_ax.axis["left"].label.set_text("radius")

    floating_ax.axis["right"].set_axis_direction("top")  # "Y axis"
    floating_ax.axis["right"].toggle(ticklabels=True)
    floating_ax.axis["right"].major_ticklabels.set_axis_direction("left")

    floating_ax.axis["bottom"].set_visible(False)  # Useless

    # Contours along standard deviations
    floating_ax.grid(True)
    floating_ax.set_title("Quarter polar plot")

    data_ax = floating_ax.get_aux_axes(polar_trans)  # return the axes that can be plotted on

    return figure, data_ax


if __name__ == "__main__":
    
    # Plot data onto the defined polar axes
    fig, ax = generate_polar_axes()

    theta = np.random.rand(10) * np.pi / 2

    radius = np.random.rand(10)

    ax.scatter(theta, radius)

    fig.savefig("test.png")