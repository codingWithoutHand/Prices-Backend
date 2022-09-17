import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet

df = pd.read_csv("/Users/seungsukim/Desktop/Prices-Backend/sample.csv", engine= 'python', encoding='cp949')

model=Prophet()
model.fit(df)  

future=model.make_future_dataframe(periods=4,freq='w')
forecast=model.predict(future)

result=forecast[['기간','휘발유']]
result.tail()

new_file.to_csv("/Users/choiyun/Downloads/result.csv", index=False)