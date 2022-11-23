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

# %% [markdown]
# ### Importing Finalized dataset

# %%
data = pd.read_excel("Tou_input.xlsx")

# %%
data.columns

# %% [markdown]
# ### Creating timestamp column(for the year 2021)

# %%
data["timestamp"]=pd.date_range(start='2021-01-01 00:00', periods = 8760,freq ="1h")

# %%
data['Date'] = pd.to_datetime(data['timestamp']).dt.date
data['Time'] = pd.to_datetime(data['timestamp']).dt.time
data['Month'] = pd.to_datetime(data['timestamp']).dt.month

# %%

# %%

# %%
data["Net_load"] = data["Total_energy_load"] - data["Solar_load"] - data["Wind_load"]

# %%
data["Others"] = data["Total_energy_load"] - data["Domestic"] - data["Industrial"] -data["Commercial"] - data["Agriculture"]

# %%

# %%
new_order = ["timestamp","Date","Time","Month","Total_energy_load","Solar_load","Wind_load","Net_load","Domestic","Industrial","Commercial","Agriculture","Others"]
data = data.reindex(new_order, axis=1)

# %%
data

# %%

# %%
plt.plot(data["timestamp"],data["Total_energy_load"],color ="black",label ="Total_Load")
plt.stackplot(data["timestamp"],data["Domestic"], data["Industrial"], data["Commercial"],data["Agriculture"],data["Others"],
              colors =['yellow', 'green','skyblue','orange','red'],alpha =0.5)

plt.plot(data["timestamp"],data["Wind_load"],'--'  ,color ="navy",label ="Wind_load")
plt.plot(data["timestamp"],data["Solar_load"],'--',color ="red",label ="Solar_load")
plt.plot([], [], color ='yellow',
         label ='Domestic')
plt.plot([], [], color ='green',
         label ='Industrial')
plt.plot([], [], color ='skyblue',
         label ='Commercial')
plt.plot([], [], color ='orange',
         label ='Agriculture')
plt.plot([], [], color ='red',
         label ='Others')

plt.ylim(0,20000)
# plt.xlim(data['Timestamp'][0],data['Timestamp'][23])
plt.title("overall")
plt.rcParams['figure.figsize'] = [18, 6]
plt.xlabel("Hour")
plt.ylabel("Load (MW)")
plt.tight_layout()
plt.legend(loc="best")
plt.style.use("ggplot")
# plt.savefig("new",dpi=1500)
plt.show()

# %%
data.set_index("timestamp",inplace =True)

# %%
jan15 = data["2021-01-15 00:00:00 ": "2021-01-15 23:00:00"]

# %%
jan15

# %%
jan15.reset_index(inplace = True)

# %%
# pd.plotting.deregister_matplotlib_converters()

# %%
plt.plot(jan15["timestamp"],jan15["Total_energy_load"],color ="black",label ="Total_Load")
plt.stackplot(jan15["timestamp"],jan15["Domestic"], jan15["Industrial"], jan15["Commercial"],jan15["Agriculture"],jan15["Others"],
              colors =['yellow', 'green','skyblue','orange','red'],alpha =0.5)

plt.plot(jan15["timestamp"],jan15["Wind_load"],'--'  ,color ="navy",label ="Wind_load")
plt.plot(jan15["timestamp"],jan15["Solar_load"],'--',color ="red",label ="Solar_load")
plt.plot([], [], color ='yellow',
         label ='Domestic')
plt.plot([], [], color ='green',
         label ='Industrial')
plt.plot([], [], color ='skyblue',
         label ='Commercial')
plt.plot([], [], color ='orange',
         label ='Agriculture')
plt.plot([], [], color ='red',
         label ='Others')
plt.ylim(0,20000)
plt.xlim(jan15['timestamp'][0],jan15['timestamp'][23])
plt.title("Jan 15th")
plt.rcParams['figure.figsize'] = [18, 6]
plt.xlabel("Hour")
plt.ylabel("Load (MW)")
plt.tight_layout()
plt.legend(loc="best")
plt.style.use("ggplot")
# plt.savefig("new",dpi=1500)
plt.show()

# %%
# data.set_index("timestamp",inplace =True)

# %%
# January = data["2021-01-01 00:00:00 ": "2021-01-31 23:00:00"]

# %%
# January.reset_index(inplace = True)

# %%
# plt.plot(January["timestamp"],January["Total_energy_load"],color ="black",label ="Total_Load")
# plt.stackplot(January["timestamp"],January["Domestic"], January["Industrial"], January["Commercial"],January["Agriculture"],January["Others"],
#               colors =['yellow', 'green','skyblue','orange','red'],alpha =0.5)

# plt.plot(January["timestamp"],January["Wind_load"],'--'  ,color ="navy",label ="Wind_load")
# plt.plot(January["timestamp"],January["Solar_load"],'--',color ="red",label ="Solar_load")
# plt.plot([], [], color ='yellow',
#          label ='Domestic')
# plt.plot([], [], color ='green',
#          label ='Industrial')
# plt.plot([], [], color ='skyblue',
#          label ='Commercial')
# plt.plot([], [], color ='orange',
#          label ='Agriculture')
# plt.plot([], [], color ='red',
#          label ='Others')
# plt.ylim(0,20000)
# # plt.xlim(January['timestamp'][0],January['timestamp'][23])
# plt.title("Jan 15th")
# plt.rcParams['figure.figsize'] = [18, 6]
# plt.xlabel("Hour")
# plt.ylabel("Load (MW)")
# plt.tight_layout()
# plt.legend(loc="best")
# plt.style.use("ggplot")
# # plt.savefig("new",dpi=1500)
# plt.show()

# %%

# %%
data.columns

# %%
# df2 = data.loc[data.groupby(['timestamp', 'Month'])['Total_energy_load'].idxmax()]

# %%

# %%
data.reset_index(inplace = True)

# %%
data.groupby(["Month","Date"])["Total_energy_load"].max()

# %%
data.groupby(["Month"])["Total_energy_load"].agg(["min","max"])

# %%

# %%
# month = np.where(data["Month"]==1)

# %%

# %%
