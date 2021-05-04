# Import relevant libraries 

import pandas as pd # to deal with the dataset 
import plotly.express as px #to plot with beauty 
import json


data = pd.read_json('https://base-covid19.pt/export3.json', orient='index')

print(data.head())
