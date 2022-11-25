# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# ### Need to clean more

# %%
pd.plotting.register_matplotlib_converters()

# %%
#  pip install openpyxl

# %%
data = pd.read_excel("D:/TOU/220802 State load profile.xlsx",sheet_name=4)

# %%
data.columns


# %%
def data_details(df):
    return print(df.shape,df.info(),df.columns)


# %%
data_details(data)

# %%
data['Date'] = pd.to_datetime(data['timestamp']).dt.date
data['Time'] = pd.to_datetime(data['timestamp']).dt.time
data['Month'] = pd.to_datetime(data['timestamp']).dt.month

# %%
data.columns

# %%
data.columns = data.columns.str.strip()

# %%
data.columns

# %% [markdown]
# #### This import function is useful to analyse the data

# %%
# from pivottablejs import pivot_ui
# pivot_ui(data)


# %%
maximum = data["Total_energy_load"].max()

# %%
minimum = data["Total_energy_load"].min()

# %%
x = (maximum- minimum)/10

# %%
a= data[(data["Total_energy_load"] >= minimum) & (data["Total_energy_load"] <= minimum + x)] 
b= data[(data["Total_energy_load"] > minimum + x) & (data["Total_energy_load"] <= minimum +(2*x))]
c= data[(data["Total_energy_load"] > minimum +(2*x)) & (data["Total_energy_load"] <= minimum +(3*x))]
d = data[(data["Total_energy_load"] > minimum +(3*x)) & (data["Total_energy_load"] <= minimum +(4*x))]
e = data[(data["Total_energy_load"] > minimum +(4*x)) & (data["Total_energy_load"] <= minimum +(5*x))]
f = data[(data["Total_energy_load"] > minimum +(5*x)) & (data["Total_energy_load"] <= minimum +(6*x))]
g = data[(data["Total_energy_load"] > minimum +(6*x)) & (data["Total_energy_load"] <= minimum +(7*x))]
h = data[(data["Total_energy_load"]> minimum +(7*x) ) & (data["Total_energy_load"] <= minimum +(8*x))]
i = data[(data["Total_energy_load"] > minimum +(8*x)) & (data["Total_energy_load"] <= minimum +(9*x))]
j = data[(data["Total_energy_load"] > minimum +(9*x)) & (data["Total_energy_load"] <= maximum )]

# %% [markdown]
# ### Exporting the splitted values (excel format in a single workbook)

# %%
z =[a,b,c,d,e,f,g,h,i,j]
y =[]
for i in z:
    i = len(i)
    y.append(i)

# %%
y

# %%
count = pd.DataFrame()

# %%
count["no_of_points"] = y

# %%
count.plot(kind="bar")

# %%
# with pd.ExcelWriter('yearlydatasplit.xlsx') as writer:
#     a.to_excel(writer, sheet_name='yearly_1')
#     b.to_excel(writer, sheet_name='yearly_2')
#     c.to_excel(writer, sheet_name='yearly_2')
#     d.to_excel(writer, sheet_name='yearly_4')
#     e.to_excel(writer, sheet_name='yearly_5')
#     f.to_excel(writer, sheet_name='yearly_6')
#     g.to_excel(writer, sheet_name='yearly_7')
#     h.to_excel(writer, sheet_name='yearly_8')
#     i.to_excel(writer, sheet_name='yearly_9')
#     j.to_excel(writer, sheet_name='yearly_10')

# %% [markdown]
# ### Visualization of the Rolling mean over the 8760 values

# %%
data["Rolling_mean"] = data["Total_energy_load"].rolling(150).mean()

# %%
data.reset_index(inplace = True)

# %%
plt.plot(data["index"],data["Total_energy_load"],color ="#ee795d",label = "Total_energy_load")
plt.plot(data["index"],data["Rolling_mean"],color ="black",label ="Rolling_mean")
plt.ylim(6000,18000)
plt.xlim(0,8760)
# plt.xlim(1,23)
plt.rcParams['figure.figsize'] = [20, 6]
plt.xlabel("Hour")
plt.ylabel("Load (MW)")
# plt.legend(loc="best")
plt.style.use("ggplot")
# plt.savefig("new",dpi=1500)
plt.show()

# %% [markdown]
# #### resetting the index

# %%
data.set_index("timestamp",inplace =True)

# %% [markdown]
# ## Splitting the Data Based on Months Using Timestamp Data (Date range method)

# %% [markdown]
# #### Alternate menthod is also there where we create  a new column called Month like (data["month"] = data["timestamp"].dt.month)
#
# * data['month'] = data['timestamp'].dt.month

