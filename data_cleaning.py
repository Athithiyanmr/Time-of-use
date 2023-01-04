# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# %%
data = pd.read_excel("HOURLY DEMAND -  2021.xlsx",header=1)

# %%
data.drop("STATION                    TIME",axis =1, inplace =True)

# %%
data = data.T

# %%
a = data.columns.to_list()

# %%
jan_2021=pd.DataFrame(data.values.ravel('F'))

# %%
jan_2021.loc[48]
