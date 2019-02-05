
# coding: utf-8

# In[7]:


def miles_to_km(miles):
    km = miles * 1.60934
    print(km, "km")
    
m = input('Please enter miles: ')
m = float(m)
miles_to_km(m)