# %%
month1  = data["2021-07-28 00:00:00 ": "2021-08-31 23:00:00"]["Total_energy_load"]
month2  = data["2021-09-01 00:00:00 ": "2021-09-30 23:00:00"]["Total_energy_load"]
month3  = data["2021-10-01 00:00:00 ": "2021-10-31 23:00:00"]["Total_energy_load"]
month4  = data["2021-11-01 00:00:00 ": "2021-11-30 23:00:00"]["Total_energy_load"]
month5  = data["2021-12-01 00:00:00 ": "2021-12-31 23:00:00"]["Total_energy_load"]
month6  = data["2022-01-01 00:00:00 ": "2022-01-31 23:00:00"]["Total_energy_load"]
month7  = data["2022-02-01 00:00:00 ": "2022-02-28 23:00:00"]["Total_energy_load"]
month8  = data["2022-03-01 00:00:00 ": "2022-03-31 23:00:00"]["Total_energy_load"]
month9  = data["2022-04-01 00:00:00 ": "2022-04-30 23:00:00"]["Total_energy_load"]
month10 = data["2022-05-01 00:00:00 ": "2022-05-31 23:00:00"]["Total_energy_load"]
month11  = data["2022-06-01 00:00:00 ": "2022-06-30 23:00:00"]["Total_energy_load"]
month12  = data["2022-07-01 00:00:00 ": "2022-07-27 23:00:00"]["Total_energy_load"]


# %%
def creating_df(df):
    
    df= pd.DataFrame(df)
    df.reset_index(inplace =True) 
    df['Date'] = pd.to_datetime(df['timestamp']).dt.date
    df['Time'] = pd.to_datetime(df['timestamp']).dt.time
    return (df)


# %%
month1 = creating_df(month1)
month2 = creating_df(month2)
month3 = creating_df(month3)
month4 = creating_df(month4)
month5 = creating_df(month5)
month6 = creating_df(month6)
month7 = creating_df(month7)
month8 = creating_df(month8)
month9 = creating_df(month9)
month10 = creating_df(month10)
month11 = creating_df(month11)
month12 = creating_df(month12)

# %%

# %% [markdown]
# ### Exporting the splitted month data (excel format in a single workbook)

# %%
# with pd.ExcelWriter('monthwisedatasplit.xlsx') as writer:
#     month1.to_excel(writer, sheet_name='August')
#     month2.to_excel(writer, sheet_name='September')
#     month3.to_excel(writer, sheet_name='October')
#     month4.to_excel(writer, sheet_name='November')
#     month5.to_excel(writer, sheet_name='December')
#     month6.to_excel(writer, sheet_name='January')
#     month7.to_excel(writer, sheet_name='February')
#     month8.to_excel(writer, sheet_name='March')
#     month9.to_excel(writer, sheet_name='April')
#     month10.to_excel(writer, sheet_name='May')
#     month11.to_excel(writer, sheet_name='June')
#     month12.to_excel(writer, sheet_name='July')

# %% [markdown]
# ### Manipulating the Solar Data (for each month)

# %% [markdown]
# ### Need to change the column name

# %%
# January = pd.read_excel("Solar Load profiles from SAM/Solar load profile January.xlsx")
# February = pd.read_excel("Solar Load profiles from SAM/solar load profile Feb.xlsx")
# March = pd.read_excel("Solar Load profiles from SAM/Solar Load Profile march.xlsx")
# April = pd.read_excel("Solar Load profiles from SAM/Solar Load Profile April.xlsx")
# May = pd.read_excel("Solar Load profiles from SAM/Solar Load Profile May.xlsx")
# June = pd.read_excel("Solar Load profiles from SAM/Solar load profile June.xlsx")
# July = pd.read_excel("Solar Load profiles from SAM/Solar load profile July.xlsx")
# August = pd.read_excel("Solar Load profiles from SAM/Solar load profile August.xlsx")
# September = pd.read_excel("Solar Load profiles from SAM/Solar Load profile September.xlsx")
# October = pd.read_excel("Solar Load profiles from SAM/State load profile for october.xlsx")
# November = pd.read_excel("Solar Load profiles from SAM/State load profile november.xlsx")
# December = pd.read_excel("Solar Load profiles from SAM/State load profile December.xlsx")
# Annual = pd.read_excel("Solar Load profiles from SAM/State load profile Annual.xlsx")

# %%

# %%
# def data_manipulating(df,month_days):
#     lst_dict = []
#     for a in range(month_days):
#         lst_dict.append(df)
#     df = df.append(lst_dict,ignore_index = True)  
#     return (df)

# %%

# %%
# January =  data_manipulating(January,30)
# February =  data_manipulating(February,27)
# March =  data_manipulating(March,30)
# April =  data_manipulating(April,29)
# May =  data_manipulating(May,30)
# June =  data_manipulating(June,29)
# July =  data_manipulating(July,26)
# August =  data_manipulating(August,34)
# September =  data_manipulating(September,29)
# October =  data_manipulating(October,30)
# November =  data_manipulating(November,29)
# December =  data_manipulating(December,30)

