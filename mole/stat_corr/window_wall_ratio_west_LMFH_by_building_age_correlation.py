# OeQ autogenerated correlation for 'Window/Wall Ratio West in Correlation to the Building Age'

import math
import numpy as np
from . import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Western Direction'
    A_WIN_W_BY_AW= oeq.correlation(
    const= -4590.02660382,
    a=     9.07172432591,
    b=     -0.00670666922272,
    c=     2.19817135124e-06,
    d=     -2.69506230435e-10,
    mode= "lin")

    return dict(A_WIN_W_BY_AW=A_WIN_W_BY_AW.lookup(*xin))

