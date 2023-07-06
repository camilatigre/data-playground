import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_marvel_chars = '/kaggle/input/marvel-characters/Marvel Characters.csv'

df = pd.read_csv(data_marvel_chars)


# Calculate the count of each gender category
gender_counts = df['gender'].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Gender Distribution')

# Calculate the number of female and male characters
num_female = gender_counts['female']
num_male = gender_counts['male']

# Add the phrase with real data
phrase = "Looking at this chart and knowing 137 characters from Marvel and some of their genders, \nwe can affirm that for each {} males characters we have {} female character".format(num_male, num_female)
print(phrase)

# Display the pie chart
plt.show()