# %%
# from datetime import datetime
# January["timestamp"]=pd.date_range(start='2022-01-01 00:00', periods = 744,freq ="1h")
# February["timestamp"]=pd.date_range(start='2022-02-01 00:00', periods = 672,freq ="1h")
# March["timestamp"]=pd.date_range(start='2022-03-01 00:00', periods = 744,freq ="1h")
# April["timestamp"]=pd.date_range(start='2022-04-01 00:00', periods = 720,freq ="1h")
# May["timestamp"]=pd.date_range(start='2022-05-01 00:00', periods = 744,freq ="1h")
# June["timestamp"]=pd.date_range(start='2022-06-01 00:00', periods = 720,freq ="1h")
# July["timestamp"]=pd.date_range(start='2022-07-01 00:00', periods = 648,freq ="1h")
# August["timestamp"]=pd.date_range(start='2021-07-28 00:00', periods = 840,freq ="1h")
# September["timestamp"]=pd.date_range(start='2021-09-01 00:00', periods = 720,freq ="1h")
# October["timestamp"]=pd.date_range(start='2021-10-01 00:00', periods = 744,freq ="1h")
# November["timestamp"]=pd.date_range(start='2021-11-01 00:00', periods = 720,freq ="1h")
# December["timestamp"]=pd.date_range(start='2021-12-01 00:00', periods = 744,freq ="1h")

# %% [markdown]
# ## Data manipulation is depends on the data (Solar and wind Load)

# %% [markdown]
# ### Below all are example codes

# %%
# January['Date'] = pd.to_datetime(January['Timestamp']).dt.date
# January['Time'] = pd.to_datetime(January['Timestamp']).dt.time
# January["Average energy load"] = data_january["Average energy load "]
# January["NetLoad"] = January["Average energy load"] - January["Hourly Data: System power generated (kW)"]

# %%

# %%

# %% [markdown]
# ## Data Visualization Code For reference

# %% [markdown]
# ####  Ref Colab Workbook (https://colab.research.google.com/drive/1vYzWSS7lwzPVq6TzsEpWXw1bQiI0GoLv#scrollTo=rzv8991MuJKB)

# %%
# plt.plot(jan15["Timestamp"],jan15["Average energy load "],color ="black",label ="Total_Load")
# plt.stackplot(jan15["Timestamp"],jan15["Domestic"], jan15["Industrial"], jan15["Commercial"],jan15["Agriculture"],jan15["Others"],
#               colors =['yellow', 'green','skyblue','orange','red'],alpha =0.5)

# plt.plot(jan15["Timestamp"],jan15["Windload"],'--'  ,color ="navy",label ="Wind_load")
# plt.plot(jan15["Timestamp"],jan15["solar_load"],'--',color ="red",label ="Solar_load")
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
# plt.xlim(jan15['Timestamp'][0],jan15['Timestamp'][23])
# plt.title("January 15th")
# plt.rcParams['figure.figsize'] = [18, 6]
# plt.xlabel("Hour")
# plt.ylabel("Load (MW)")
# plt.tight_layout()
# plt.legend(loc="best")
# plt.style.use("ggplot")
# # plt.savefig("new",dpi=1500)
# plt.show()

# %%
# plt.plot(yearly["Timestamp"],yearly["Average energy load "],color ="black",label ="Total_Load")
# plt.stackplot(yearly["Timestamp"],yearly["Domestic"], yearly["Industrial"], yearly["Commercial"],yearly["Agriculture"],yearly["Others"],
#               colors =['yellow', 'green','skyblue','orange','red'],alpha =0.5)

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
# plt.xlim(yearly['Timestamp'][0],yearly['Timestamp'][8759])
# # plt.title("April 15th")
# plt.rcParams['figure.figsize'] = [18, 6]
# plt.xlabel("Hour")
# plt.ylabel("Load (MW)")
# plt.tight_layout()
# plt.legend(loc="best")
# plt.style.use("ggplot")
# plt.savefig("new",dpi=1500)
# plt.show()

# %% [markdown]
# ## Monthly split by dt.month

# %% [markdown]
# ### Jan to Dec

# %%
January = data[data["Month"]== 1]
February = data[data["Month"]== 2]
March = data[data["Month"]== 3]
April = data[data["Month"]== 4]
May = data[data["Month"]== 5]
June = data[data["Month"]== 6]
July = data[data["Month"]== 7]
August = data[data["Month"]== 8]
September = data[data["Month"]== 9]
October = data[data["Month"]== 10]
November = data[data["Month"]== 11]
December = data[data["Month"]== 12]

# %%

# %%
