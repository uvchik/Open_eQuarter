# OeQ autogenerated correlation for 'Window/Wall Ratio East in Correlation to the Building Age'

import math
import numpy as np
from . import oeqCorrelation as oeq
def window_wall_east_ratio_SFH_by_building_age_correlation(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Eastern Direction'
    A_WIN_E_BY_AW= oeq.correlation(
    const= 3443.04500822,
    a=     -7.03961089554,
    b=     0.00539428257241,
    c=     -1.83599645651e-06,
    d=     2.34190543055e-10,
    mode= "lin")

    return dict(A_WIN_E_BY_AW=A_WIN_E_BY_AW.lookup(*xin))

