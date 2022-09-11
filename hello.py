import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model

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

money_happiness_df.plot(kind='scatter', x='GDP', y='Happiness',color='blue')
#
# plt.show()

X = np.array(money_happiness_df['GDP']).reshape(-1,1)
y = money_happiness_df['Happiness']

linear_regression_model = sklearn.linear_model.LinearRegression()
linear_regression_model.fit(X, y)

prediction_y = linear_regression_model.predict(X)

plt.scatter(X, y,  color='blue')
plt.plot(X,prediction_y, color='red')
plt.show()

argentina_gdp = [[13588.84]]
print(linear_regression_model.predict(argentina_gdp))
