#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  #for data cleaning

import plotly.express as ex  # use for data visualization
import plotly.graph_objects as go  #use for designing advance graphs
import plotly.io as pio  # use in graph templates
import plotly.colors as colors
pio.templates.default = 'plotly_white'  # setting template colour


# In[2]:


data = pd.read_csv('Sample - Superstore.csv', encoding = 'latin-1')  # imports all the data from our csv file


# In[3]:


data.head()  # this will show us only upto 5 datas


# In[4]:


data.describe()  # ek mota-moti andaza mil jata hai entire data ka 


# In[5]:


data.info()


# # Converting date columns

# In[6]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])


# In[7]:


data.info()


# In[8]:


data.head()


# In[9]:


data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek


# In[10]:


data.head()


# # **calculate monthly sales, which month has the highest sales, which month has the lowest sales** 

# In[11]:


monthly_sales = data.groupby('Order Month')['Sales'].sum().reset_index()


# In[12]:


monthly_sales


# In[13]:


fig = ex.line(monthly_sales,
             x = 'Order Month',  # Horizontal line
             y = 'Sales',  # Vertical Line
             title = 'Monthly Sales Analysis')


# In[14]:


fig.show()


# # **Sales based on product category, determine category wise lowest and highest sales**

# In[15]:


product = data.groupby('Category')['Sales'].sum().reset_index()


# In[16]:


product


# In[17]:


# fig2 = ex.pie(product,
#               'Category',
#               'Sales', 
#               title = 'Product category wise sales')


# In[18]:


fig2 = ex.pie(product,
            values = 'Sales',
            names = 'Category',
            hole = 0.5,
            color_discrete_sequence = ex.colors.qualitative.Pastel)

fig2.update_traces(textposition='inside', textinfo='percent+label')
fig2.update_layout(title_text = 'sales analysis by category', title_font = dict(size = 24))


# # **sales analysis based on Sub-Category**

# In[19]:


data.head()


# In[20]:


sales_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[21]:


sales_subcategory


# In[22]:


fig3 = ex.bar(sales_subcategory, 
             x = 'Sub-Category',
             y = 'Sales',
             title = 'sales analysis by sub category')


# In[23]:


fig3.show()


# # **analyze the monthly profit from sales, find the month which has the highest profit**

# In[24]:


sales_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()


# In[25]:


sales_by_month


# In[26]:


fig4 = ex.scatter(sales_by_month,
              'Order Month',
              'Profit',
              title = 'Monthly profit analysis')


# In[27]:


fig4.show()


# # **Analyze the profit by category and sub-category**

# In[28]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()


# In[29]:


profit_by_category


# In[50]:


fig5 = ex.pie(profit_by_category,
              'Category',
              'Profit',
              title = 'category wise profit')
# fig5.update_traces(textposition = 'inside', textinfo = 'percent+label')
# fig5.update_layout(title_text = 'profit by category', title_font = dict(size = 24))


# In[51]:


fig5.show()


# In[32]:


profit_by_Sub_category = data.groupby('Sub-Category')['Profit'].sum().reset_index()


# In[33]:


profit_by_Sub_category


# In[34]:


fig6 = ex.pie(profit_by_Sub_category,
              'Sub-Category',
              'Profit',
              title = 'category wise profit')


# In[35]:


fig6.show()


# # **Analysing sales and profit by customer segment, separate**

# In[36]:


data.head()


# In[37]:


sales_by_customer_segment = data.groupby('Segment')['Sales'].sum().reset_index()


# In[38]:


sales_by_customer_segment


# In[39]:


fig7 = ex.bar(sales_by_customer_segment,
                  x = 'Segment',
                  y = 'Sales',
              title = 'Segment wise Sales')


# In[40]:


fig7.show()


# In[41]:


Profit_by_customer_segment = data.groupby('Segment')['Profit'].sum().reset_index()


# In[42]:


Profit_by_customer_segment


# In[43]:


fig8 = ex.bar(Profit_by_customer_segment,
                  x = 'Segment',
                  y = 'Profit',
              title = 'Segment wise Profit')


# In[44]:


fig8.show()


# # **Analysing sales and profit by customer segment, combined**

# In[45]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                     y = sales_profit_by_segment['Sales'],
                     name = 'Sales',
                     marker_color = color_palette[0]))
fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                     y = sales_profit_by_segment['Profit'],
                     name = 'Profit',
                     marker_color = color_palette[1]))

fig.update_layout(title = 'Sales and Profit analysis by customer segment',
                  xaxis_title = 'Customer Segment',
                  yaxis_title = 'Amount')


# # **Sales to Profit Ratio**

# In[46]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']

print(sales_profit_by_segment[['Segment', 'Sales_to_Profit_ratio']])


# In[ ]:




