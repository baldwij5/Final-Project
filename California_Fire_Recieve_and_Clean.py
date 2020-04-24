#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:07:41 2020

@author: jackbaldwin
"""

import pandas as pd
import geopandas as gpd
import csv
import zipfile
from zipfile import ZipFile 
    
#%%
def analyze_csv(csv):
    df=pd.read_csv(csv)
    df=df.reset_index()
    return df

#%%
csv = 'Raw Data/fire_archive_V1_116683.csv'
df= analyze_csv(csv)
df.to_csv(r'Working Data/clean_fire_data.csv',index=False)
print(df.head())

#%%
zipname_bg = 'Raw Data/tl_2019_06_bg.zip'

with ZipFile(zipname_bg, 'r') as zip: 
    zip.printdir() 
    
#%%
with ZipFile(zipname_bg, 'r') as zipObj:
    zipObj.extractall('Working Data/bg_cali')
    
#%%
bg = gpd.read_file('Working Data/bg_cali', index_col='GEOID')
bg.set_index('GEOID', inplace = True)
print(bg.columns)
print(bg.head())

#%%
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

#%%
cali_merged = gpd.tools.sjoin(bg, 
                          gdf, 
                          how="inner",
                          op = 'intersects')

#%%
cali_merged.reset_index(inplace = True)
cali_merged = cali_merged.rename(columns = {'level_0':'BGCE'})

#%%
state_freq = cali_merged['STATEFP'].value_counts()
state_freq=pd.DataFrame(data = state_freq)
state_freq = state_freq.reset_index()
state_freq = state_freq.rename(columns = {'index':'STATEFP', "STATEFP":"state_fire_counts"})
print(state_freq)

#%%
county_freq = cali_merged['COUNTYFP'].value_counts()
county_freq=pd.DataFrame(data = county_freq)
county_freq = county_freq.reset_index()
county_freq = county_freq.rename(columns = {'index':'COUNTYFP', "COUNTYFP":"county_fire_counts"})
print(county_freq)

#%%
tract_freq = cali_merged['TRACTCE'].value_counts()
tract_freq=pd.DataFrame(data = tract_freq)
tract_freq = tract_freq.reset_index()
tract_freq = tract_freq.rename(columns = {'index':'TRACTCE', "TRACTCE":"tract_fire_counts"})
print(tract_freq)

#%%
bg_freq = cali_merged['BGCE'].value_counts()
bg_freq=pd.DataFrame(data = bg_freq)
bg_freq = bg_freq.reset_index()
bg_freq = bg_freq.rename(columns = {'index':'BGCE', "BGCE":"bg_fire_counts"})
print(bg_freq)

#%%
state_pop = pd.read_json(r'Raw Data/ca_pop.json')
state_pop_new_header = state_pop.iloc[0] 
state_pop = state_pop[1:] 
state_pop.columns = state_pop_new_header
state_pop = state_pop.rename(columns = {'B01001_001E':'pop'}) 
state_pop.to_csv('Working Data/ca_state_pop.csv',index=False)
print(state_pop)

#%%
county_pop = pd.read_json(r'Raw Data/ca_county_pop.json')
county_pop_new_header = county_pop.iloc[0] 
county_pop = county_pop[1:] 
county_pop.columns = county_pop_new_header
county_pop = county_pop.rename(columns = {'B01001_001E':'pop'})
county_pop['geoid']=county_pop.state+county_pop.county
print(county_pop)
county_pop.to_csv('Working Data/ca_county_pop.csv',index=False)

#%%
tract_pop = pd.read_json(r'Raw Data/ca_tracts_pop.json')
tract_pop_new_header = tract_pop.iloc[0] 
tract_pop = tract_pop[1:] 
tract_pop.columns = tract_pop_new_header
tract_pop = tract_pop.rename(columns = {'B01001_001E':'pop'})
tract_pop['geoid']=tract_pop.state+tract_pop.county+tract_pop.tract
print(tract_pop)
tract_pop.to_csv('Working Data/ca_tract_pop.csv',index=False)

#%%
sky_bg_pop = pd.read_json(r'Raw Data/siskiyou_bg_pop.json')
sky_bg_pop_new_header = sky_bg_pop.iloc[0] 
sky_bg_pop = sky_bg_pop[1:] 
sky_bg_pop.columns = sky_bg_pop_new_header
sky_bg_pop = sky_bg_pop.rename(columns = {'B01001_001E':'pop', 'block group':'bg'}) 
sky_bg_pop['geoid']=sky_bg_pop.state+sky_bg_pop.county+sky_bg_pop.tract+sky_bg_pop.bg
print(sky_bg_pop)
sky_bg_pop.to_csv('Working Data/sky_bg_pop.csv',index=False)

#%%
la_bg_pop = pd.read_json(r'Raw Data/la_bg_pop.json')
la_bg_pop_new_header = la_bg_pop.iloc[0] 
la_bg_pop = la_bg_pop[1:] 
la_bg_pop.columns = la_bg_pop_new_header
la_bg_pop = la_bg_pop.rename(columns = {'B01001_001E':'pop', 'block group':'bg'}) 
la_bg_pop['geoid']=la_bg_pop.state+la_bg_pop.county+la_bg_pop.tract+la_bg_pop.bg
print(la_bg_pop)
la_bg_pop.to_csv('Working Data/la_bg_pop.csv',index=False)

#%%
state_merged = state_pop.merge(state_freq
                , left_on='state'
                , right_on='STATEFP'
                , indicator = True
                , validate ="1:1" )

state_merged = state_merged.rename(columns = {'state':'geoid'}) 
print(state_merged)

#%%
county_merged = county_pop.merge(county_freq
                , left_on='county'
                , right_on='COUNTYFP'
                , indicator = True
                , validate ="1:1" )


print(county_merged)
print(county_merged.columns)

#%%
tract_merged = tract_pop.merge(tract_freq
                , left_on='tract'
                , right_on='TRACTCE'
                , indicator = True
                , validate ="m:1" )

print(tract_merged)
print(tract_merged.columns)

#%%
sky_bg_merged = sky_bg_pop.merge(bg_freq
                , left_on='geoid'
                , right_on='BGCE'
                , indicator = True
                , validate ="1:1" )

print(sky_bg_merged)
print(sky_bg_merged.columns)

#%%
la_bg_merged = la_bg_pop.merge(bg_freq
                , left_on='geoid'
                , right_on='BGCE'
                , indicator = True
                , validate ="1:1" )

print(la_bg_merged)
print(la_bg_merged.columns)

#%%
state_qgis_input = state_merged[['NAME', 'pop', 'state_fire_counts', 'geoid']]
print(state_qgis_input)

#%%
county_qgis_input = county_merged[['NAME', 'pop', 'county_fire_counts', 'geoid']]
print(county_qgis_input)

#%%
tract_qgis_input = tract_merged[['NAME', 'pop', 'tract_fire_counts', 'geoid']]
print(tract_qgis_input)

#%%
sky_bg_qgis_input = sky_bg_merged[['NAME', 'pop', 'bg_fire_counts', 'geoid']]
print(sky_bg_qgis_input)

#%%
la_bg_qgis_input = la_bg_merged[['NAME', 'pop', 'bg_fire_counts', 'geoid']]
print(la_bg_qgis_input)
print(la_bg_qgis_input['bg_fire_counts'])

#%%
state_qgis_input.to_csv('Working Data/state_qgis_input.csv', index = False)
county_qgis_input.to_csv('Working Data/county_qgis_input.csv', index = False)
tract_qgis_input.to_csv('Working Data/tract_qgis_input.csv', index = False)
sky_bg_qgis_input.to_csv('Working Data/sky_bg_qgis_input.csv', index = False)
la_bg_qgis_input.to_csv('Working Data/la_bg_qgis_input.csv', index = False)



