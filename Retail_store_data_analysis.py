#!/usr/bin/env python
# coding: utf-8

# # Importing Necessary libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px  # use for data visualization
import plotly.graph_objects as go  #use for designing advance graphs
import plotly.io as pio  # use in graph templates
import plotly.colors as colors
pio.templates.default = 'plotly_white'  # setting template colour


# In[2]:


df = pd.read_csv('Orders.csv')
df2 = pd.read_csv('Details.csv')
df


# In[3]:


df2


# In[4]:


df.info()


# In[5]:


df['Order Date'].head(5)


# # Converting Dtype of Order date to datetime

# In[6]:


df['Order Date'] = pd.to_datetime(df['Order Date'], format = '%d-%m-%Y')
df.info()


# In[7]:


df['Order Date'].head(5)


# In[8]:


df


# In[9]:


# df['Order Date'] = pd.to_datetime(df['Order Date'], format = '%d %m %Y')


# In[10]:


# df


# In[11]:


df.info()


# In[12]:


# df = df.drop(['Day'], axis = 1)


# In[13]:


df


# In[14]:


df2


# In[15]:


# when we merge df order Id and df2's order id we'll get sales and profit sidewise 


# # merging df(Orders.csv) and df2(Details.csv)

# In[16]:


dfm = pd.merge(df2, df, on = 'Order ID', how = 'inner')


# In[17]:


dfm


# In[18]:


pd.set_option('display.max.rows', 1500)  #Display all rows


# In[19]:


dfm


# In[20]:


dfm.head(5)


# In[21]:


dfm.dtypes


# # Creating a dataframe that contains total_sales i.e, Amount * Quantity

# In[22]:


dfm['total_sales'] = dfm['Amount'] * dfm['Quantity']


# In[23]:


dfm.head()


# # Separating Month from date for future analysis

# In[24]:


dfm['Month'] = dfm['Order Date'].dt.month
dfm.head()


# # Total sales by month

# In[25]:


ts = dfm.groupby('Month')['total_sales'].sum().reset_index()


# In[26]:


ts.columns = ['Month', 'total_sales']


# In[27]:


# plt.xticks(ticks = range(1, 13))
# ts.plot(kind = 'line', title = 'Total Sales')
fig = px.line(ts,
            x = 'Month',
            y = 'total_sales',
            title = 'Total sales')
fig.update_layout(xaxis = dict(tickmode = 'linear',  #forces plotly to space ticks evenly
                               tick0 = 1,  #start ticks at 1(january)
                               dtick = 1))  #increment by 1, so it shows 1,2,3,4..12
#what is dict? A-> lengthy version to declare tickmode, tick0, dtick see below
# xaxis = {'tickmode' : 'linear',  #
#                                'tick0' : 1,
#                                'dtick' : 1} )
fig.show()


# # Total Profit by month

# In[28]:


tp = dfm.groupby('Month')['Profit'].sum().reset_index()


# In[29]:


tp.columns = ['Month', 'Profit']


# In[30]:


fig = px.bar(tp,
            x = 'Month',
            y = 'Profit',
            title = 'Total Profit')
fig.update_layout(xaxis = dict(tickmode = 'linear',
                               tick0 = 1, 
                               dtick = 1)) 
fig.show()


# In[31]:


# plt.xticks(ticks = range(1, 13))
# tp.plot(kind = 'line', title = 'Total Profit', grid = True)


# # Product sub-category contributing more sales

# In[32]:


dfm.head()


# In[33]:


scs = dfm.groupby('Sub-Category')['Profit'].sum().reset_index()   #group by sub-category and sum the profit


# In[34]:


scs.columns = ['Sub-Category','Profit']
# scs = scs.sort_values(ascending = False)  #sort from high to low


# In[35]:


fig = px.histogram(scs,
            x = 'Sub-Category',
            y = 'Profit', 
            title = 'Sub-category wise profit')
fig.update_layout(xaxis = dict(tickmode = 'linear',
                               tick0 = 1, 
                               dtick = 1)) 
fig.show()
# sorted_profit = sorted_profit.reset_index()  this will convert it to dataframe


# # States or cities bring in the most revenue

