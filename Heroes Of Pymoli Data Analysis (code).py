
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np


# In[81]:


file_to_load = "Resources/purchase_data.csv"
purchase_data = pd.read_csv(file_to_load)


# In[82]:


purchase_data.head()


# In[83]:


# data cleaning 
purchase_data = purchase_data.dropna(how='any')
purchase_data.count()


# In[84]:


# players summary
player_summary = purchase_data.loc[:, ["Gender", "SN", "Age"]]
player_summary.head()


# In[85]:


player_summary = player_summary.drop_duplicates()
num_players = player_summary.count()[0]
num_players


# In[86]:


# unique items
num_unique_items = len(purchase_data["Item ID"].unique())
# average purchase price
ave_purchase_price = round(purchase_data["Price"].mean())
# total number purchase
total_num_purchases = purchase_data["Item Name"].count()
# total revenue
total_revenue = purchase_data["Price"].sum()


# In[87]:


summary_df_player = pd.DataFrame({"Number of Unique Items":num_unique_items,
                           "Average Purchase Price":ave_purchase_price,
                           "Total Number of Purchases":total_num_purchases,
                           "Total Revenue":total_revenue},index = [0])


# In[88]:


summary_df_player


# In[89]:


# gender demographics
gender_demographics_totals = player_summary["Gender"].value_counts()
gender_demographics_percents = gender_demographics_totals / num_players * 100
gender_demographics = pd.DataFrame({"Total Count": gender_demographics_totals,
                                    "Percentage of Players": gender_demographics_percents})

gender_demographics


# In[96]:


# Basic Calculations
gender_purchase_total = purchase_data.groupby(["Gender"]).sum()["Price"].rename("Total Purchase Value")
gender_average = purchase_data.groupby(["Gender"]).mean()["Price"].rename("Average Purchase Value")
gender_counts = purchase_data.groupby(["Gender"]).count()["Price"].rename("Purchase Count")


# Create a summary data frame to hold the results
ave_total_puchase_person = gender_purchase_total / gender_demographics["Total Count"]

#data cleaner formatting
gender_data = pd.DataFrame({"Purchase Count": gender_counts, 
                            "Average Purchase Value": gender_average, 
                           " avg. purchase total per person": ave_total_puchase_person})

# Display the summary data frame
gender_data


# In[108]:


# Establish bins for ages
Ages_Bin = [0,10,15,20,25,30,35,40,100]
Ages_group = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
purchase_data['Age Ages_Bin'] = pd.cut(purchase_data['Age'],Ages_Bin,labels=Ages_group,right=False)

purchase_data_age_groupby = purchase_data.groupby(by='Age Ages_Bin')


#Use Cut to categorize players using the age bins. Hint: use pd.cut()
player_summary["Age Ranges"] = pd.cut(player_summary["Age"], Ages_Bin, labels=Ages_group)
player_summary.head()


# In[110]:


# Calculate the numbers and percentages by age group
age_demographics_totals = player_summary["Age Ranges"].value_counts()
age_demographics_percents = age_demographics_totals / num_players * 100

age_demographics = pd.DataFrame({"Total Count": age_demographics_totals, "Percent of Players": age_demographics_percents})
age_demographics = age_demographics.sort_index()

age_demographics


# In[111]:


# top spender
purchase_data_spender_groupby = purchase_data.groupby("SN")
total_purchase_value = purchase_data_spender_groupby["Price"].sum()
purchase_count = purchase_data_spender_groupby["Price"].count()
average_purchase_price = round(purchase_data_spender_groupby["Price"].mean(),2)


# In[114]:


display_df_spender = pd.DataFrame({"Purchase Count": purchase_count,
                                   "Average Purchase Price":average_purchase_price,
                                   "Total Purchase Value":total_purchase_value})
                  
                  
display_df_spender.sort_values(by = 'Total Purchase Value', ascending=False).head()


# In[125]:


# most popular 
purchase_data_popular_groupby = purchase_data.groupby(["Item ID", "Item Name"])
purchase_count = purchase_data_popular_groupby["Price"].count()
item_price = purchase_data_popular_groupby["Price"].mean()
total_purchase_price = purchase_data_popular_groupby["Price"].sum()

display_df_popular = pd.DataFrame({"Purchase Count":purchase_count,
                                    "Item Price": item_price,
                  
                                   "Total Purchase Price": total_purchase_price,
                  })
display_df_popular.sort_values(by="Purchase Count",ascending= False).head()


# In[128]:


# most profitable items
purchase_data_profitable_groupby = purchase_data.groupby(["Item ID", "Item Name"])
purchase_count = purchase_data_profitable_groupby["Price"].count()
item_price = purchase_data_profitable_groupby["Price"].mean()
total_purchase_price = purchase_data_profitable_groupby["Price"].sum()

display_df_profitable = pd.DataFrame({'Purchase Count':purchase_count,
                                      'Item Price': item_price,
                  
                                      'Total Purchase Price': total_purchase_price})
                  
display_df_profitable.sort_values(by="Total Purchase Price",ascending= False).head()

