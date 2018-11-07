#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import plotly.plotly as py
import plotly.tools as tls
from plotly import figure_factory as ff

import numpy as np
import matplotlib.pyplot as plt

x=[-.7, .75]
y=[0, 0]
plt.scatter(x,y, marker='o', color="r")
plt.title('Quiver Plot with Custom Arrow Size')
fig = plt.gcf()

plotly_fig = tls.mpl_to_plotly(fig)


x,y = np.meshgrid(np.arange(-2, 2, .2),
                  np.arange(-2, 2, .25))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)

quiver_fig = ff.create_quiver(x, y, u, v,
                       scale=.25,
                       arrow_scale=.8, # Sets arrow scale
                       name='quiver',
                       angle=np.pi/4,
                       line=dict(width=1))

quiver_fig.add_trace(plotly_fig['data'][0])
quiver_fig['data'][0]['line']['color'] = 'rgb(0,255,0)'

py.iplot(quiver_fig, filename='mpl-quiver-with-custom-arrow-size')