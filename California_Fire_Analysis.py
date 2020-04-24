#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:41:47 2020

@author: jackbaldwin
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%
state = pd.read_csv('QGIS Output/ca_state_calculations.csv')
counties = pd.read_csv('QGIS Output/ca_counties_calculations.csv')
tracts = pd.read_csv('QGIS Output/ca_tracts_calculations.csv')
la_bg = pd.read_csv('QGIS Output/ca_la_bg_calculations.csv')
sky_bg = pd.read_csv('QGIS Output/ca_sky_bg_calculations.csv')

#%%
state = state.dropna(subset=['fire_per_capita'])
counties=counties.dropna(subset=['fires_per_capita'])
tracts=tracts.dropna(subset=['fires_per_capita'])
la_bg=la_bg.dropna(subset=['fires_per_capita'])
sky_bg=sky_bg.dropna(subset=['fires_per_capita'])

#%%
print(state['fire_per_capita'].describe())
print(counties['fires_per_capita'].describe())
print(tracts['fires_per_capita'].describe())
print(la_bg['fires_per_capita'].describe())
print(sky_bg['fires_per_capita'].describe())

#%%
plt.figure()
ax = sns.boxenplot(counties['fires_per_capita'],orient='h')
plt.savefig('Final Data/counties_fpc_boxen.png')

plt.figure()
ax = sns.boxenplot(tracts['fires_per_capita'],orient='h')
plt.savefig('Final Data/tracts_fpc_boxen.png')

plt.figure()
ax = sns.boxenplot(la_bg['fires_per_capita'],orient='h')
plt.savefig('Final Data/la_bg_fpc_boxen.png')

plt.figure()
ax = sns.boxenplot(sky_bg['fires_per_capita'],orient='h')
plt.savefig('Final Data/sky_bg_fpc_boxen.png')

#%%
plt.figure()
counties_fpc_pd = sns.jointplot('fires_per_capita', 'pop_density', data=counties,kind='hex')
plt.savefig('Final Data/counties_fpc_by_popdensity_hex.png')

plt.figure()
tracts_fpc_pd = sns.jointplot('fires_per_capita', 'pop_density', data=tracts,kind='hex')
plt.savefig('Final Data/tracts_fpc_by_popdensity_hex.png')

plt.figure()
la_bg_fpc_pd = sns.jointplot('fires_per_capita', 'pop_density', data=la_bg,kind='hex')
plt.savefig('Final Data/la_bg_fpc_by_popdensity_hex.png')

plt.figure()
sky_bg_fpc_pd = sns.jointplot('fires_per_capita', 'pop_density', data=sky_bg,kind='hex')
plt.savefig('Final Data/sky_bg_fpc_by_popdensity_hex.png')

#%%
state_trimmed = state[['NAME', 'GEOID', 'fire_per_capita']]
state_trimmed.to_csv('Final Data/ca_fires_per_capita.csv', index = False)
print(state_trimmed)

counties_trimmed = counties[['county_final_NAME', 'GEOID', 'fires_per_capita']]
counties_trimmed = counties_trimmed.sort_values(by=['fires_per_capita'], axis = 0, ascending = False)
counties_top_ten = counties_trimmed.head(10)
counties_top_ten.to_csv('Final Data/counties_top_ten.csv', index = False)
print(counties_top_ten)

tracts_trimmed = tracts[['tract_final_NAME', 'GEOID', 'fires_per_capita']]
tracts_trimmed = tracts_trimmed.sort_values(by=['fires_per_capita'], axis = 0, ascending = False)
tracts_top_ten = tracts_trimmed.head(10)
tracts_top_ten.to_csv('Final Data/tracts_top_ten.csv', index = False)
print(tracts_top_ten)

la_bg_trimmed = la_bg[['la_bg_final_NAME', 'GEOID', 'fires_per_capita']]
la_bg_trimmed = la_bg_trimmed.sort_values(by=['fires_per_capita'], axis = 0, ascending = False)
la_bg_top_ten = la_bg_trimmed.head(10)
la_bg_top_ten.to_csv('Final Data/la_bg_top_ten.csv', index = False)
print(la_bg_top_ten)

sky_bg_trimmed = sky_bg[['sky_bg_final_NAME', 'GEOID', 'fires_per_capita']]
sky_bg_trimmed = sky_bg_trimmed.sort_values(by=['fires_per_capita'], axis = 0, ascending = False)
sky_bg_top_ten = sky_bg_trimmed.head(10)
sky_bg_top_ten.to_csv('Final Data/sky_bg_top_ten.csv', index = False)
print(sky_bg_top_ten)










