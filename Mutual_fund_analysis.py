#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


df = pd.read_excel('MFSC2.xlsx')


# In[ ]:


df.head()


# In[ ]:


df.drop(['Unnamed: 0'], axis = 1, inplace = True)


# In[ ]:


pd.set_option('display.max.rows', 1470)
pd.set_option('display.max.columns', 26)


# In[ ]:


df.head()


# # Title of columns contains special characters, here's how to remove that

# In[ ]:


# Python Automation
Columns_map = {'↓AUM': 'AUM','Absolute Returns - 1Y': 'Absolute Returns 1Y','Absolute Returns - 3M': 'Absolute Returns 3M',
'Absolute Returns - 6M': 'Absolute Returns 6M','% Largecap Holding': 'Largecap Holding','% Midcap Holding': 'Midcap Holding',
'% Smallcap Holding': 'Smallcap Holding','% Debt Holding': 'Debt Holding','% Equity Holding': 'Equity Holding'}

df.rename(columns = Columns_map, inplace = True)

df.head(2)


# In[ ]:


col = df.pop('CAGR 3Y')
df.insert(13, 'CAGR 3Y', col)  #CAGR


# # Here's how the Algorithm works
# 1. conver the column to string
# 2. set empty value to the special characters
# 3. set 0.00 to the empty values

# # Converting selected Columns to string

# In[ ]:


# Lengthy way to define

# df['AUM'] = df['AUM'].astype(str)
# df['Expense Ratio'] = df['Expense Ratio'].astype(str)
# df['Absolute Returns 1Y'] = df['Absolute Returns 1Y'].astype(str)
# df['Absolute Returns 3M'] = df['Absolute Returns 3M'].astype(str)
# df['Absolute Returns 6M'] = df['Absolute Returns 6M'].astype(str)
# df['Largecap Holding'] = df['Largecap Holding'].astype(str)
# df['Midcap Holding'] = df['Midcap Holding'].astype(str)
# df['Smallcap Holding'] = df['Smallcap Holding'].astype(str)
# df['Debt Holding'] = df['Debt Holding'].astype(str)
# df['Equity Holding'] = df['Equity Holding'].astype(str)
# df['CAGR 3Y'] = df['CAGR 3Y'].astype(str)
# df['CAGR 5Y'] = df['CAGR 5Y'].astype(str)
# df['CAGR 10Y'] = df['CAGR 10Y'].astype(str)
# df['Exit Load'] = df['Exit Load'].astype(str)
# df['PE Ratio'] = df['PE Ratio'].astype(str)
# df['NAV'] = df['NAV'].astype(str)
# df['Volatility'] = df['Volatility'].astype(str)
# df['Minimum SIP'] = df['Minimum SIP'].astype(str)

# making it simpler using python Automation
Columns_to_clean = ['AUM','Expense Ratio','Absolute Returns 1Y','Absolute Returns 3M','Absolute Returns 6M','Largecap Holding','Midcap Holding',
                    'Smallcap Holding','Debt Holding','Equity Holding','CAGR 3Y','CAGR 5Y','CAGR 10Y','Exit Load','PE Ratio','NAV','Volatility',
                    'Minimum SIP']

for col in Columns_to_clean:
    df[col] = df[col].astype(str)


# # Setting empty values to "-"

# In[ ]:


# making it simpler using python Automation
Columns_to_clean = ['AUM','Expense Ratio','Absolute Returns 1Y','Absolute Returns 3M','Absolute Returns 6M','Largecap Holding','Midcap Holding',
                    'Smallcap Holding','Debt Holding','Equity Holding','CAGR 3Y','CAGR 5Y','CAGR 10Y','Exit Load','PE Ratio','NAV','Volatility',
                    'Minimum SIP']
for col in Columns_to_clean:
    df[col] = df[col].astype(str).str.replace('-','',regex = False)


# # Converting columns back to numeric and assigning 0.00 to "-"

# In[ ]:


# making it simpler using python Automation
Columns_to_clean = ['AUM','Expense Ratio','Absolute Returns 1Y','Absolute Returns 3M','Absolute Returns 6M','Largecap Holding','Midcap Holding',
                    'Smallcap Holding','Debt Holding','Equity Holding','CAGR 3Y','CAGR 5Y','CAGR 10Y','Exit Load','PE Ratio','NAV','Volatility',
                    'Minimum SIP']
for col in Columns_to_clean:
    df[col] = pd.to_numeric(df[col]).fillna(0.00)


# In[ ]:


df.head(10)


# In[ ]:


df.dtypes


# # Small cap funds from the large dataset

# In[ ]:


scf = df[df['Sub Category'].str.contains('Small Cap Fund')]  #Small cap fund
scf


# # Mid cap fund from the large dataset

# In[ ]:


micf = df[df['Sub Category'].str.contains('Mid Cap Fund')]   #Mid cap fund
micf


# # large cap fund from the large dataset

# In[ ]:


lcf = df[df['Sub Category'].str.contains('Large Cap Fund')]   #large cap fund
lcf


# # multi cap fund from the large dataset

# In[ ]:


mcf = df[df['Sub Category'].str.contains('Multi Cap Fund')]   #Multi cap fund
mcf


# # Index fund from the large dataset

# In[ ]:


inf = df[df['Sub Category'].str.contains('Index Fund')]   #Index fund
inf


# # multi cap fund from the large dataset

# In[ ]:


fcf = df[df['Sub Category'].str.contains('Flexi Cap Fund')]   #Flexi cap fund
fcf


# # We'll majorly analyze 
# 1. Small cap fund
# 2. Multi cap fund
# 3. Flexi cap fund

# # Final Sorting Small cap Fund

# In[ ]:


data1 = scf[scf['CAGR 3Y'] > 20].sort_values(by = ['AUM','CAGR 3Y', 'CAGR 5Y', 'CAGR 10Y', 'Exit Load', 'PE Ratio'], ascending = [False, False, False, 
                                                                                                                                  False, True, True])
data1


# # Final Sorting Multi cap Fund

# In[ ]:


data2 = mcf[mcf['CAGR 3Y'] > 20].sort_values(by = ['AUM','CAGR 3Y', 'CAGR 5Y', 'CAGR 10Y', 'Exit Load', 'PE Ratio'], ascending = [False, False, False, 
                                                                                                                                  False, True, True])
data2


# # Final Sorting Flexi cap Fund

# In[ ]:


data3 = fcf[fcf['CAGR 3Y'] > 20].sort_values(by = ['AUM','CAGR 3Y', 'CAGR 5Y', 'CAGR 10Y', 'Exit Load', 'PE Ratio'], ascending = [False, False, False, 
                                                                                                                                  False, True, True])
data3


# In[ ]:


# data1.to_excel('small_cap_sorted_data.xlsx')


# In[ ]:


# data2.to_excel('multi_cap_sorted_data.xlsx')


# In[ ]:


# data3.to_excel('flexi_cap_sorted_data.xlsx')


# In[ ]:


get_ipython().system('jupyter nbconvert --to python Mutual_fund_analysis.ipynb')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




