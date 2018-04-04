# OeQ autogenerated correlation for 'Window/Wall Ratio at Multi Family Houses in Correlation to the Building Age'

import math
import numpy as np
def window_wall_ratio_MFH_by_building_age(xin,mode='distribution'):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Eastern Direction'
    Const= -36887.3474112
    a=     75.3645550276
    b=     -0.0577161046535
    c=     1.96362693858e-05
    d=     -2.50421507957e-09
    A_WIN_E_BY_AW = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Window to Wall Ratio in Southern Direction'
    Const=  20056.562623
    a=     -41.0808701415
    b=     0.031538206644
    c=     -1.07556725787e-05
    d=     1.37486214954e-09
    A_WIN_S_BY_AW = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Window to Wall Ratio in Western Direction'
    Const= -36887.3474112
    a=     75.3645550276
    b=     -0.0577161046535
    c=     1.96362693858e-05
    d=     -2.50421507957e-09
    A_WIN_W_BY_AW = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Window to Wall Ratio in Northern Direction'
    Const= 13926.9395997
    a=     -28.5763303241
    b=     0.0219763900267
    c=     -7.50745126781e-06
    d=     9.61237974674e-10
    A_WIN_N_BY_AW = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Window to Wall Ratio in all Directions'
    Const= -38379.8302692
    a=     78.1944364451
    b=     -0.0597196461799
    c=     2.02639207707e-05
    d=     -2.57760070411e-09
    A_WIN_BY_AW = Const + a*x + b*x**2 + c*x**3 + d*x**4
 
    l_sum = A_WIN_E_BY_AW + A_WIN_S_BY_AW + A_WIN_W_BY_AW + A_WIN_N_BY_AW + A_WIN_BY_AW
    if mode is 'distribution':
        return {'A_WIN_E_BY_AW' : A_WIN_E_BY_AW/l_sum, 'A_WIN_S_BY_AW' : A_WIN_S_BY_AW/l_sum, 'A_WIN_W_BY_AW' : A_WIN_W_BY_AW/l_sum, 'A_WIN_N_BY_AW' : A_WIN_N_BY_AW/l_sum, 'A_WIN_BY_AW' : A_WIN_BY_AW/l_sum}

    return(A_WIN_E_BY_AW/l_sum * 1850 + A_WIN_S_BY_AW/l_sum * 1935 + A_WIN_W_BY_AW/l_sum * 1954.5 + A_WIN_N_BY_AW/l_sum * 1964.5 + A_WIN_BY_AW/l_sum * 1974.5 )


