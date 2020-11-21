# Let us start by importing the required libraries and our data-set:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Importing our data-set
file_path = "weatherHistory.csv"
file = pd.read_csv(file_path)
# file.head()
# print(file)


# Now we need to drop the unwanted data, convert the data in to our need and resample our data :
titles_req = ["Formatted Date", "Apparent Temperature (C)", "Humidity"]
df = file[titles_req]

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df_1 = df.set_index('Formatted Date')
df_1 = df_1.resample('MS').mean()

# Here is how the data looks after resampling:
# df_1.head()
# print(df_1)

# Now let us plot our data in a line graph
plt.figure(figsize=(14,6))
plt.title("variation in Apparent Trmperature and Humidity with time")
plt.plot(df_1)


# As we can see, both the peaks and the troughs are almost same throughout the period of 10 years. Here is a plot of the average temperature and humidity of the month of April over 10 years.
df_april = df_1[df_1.index.month==4]

plt.figure(figsize=(14,6))
plt.plot(df_april)

# We can clearly see that there is a sharp rise in temperature in the year of 2009 whereas there is a fall in temperature in the year of 2015. Hence we can conclude that global warming has caused an uncertainty in temperature over the past 10 years while the average humidity as remained constant throughout the 10 years.