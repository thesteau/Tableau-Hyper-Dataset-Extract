# Tableau-Hyper-Dataset-Extract

Converts Tableau's .hyper dataset file into a .csv file.
Please note: You must use the exact path.

## Prerequisites
```
Python 3.7 or later
Pandas 1.2.3
Pantab 1.0.1
```

## Getting Started

After you have the required packages installed, simply run the script on the same directory as the .hyper file.

However, you may run this script for the specific method as shown below.

```python
import HyperConvert as hc

hyper = tableau_data_path.hyper  # The exact path of the original file with the .hyper extension
dest = destination_path.csv      # The destination path for the file with the .csv extension

hc.hyper_to_csv(hyper, dest)
```