# In[36]:


dfm.head(3)


# In[37]:


sbr = dfm.groupby('State')['total_sales'].sum().reset_index()


# In[38]:


sbr.columns = ['State','total_sales']


# In[39]:


fig = px.line(sbr,
            x = 'State',
            y = 'total_sales', 
            title = 'State wise profit')
fig.update_layout(xaxis = dict(tickmode = 'linear',
                               tick0 = 1, 
                               dtick = 1)) 
fig.show()


# In[40]:


dfm.head()


# # Regional difference in product preference 

# In[41]:


rdpp = dfm.groupby(['State','Sub-Category']).size().reset_index(name = 'count')


# In[42]:


rdpp


# In[43]:


fig = px.line(rdpp,
            x = 'State',
            y = 'count',
            color = 'Sub-Category',
            title = 'Regional differences in product preference',
            # barmode = 'group'
             )
fig.update_layout(xaxis = dict(tickmode = 'linear',
                               tick0 = 1, 
                               dtick = 1)) 
fig.show()


# # Regional difference in payment methods

# In[44]:


rdpm = dfm.groupby(['State','PaymentMode']).size().reset_index(name = 'count')


# In[45]:


rdpm


# In[46]:


fig = px.line(rdpm,
            x = 'State',
            y = 'count',
            color = 'PaymentMode',
            title = 'Regional differences in payment methods',
            # barmode = 'group'
             )
fig.update_layout(xaxis = dict(tickmode = 'linear',
                               tick0 = 1, 
                               dtick = 1)) 
fig.show()


# In[47]:


dfm.head()


# # Cities with recent high quantity orders

# In[48]:


hqo = dfm[dfm['Order Date'] > '2018-08-31'].sort_values(by = ['Quantity', 'Order Date', 'City'], ascending = [False, False, False])


# In[49]:


hqo.groupby(['Order Date', 'City']).agg({'Quantity':'sum'}).reset_index()


# In[50]:


hqo = dfm[dfm['Order Date'] > '2018-08-31'].sort_values(by = ['Quantity', 'Order Date', 'City'], ascending = [False, False, False])
result = (hqo.groupby(['Order Date', 'City'])['Quantity'].sum().reset_index().sort_values(by = ['Quantity','Order Date'],
                                                                                         ascending = [False, False]))


# # Sorted the Order Quantity in Descending(high to low)

# In[51]:


result.head(20)


# In[52]:


fig = px.line(result,
            x = 'City',
            y = 'Quantity',
            color = 'Quantity',
            title = 'Recent high Quantities ordered',
            # barmode = 'group'
             )
fig.update_layout(xaxis = dict(tickmode = 'linear',
                               tick0 = 1, 
                               dtick = 1)) 
fig.show()


# # Most Popular and profitable Payment Mode

# In[53]:


dfm.head(3)


# In[54]:


dfm.dtypes


# In[55]:


dfm['PaymentMode'] = dfm['PaymentMode'].astype(str)


# In[56]:


mpp = dfm.groupby('PaymentMode')['Profit'].sum().reset_index()
mpp


# In[57]:


fig5 = px.pie(mpp,
              'PaymentMode',
              'Profit',
              title = 'most popular/profitable payment mode')
fig5.show()


# # Payment modes linked to High Profit and Loss

# In[58]:


pmp = mpp.loc[[mpp['Profit'].idxmax(), mpp['Profit'].idxmin()]]
fig = px.pie(pmp, 
            'PaymentMode',
            'Profit',
            title = 'Highest and Lowest profit payment modes')
fig.show()


# # High amount but Low profit

# In[59]:


hmlp = dfm[dfm['Profit'] < 0 ].sort_values(by = ['Profit','Amount'])
result = (hmlp.groupby('Amount')['Profit'].sum().reset_index().sort_values(by = ['Profit','Amount'], ascending = [True, False]))
rr = result.sort_values(by = ['Amount','Profit'], ascending = [False, False])
drr = rr.head(10)


# In[60]:


drr


# In[61]:


fig = px.line(drr,
              x = 'Amount',
              y = 'Profit',
              title = 'High amount but low profit')
fig.show()

