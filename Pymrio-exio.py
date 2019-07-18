import pandas as pd
import os
import matplotlib.pyplot as plt
# import random
import glob
import numpy as np
# import glob
from numpy.linalg import inv
import zipfile
cwd = os.getcwd()
cwd
import pymrio
# atver atzipotu datu masību
exio3 = pymrio.parse_exiobase3(path=r'C:\tmp\mrios\exio3\2011')
exio3.calc_all()
# final deman vector
exio3.y = exio3.Y.groupby('region', as_index=False).agg("sum")
D_cba = exio3.satellite.M*exio3.y.T
