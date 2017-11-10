#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.sankey import Sankey


# Example 1 -- Mostly defaults
# This demonstrates how to create a simple diagram by implicitly calling the
# Sankey.add() method and by appending finish() to the call to the class.

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

higgs_prod_pb = [
    ('gg', 49.8, 0),
    ('VBF', 4.18, 1),
    ('VH', 1.5 + 0.88, -1),
    ('ttH', 0.61, -1),
    ]

higgs_prod_total = sum(pb for nm, pb, orient in higgs_prod_pb)
fracs = [ (n, pb/higgs_prod_total, orient) for n, pb, orient in higgs_prod_pb]
fracs.append( ('', -1.0, 0) )

out_fracs = [
    ('', 1.0, 0),
    ('bb', -0.57, 0),
    ('ww', -0.21, -1),
    ('gg', -0.09, -1),
    (r'$\tau \tau$', -0.06, -1),
    ('cc', -0.03, 1),
    ('zz', -0.03, -1),
    ('other', -0.01, -1),
]

labels, flows, orient = zip(*fracs)

san = Sankey(
    format='%.1g',
    head_angle=120,
    ax=ax, flows=flows,
    labels=labels,
    orientations=orient,
    pathlengths=[0.1]*len(fracs)
)
out_lab, out_flow, out_ori = zip(*out_fracs)

san.add(flows=out_flow,
        labels=out_lab,
        prior=0, connect=(4,0),
        orientations=out_ori)
# san.add(flows=[0.57, -0.57/3, -0.57/3, -0.57/3],
#         labels=['', 'suck', 'it', 'danny'],
#         prior=0, connect=(1,0),
#         orientations=[0, 1, 1, 1])
# san.add(flows=[0.03, -0.03], prior=0, connect=(5, 0), orientations=[-1, 1])
san.finish()

plt.savefig('bob.pdf')
