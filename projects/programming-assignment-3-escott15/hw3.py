import county_demographics
from county_demographics import *
import data

# part 1
"""
To get the population total of all the country demographics throughout 
the whole dataset
input type: list[Data.CountyDemographics]
output type: int
"""
def population_totals(lst:list[data.CountyDemographics])-> int:
    population_total = 0
    for county in lst:
        population_total += county.population.get('2014 Population', 0)
    return population_total

#part 2
"""
The purpose of this function is to filter the data by state
input type: list[Data.CountyDemographics], str
Output type: list[Data.CountyDemographics]
"""

def filter_by_state(lst:list[data.CountyDemographics], state:str)->list[data.CountyDemographics]:
    new_list = []
    for county in lst:
        if county.state == state:
            new_list.append(county)
    return new_list

#part 3
#population_by_education
"""
The purpose of this function is to get the population of each county by the education
input type: list[Data.CountyDemographics]
output type: float 
"""

def population_by_education(lst:list[data.CountyDemographics], e:str)->float:
    result = 0.0
    for county in lst:
        if e in county.education:
            temp = county.population.get('2014 Population', 0) #gets total population
            result += temp * county.education[e] #then multiplies it by the percent of education and sets it equal to result
    return result
#population_by_ethnicity
"""
the purpose of this function is to get the population of ethnicity of each county and add them all together. 
input type: list[Data.CountyDemographics]
output type: float 
"""
def population_by_ethnicity(lst:list[data.CountyDemographics], e:str)->float:
    result = 0.0
    for county in lst:
        if e in county.ethnicities:
            temp = county.population.get('2014 Population', 0)
            result += temp * county.ethnicities[e]
    return result
#population_by_poverty_level
"""
This function gets the total amount of population in the counties that are below poverty level
input type: list[Data.CountyDemographics]
output type: float
"""
def population_by_poverty_level(lst:list[data.CountyDemographics] )->float:
    result = 0.0
    for county in lst:
        temp = county.population.get('2014 Population', 0)
        result += county.income['Persons Below Poverty Level']*temp
    return result
#part 4
#percent_by_education
"""
this function gets the percent of the education of the counties in the list relative to the total population, depending
on what the user inputs
input type: list[data.CountyDemographics], string
output type: float
"""
def percent_by_education(lst:list[data.CountyDemographics], e:str)->float:
   total_pop = population_totals(lst)   #gets total population
   edu_pop = population_by_education(lst, e)    #gets educated population
   if total_pop == 0.0:
       return total_pop
   return float(edu_pop/total_pop)
#perecent_by_ethnicity
"""
this function gets the percent of the ethnicity of the counties in the list relative to the total population, depending 
on what the user inputs
input type: list[data.CountyDemographics], string
output type: float
"""
def percent_by_ethnicity(lst:list[data.CountyDemographics], e:str)->float:
    total_pop = population_totals(lst)
    ethn_pop = population_by_ethnicity(lst, e)
    if total_pop == 0.0:
        return total_pop
    return float(ethn_pop/total_pop)
#percent_below_poverty_level
"""
This function gets the percent of the below poverty level in the counties relative to the total population
input type: list[data.CountyDemographics]
output type: float
"""
def percent_below_poverty_level(lst:list[data.CountyDemographics])->float:
    total_pop = population_totals(lst)
    pov_pop = population_by_poverty_level(lst)
    if total_pop == 0.0:
        return total_pop
    return float(pov_pop/total_pop)
#part 5
#eduation_greater_than
#education_less_than
"""
the purpose of this function is to find all of the counties within a set list of counties if the input education and input
percent is less than or greater than and return them all in a new list Depending on which function you use. (less than or
greater than)
input type: list[data.CountyDemographics], string, float
output type: list[data.CountyDemographics]
"""
def education_greater_than(lst:list[data.CountyDemographics], e:str, num:float)->list[data.CountyDemographics]:
    result = []
    for county in lst:
        if county.education[e] > num:
            result.append(county)
    return result
def education_less_than(lst:list[data.CountyDemographics], e:str, num:float)->list[data.CountyDemographics]:
    result = []
    for county in lst:
        if county.education[e] < num:
            result.append(county)
    return result
#ethnicity_greater_than
"""
The purpose of this function is to find and return all of the counties in a list if the input ethnicity and the input 
percent is greater than the given percent value. 
input type: list[data.CountyDemographics], string, float
output type: list[data.CountyDemographics]
"""
def ethnicity_greater_than(lst:list[data.CountyDemographics], e:str, num:float)->list[data.CountyDemographics]:
    result = []
    for county in lst:
        if county.ethnicities[e] > num:
            result.append(county)
    return result
#ethnicity_less_than
"""
The purpose of this function is to find and return all of the counties in a list if input ethnicity and the input 
percent is less than the given percent value(float). 
input type: list[data.CountyDemographics], string, float
output type: list[data.CountyDemographics]
"""
def ethnicity_less_than(lst:list[data.CountyDemographics], e:str, num:float)->list[data.CountyDemographics]:
    result = []
    for county in lst:
        if county.ethnicities[e] < num:
            result.append(county)
    return result
#below_poverty_level_greater_than
"""
the purpose of this function is to find and return all of the counties in a list if input the county is greater than 
a certain percent which is given 
input type: list[data.CountyDemographics], string, float
output type: list[data.CountyDemographics]
"""
def below_poverty_level_greater_than(lst:list[data.CountyDemographics], num:float)->list[data.CountyDemographics]:
    result = []
    for county in lst:
        if county.income.get('Persons Below Poverty Level', 0) > num:
            result.append(county)
    return result
#below_poverty_level_less_than
"""
the purpose of this function is to find and return all of the counties in a list if input the county is less than 
a certain percent which is given 
input type: list[data.CountyDemographics], float
output type: list[data.CountyDemographics]
"""
def below_poverty_level_less_than(lst:list[data.CountyDemographics], num:float)->list[data.CountyDemographics]:
    result = []
    for county in lst:
        if county.income.get('Persons Below Poverty Level', 0) < num:
            result.append(county)
    return result

