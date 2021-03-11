# Tableau-Hyper-Dataset-Extract

Requires:
Python 3.7 or later
Pandas 1.2.3
Pantab 1.0.1

Converts a hyper data file into csv through python.

Please note: You must use the exact path.

To use this package as a module:

import HyperConvert as hc

hyper = tableau_data_path.hyper
dest = destination_path.csv

hc.hyper_to_csv(hyper, dest)
