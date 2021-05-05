# Import relevant libraries 

import pandas as pd # to deal with the dataset 
import plotly.express as px #to plot with beauty 

from download_file import download_file
import json


## Get around pandas freezing when opening the file
url_name = 'https://base-covid19.pt/export3.json'
output_file = 'export3.json'

download_file('https://base-covid19.pt/export3.json', output_file=output_file)

## Reads the json brute force
data = pd.read_json(output_file)


## Time columns inserted as dictionaries
col_names_to_time = ["signingDateParsed", "created", "updated"]

for col_name in col_names_to_time:
    data[col_name] = data[col_name].apply(pd.Series)
    data[col_name] = pd.to_datetime(data[col_name])
    
## Time columns with easy to interpret datetime
data["publicationDate"] = pd.to_datetime(data["publicationDate"])
data["signingDate"] = pd.to_datetime(data["signingDate"])


print(data[["updated", "contracting"]].head())

