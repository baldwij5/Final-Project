
### Summary

This process uses spatial joins, field calculators, and seaborn visualizations
to better understand per capita wildfire burdens utilizing geogaphical 
heirarchies as scoping levels. NASA MODIS satellite data was used as 
fire observation inputs and catalogued according to US Census shapefiles.

### Input Data

'fire_archive_V1_116683.csv': csv containing all recorded wildfire observations 
by the NASA MODIS satellite  from January 1, 2010 through December 31, 2019. 

'tl_2019_us_state (1).zip': Zipfile containing US TIGER/LINE shapefile for 
each state in the United States of America.

'tl_2019_us_county.zip': Zipfile containing US TIGER/LINE shapefile for 
each county in the United States of America.

'tl_2019_06_bg.zip':Zipfile containing US TIGER/LINE shapefile for 
each state in the California.

'ca_pop.json': JSON file containing the total population of California - ACS 
2018

'ca_county_pop.json': JSON file containing the total population of each 
county in California - ACS 2018

'ca_tracts_pop.json': JSON file containing the total population of each 
census tract in California - ACS 2018

'siskiyou_bg_pop.json': JSON file containing the total population of each 
block group in Siskiyou county - ACS 2018

'la_bg_pop.json': JSON file containing the total population of each 
block group in Los Angeles county - ACS 2018

'state_qgis_input.csvt': csv template file to instruct QGIS in accepting 
relevant QGIS input csvs

'county_qgis_input.csvt':csv template file to instruct QGIS in accepting 
relevant QGIS input csvs

'tract_qgis_input.csvt':csv template file to instruct QGIS in accepting 
relevant QGIS input csvs

'sky_bg_qgis_input.csvt':csv template file to instruct QGIS in accepting 
relevant QGIS input csvs

'la_bg_qgis_input.csvt':csv template file to instruct QGIS in accepting 
relevant QGIS input csvs

### Deliverables

By the end of the analysis, we will be able to determine the fires-per-capita 
for each of the chosen geographical heirarchies: the state of California,
each California County, each California census tract, Los Angeles county
census block groups, and Siskiyou county census block groups. We will also
produce a series of descriptive graphs showing the distribution of 
fires-per-capita for for each geographical heirarchy and the top 10 areas
of fires-per-capita within each heirarchy. Comparison graphs between 
fires-per-capita and population density for each geographical heirarchy will
be produced. Finally, we will produce an interactive map containing all of the 
relevant calculations and comparisons as a visualization tool.  

### Instructions

**California_Fire_Recieve_and_Clean.py**

1. Import: pandas, geopandas, csv, zipfile, and Zipfile from zipfile

2. Build function analyze_csv() to analyze csv input

3. Use analyze_csv() to read in the fire data as a data frame and save into 
the 'Working Data' directory

4. Name the block goup zipfile and print the directory. 

5. use geopandas to read the 'bg' file and index the resulting geodataframe 
on the 'GEOID' column

6. Use geopandas to create a new geodataframe that converts the 'x' and 'y'
columns to geometric points. Save ths dataframe in an object called 'gdf'

7. Perform a spatial join on 'bg' and 'gdf' as a geopandas merge. The join
sould be inner and intersetcs. Call the resulting object 'cali_merged'.

8. Reset the index for 'cali_merged' and rename the column 'level_0' as 'BGCE'.
This is to create a new block group geoid later.

9. For each of the geographic heirarchies, calculate the frequecies of fires
by using the value_count() method on each individual identifier column. 
Then convert them to pandas data frames, reset indexes, and label the value 
counts as each heirarchy's fire counts.


10. For each of the geographical heirarchies, import the JSON Census data,
reset the header to appropriate columns, rename releant column as 'pop', 
and create a 'geoid' column populated by aggregated columns from each
identifier. Save these dataframes in the 'Working Data' directory.

11. For each of the geographical heirarchies, merge the frequency data frame
and the population datframe on each appropriate column indicator. 

12. Trim each merged dataframe to include only 'NAME', 'pop', 
'state_fire_counts', and 'geoid' columns. 

13. Finally, save each dataframe to the 'Working Data' directory. 

**QGIS Steps**

1. Load zipfile containing US states and filter down to California: 'STATEFP' = '06'
Export the result as a geodatabase, reproject to ESPG: 32610, and export as a 
geodatabase again. 

2. Load zipfile containing US counties and filter down to California: 'STATEFP' = '06'
Export the result as a geodatabase, reproject to ESPG: 32610, and export as a 
geodatabase again.

3. Load zipfile containing US census tracts and filter down to California: 'STATEFP' = '06'
Export the result as a geodatabase, reproject to ESPG: 32610, and export as a 
geodatabase again.

4. Load the zipfile containing US census block groups for California and filter down 
to Los Angeles county: 'COUNTYFP' = '307'.Reproject to ESPG: 32610, and export
as a geodatabase. Repeat this process for Siskiyou county: 'COUNTYFP' = '093'.

5. Load the qgis input files produced by **California_Fire_Recieve_and_Clean.py**
as csv files. 

6. Perform a join for each appropriate shapefile and table on the "GEOID" and
"geoid" column respectively. 

7. Once joined, and for each shapefile, open the attribute table and open the 
field calculator. Create a new output field, set 'Output Field Name' 
to 'pop_density', set the Output Field Type to "Decimal number (real)", 
and in the expression field, and calculate the population density by dividing
the 'pop' field by the 'ALAND' field. 

8. Next, use the field calculator again to create a new output field, 
set 'Output Field Name' to 'fires_per_capita', set the Output Field Type to 
"Decimal number (real)", and in the expression field, and calculate the 
fire-per-capita rate by dividing the fire count field by the 'pop' field.

9. Complete steps 7 and 8 for each geographical heirarchy

10. Export the final attribute tables to csv in the 'QGIS Output' directory.


**California_Fire_Analsis.py**

1. Import: pandas, seaborn, and matplotlib.pyplot 

2. Load each calculations sheet and store tham as appropriate objects: state, 
counties, tracts, la_bg, and sky_bg

3. Use the .dropna() method on each object to limit the analysis to only areas 
that experienced fire

4. Use matplotlib to create a boxen plot for each 'fires_per_capita' column 
of each geographical heirarchy

5. Use matplotlib to create a hex plot comparing 'fires_per_capita' and
'pop_density' of each geographical heirarchy

6. Trim each of the geographical heirarchy data frames to only include the
'county_final_NAME', 'GEOID', 'fires_per_capita' columns. Use the sort_values()
method on the 'fires_per_capita' column, save the top 10 recorded heirarchies,
and save to the 'Final Data' directory.

7. Finally, provide some summary statistics for each geographical heirarchy.

### Tips

+ 'csvt' files are provided in the 'Working Data' file in anticipation
of loading csv files into QGIS. 

+ QGIS output files are provided by the author in order to streamline analysis.
**QGIS Steps** can be followed and will produce all relevant files. 

+ 'ca_fires.qgz' is provided as an interactive vizualization of the data

+ 'jic' directory is provided as a just in case scenario id any other files are deleted













