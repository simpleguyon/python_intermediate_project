# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
def get_unique_matches_count():
    ipl_matches_array = np.genfromtxt(path, delimiter = ',',skip_header=1)
    matches = []
    for x in ipl_matches_array:
        matches.append(x[0])
        
        
    return len(set(matches))
get_unique_matches_count()


