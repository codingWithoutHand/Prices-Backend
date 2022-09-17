import numpy as np
import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('oil.csv')

df.head()