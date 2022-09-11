from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from turtle import *
from tkinter import *

money_data_frame = pd.read_csv("money.csv") 
money_data_frame.head()

print(money_data_frame.head())

happiness_data_frame = pd.read_csv("happiness.csv") 
print(happiness_data_frame.head())

#Next, lets merge the two data frames (money and happiness)
money_happiness_df = pd.merge(happiness_data_frame, money_data_frame, 
                              on='Country', how='inner')
money_happiness_df.head(10)


money_happiness_df['GDP'] = money_happiness_df['GDP'].apply(float)

money_happiness_df.plot(kind='scatter', x='GDP', y='Happiness',color='red')
plt.show()