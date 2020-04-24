hierarchyhierarchy#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:41:21 2020

@author: jackbaldwin
"""

### Overview of Analysis

    The present analysis used population and geographical hierarchy data
from the US Census Bureau and NASA MODIA satellite data in an attempt to better
understand the amount of wildfires experienced by California residents across
the state. Aggregating data up to the state level is helpful for initial
analysis, but is difficult to understand at a granular level. For example,
the average per-capita amount of fire in California is about 0.01 from 2012 to
2019. This number may be accurate for some Californians, but is not true for
all residents. Better understanding where fires are occurring, how they have
(or have not) affected many communities, and how to respond to them are the
important questions to which the present analysis aims to contribute.

    This analysis is comparatively simple and attempts to open the door to better
understanding the current situation. Wildfire data was collected and joined to
geographical data provided by the US census. The results were then broken down
from the state level of per-capita fires to block groups in Siskiyou and Los
Angeles counties. These counties because they represented the highest and one
of the lowest frequency of fires respectively according to county level data
and were assumed to be illustrative of any results found. Descriptive statistics
and plots were made for the fires-per-capita calculations for each geographical
heirarchy. Furthermore, population density and fires-per-capita were compared
to better understand the relationship between the two variables.

### Descriptive Plots and Tables

    The average fires-per-capita in California was 0.01063.

    The first boxen plot shows the distribution of fires-per-capta for each county
in California. The mean value was 0.189190, standard deviation was 0.474316
with a distribution skewed to the right.

    The second boxen plot shows the distribution of fires-per-capta for each census
tract in California. the mean value was 0.488359, standard deviation was 3.889970
with a distribution highly skewed to the right. This graph shows that there
seem to be significant outliers pulling the fires-per-capita up in the census
tracts that had fires.

    The third boxen plot shows the distribution of fires-per-capta for each census
block group in Los Angeles county. the mean value was 0.801117, standard deviation was 9.990432
with a distribution highly skewed to the right. This graph shows that there
seem to be significant outliers pulling the fires-per-capita up in the census
block groups that had fires. The maximum of 165.300000 fires-per-capita is
extremely high, especially when related to the 75th percentile value of 0.008400.

    The fourth boxen plot shows the distribution of fires-per-capta for each census
block group in Siskiyou county. the mean value was 2.309490, standard deviation was 6.215589
with a distribution skewed to the right. This graph shows that there
seem to be definite outliers pulling the fires-per-capita up in the census
block groups that had fires. The distribution of this data is additionally
interesting because even though this county had the highest frequencies of fire
at a county level, many census block groups had less fires-per capita than the
state average

### Population Density Compared to Fires-per-Capita

    The first hex plot shows the relationship between population density and
fires-per-capita seems to be positive at the county level. Both distributions
are skewed to the right, which shows a large concentration of low
fires-per-capita and low population density. Large fires-per-capita outliers
seem to be present in low population density counties.

    The second hex plot shows the relationship between population density and
fires-per-capita seems to be positive at the census tract level. Both distributions
are skewed to the right, which shows a large concentration of low
fires-per-capita and low population density. The scale of the x-axis changed
dramatically when comparing counties and census tracts. This implies that a
large number of fires must be occurring in some census tracts with a low
population density.

    The third hex plot shows the relationship between population density and
fires-per-capita seems to be positive at the census block level in Los Angeles
county. Both distributions are skewed to the right, which shows a
large concentration of low fires-per-capita and low population density. The
scale of the x-axis resembles the census tracts graph more than the county
plot. This implies that a large number of fires must be occurring in some
census block groups with a low population density.

    The fourth hex plot shows the relationship between population density and
fires-per-capita seems to be positive at the census block level in Siskiyou
county. Both distributions are skewed to the right, which shows a
large concentration of low fires-per-capita and low population density. The
scale of the x-axis is much lower than the census block groups in Los Angeles
county. The scale of the y-axis was greatly reduced from the Los Angeles county
census block plot. This implies that Siskiyou county is, on average, less
densely populated than Los Angeles County.

### General Analysis

    A unifying theme across each examined variable was a right-skew of its
distribution. From this result, it is possible to see that as the geographical
heirarchy is reduced in area, serious disparities in fires-per-capita
begin to be made manifest. It is most obvious across Los Angeles census block
groups where a 165.300000 fires-per-capita statistic was encountered. Further
examination of this particular census block group shows that only four
individuals live in this beachside census block group in southern Los Angeles.
It seems that surburban areas with (assumming) higher income individuals are
being affected by fires in counties that are highly urbanized. This position
should of course be followed-up with future research.

    Despite these outliers, it is also possible to see that fires are occuring
in areas with low population densities. Siskiyou county experienced the highest
number of fires in the observed time period, and, on average the county had a
relatively high average fires-per-capita statistic. However, a majority of
fires-per-capita occurred in areas that were not widely populated.

### Limitations and Future Research
    This analysis is limited to geographical heirarchies that experienced fires.
In order to avoid overplotting, all areas that did not have a single instance
of fire were omitted from the dataset. This is obviously a flaw in the data
that must be redressed in the future.

    Future analysis should be performed that looks into both physical and
social effects of fires. Physical terrain obviously plays a role in the start
and spread of fires and was not directly accounted for here. Human populations
are not spread evenly across areas, and though this analysis attempts to
mitigate that issue, more work can be done. Finally, certain types of people
may be affected by fires at disparate rates. This analysis treated human
beings actuarially and removed from the real threat of wildfire.
