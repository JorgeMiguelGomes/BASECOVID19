# Import relevant libraries 

import numpy as np
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

#print(data[["signingDateParsed", "created", "updated"]].head())

## Fixing COntracting dictionary

f = pd.DataFrame.from_dict(data['contracting'][0])
dummy = f.copy(deep=True)
dummy['nif'] = np.nan
dummy['id'] = np.nan
dummy['description'] = np.nan

for i in range(1, len(data)):
    try:
        fprime = pd.DataFrame.from_dict(data['contracting'][i])
    except:
        fprime = dummy.copy(deep=True)
        
    f = pd.concat([f, fprime])
    
## Reset index for later merge
f = f.reset_index(drop=True)

## Rename columns to clarify names
f = f.rename(columns={'nif':'contracting_nif', 'description':'contracting_description', 'id':'contracting_id'})

## Fix contrated dictionary
g = pd.DataFrame.from_dict(data['contracted'][0])

for i in range(1, len(data)):
    try:
        ## Allocate only the first name where the contracted have issues
        gprime = pd.DataFrame.from_dict(data['contracted'][i]).iloc[0, :].to_frame().T
    except:
        gprime = dummy.copy(deep=True)
            
    ## Add fixed row to contrated
    g = pd.concat([g, gprime])
    

g = g.reset_index(drop=True)
g = g.rename(columns={'nif':'contracted_nif', 'description':'contracted_description', 'id':'contracted_id'})

## Merge Contractants and Contracted
contracts = f.merge(g, left_index=True, right_index=True)

## Add previously curated columns
contracts['publicationDate'] = data['publicationDate']
contracts['signingDateParsed'] = data['signingDateParsed']
contracts['price'] = data['price']
contracts['created'] = data['created']
contracts['updated'] = data['updated']

print(contracts.head())
