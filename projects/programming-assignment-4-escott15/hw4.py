"""
DISCLAIMER:

"""








import sys
import pprint as _pprint
from pprint import pformat
from data import CountyDemographics 
from county_demographics import *
from build_data import get_data

_fulldataset = get_data()
result = []
filename = sys.argv[1] 
print(f"file name: {filename}")
print('fetching data...')
#function to convert string to float with error handling from lab 7 (Tested and Working
"""
The purpose of this function is to take the incoming parameter, which is a string, and then convert it to a float.
input type: string
output type: float
"""
def str_to_float(s: str) -> None | float:   #function to convert string to float with error handling from lab 7 (T)
    try:
        return float(s)
    except ValueError:
        return None

try:    
   fileobj = open(f"inputs/{filename}", 'r')
except IndexError as _ie: #_ie == indexerror
    print(_ie)
    exit('_ie')
except FileNotFoundError as _fnf: #_fnf == filenotfound(error)
    print(_fnf)
    exit('_fnf')

fetchedops = fileobj.readlines()
#Clean data to make it readable. organize so that data is in a way that is able to be interpreted. 
#input type: list[str]
#output type: list[list[str]]
def cleanops(_data : list[str] = fetchedops)-> list[list[str]]:
        newdata =[i.strip('\n') for i in _data]
        newdata = [i.split(':') for i in newdata]
        for i in range(len(newdata)):
            if len(newdata[i]) > 1:
                if "." in newdata[i][1]:
                     temp = newdata[i][1].split('.')
                     newdata[i][1] = temp[0]
                     newdata[i].extend(temp[1:])
            for j in range(len(newdata[i])):
                converted = str_to_float(newdata[i][j])
                if converted is not None:
                    newdata[i][j] = converted
        return newdata

fileobj.close()
_cleanops= cleanops()
_pprint.pprint(_cleanops, indent=4)
print('data fetched and cleaned successfully.')
print('beginning processing...')

#functions from programming assignment 3, modified for programming assignment 4 (TESTED AND WORKING)

# part 1
"""
To get the population total of all the country demographics throughout 
the whole dataset
input type: list[Data.CountyDemographics]
output type: int
"""
def population_totals(lst:list[dict[CountyDemographics]] = _fulldataset) -> int:
    population_totals = 0 
    for county in lst:
        population_totals += county.population.get('2014 Population', 0)
    print(population_totals)
#part 2
"""
The purpose of this function is to filter the data by state
input type: list[Data.CountyDemographics], str
Output type: list[Data.CountyDemographics]
"""

def filter_by_state(state:str, lst:list[CountyDemographics] = _fulldataset )->list[CountyDemographics]:
    new_list = []
    for i in range(len(lst)):
        j, v = list[i].state 
    return new_list

#part 3
#population_by_education
"""
The purpose of this function is to get the population of each county by the education
input type: list[Data.CountyDemographics]
output type: float 
"""

def population_by_education(e:str, lst:list[CountyDemographics] = _fulldataset )->float:
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
def population_by_ethnicity(e:str, lst:list[CountyDemographics] = _fulldataset)->float:
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
def population_by_poverty_level(lst:list[CountyDemographics] = _fulldataset)->float:
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
def percent_by_education(e:str, lst:list[CountyDemographics] = _fulldataset )->float:
   total_pop = population_totals(lst)   #gets total population
   edu_pop = population_by_education(lst, e)    #gets educated population
   if total_pop == 0.0:
       return total_pop
   return float(edu_pop/total_pop)
#percent_by_ethnicity
"""
this function gets the percent of the ethnicity of the counties in the list relative to the total population, depending 
on what the user inputs
input type: list[data.CountyDemographics], string
output type: float
"""
def percent_by_ethnicity(e:str, lst:list[CountyDemographics] = _fulldataset )->float:
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
def percent_below_poverty_level(lst:list[CountyDemographics] = _fulldataset)->float:
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
def education_greater_than( e:str, num:float, lst:list[CountyDemographics] = _fulldataset)->list[CountyDemographics]:
    result = []
    for county in lst:
        if county.education[e] > num:
            result.append(county)
    return result
def education_less_than( e:str, num:float, lst:list[CountyDemographics] = _fulldataset)->list[CountyDemographics]:
    result = []
    for county in lst:
        if county.education[e] < num:
            result.append(county)
    return result
#ethnicity_greater_thane:str
"""
The purpose of this function is to find and return all of the counties in a list if the input ethnicity and the input 
percent is greater than the given percent value. 
input type: list[data.CountyDemographics], string, float
output type: list[data.CountyDemographics]
"""
def ethnicity_greater_than( e:str, num:float, lst:list[CountyDemographics] = _fulldataset)->list[CountyDemographics]:
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
def ethnicity_less_than( e:str, num:float, lst:list[CountyDemographics] = _fulldataset)->list[CountyDemographics]:
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
def below_poverty_level_greater_than( num:float, lst:list[CountyDemographics] = _fulldataset)->list[CountyDemographics]:
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
def below_poverty_level_less_than( num:float, lst:list[CountyDemographics] = _fulldataset)->list[CountyDemographics]:
    result = []
    for county in lst:
        if county.income.get('Persons Below Poverty Level', 0) < num:
            result.append(county)
    return result
#end of functions from programming assignment (TESTED AND WORKING)
#process data based on the type of operation specified in the input file.    / MAIN PROCESSING
_invalid = "Invalid paramter, please check .ops file"
_parameters = CountyDemographics.filter_paramters()
_displayflag = False
"""
The purpose of this funciton is to process the operation lines and do what it is asking
input type: no input 
output type: no direct output (resut.append())
"""
def process_ops()-> None:
    global _displayflag
    global _invalid
    global _parameters
    for i in range(len(_cleanops)):  
        op = _cleanops[i]
        if op[0] == "filter-state":
            if op[1] in CountyDemographics.states(): #stored list of all the possible abbreviations 
                temp = f"\nFiltered state: {op[1]} result: {filter_by_state(op[1])}"
                result.append(temp)
            else:       # arguments dont meet parameters
                print(_invalid)
                break 
        elif op[0] == "filter-gt":       #filter greater than
            if _cleanops[i][1] == _parameters[0]:     #education 
                temp = f"\nEducation filtered greater than %{op[2]}. ({op[3]}) Results: {education_greater_than(op[3], op[2])}"
                result.append(temp)
            elif _cleanops[i][1] == _parameters[1]:   #Ethnicities 
                temp = f"\nEthnicities filtered greater than %{op[2]}. ({op[3]}) Results: {ethnicity_greater_than(op[3], op[2])}"
                result.append(temp)
            elif _cleanops[i][1] == _parameters[2]:   #BelowPovertyLevel
                temp = f"\nBelow poverty poverty filtered greater than %{op[2]}. Results: {below_poverty_level_greater_than(op[2])}"
                result.append(temp)
            else:       # arguments dont meet parameters
                print(_invalid) 
                break
        elif op[0] == "filter-lt":      #filter less than 
            if op[1] == _parameters[0]:     #Education
                temp = f"\nEducation filtered less than %{op[2]}. ({op[3]}) Results: {education_less_than(op[3], op[2])}"
                result.append(temp)
            elif op[1] == _parameters[1]:   #Ethnicities
                temp = f"\nEthnicities filtered less than %{op[2]}. ({op[3]}) Results: {ethnicity_less_than(op[3], op[2])}"
                result.append(temp)
            elif op[1] == _parameters[2]:   #Belowpovertylevel
                temp = F"\nBelow poverty level filtered less than %{op[2]}, Results: {below_poverty_level_less_than(op[2])}"
                result.append(temp)
            else:       # arguments dont meet parameters
                print(_invalid)
                break
        elif op[0] == "display":        #display
            print(result)
            _displayflag = True 
        elif op[0] == "population-total":
            temp = f"\nPopulation total: {population_totals()}"
            result.append(temp)
        elif op[0] == "percent":        #percent of population by ()
            if _cleanops[i][1] == _parameters[0]:       #education
                temp = f"Percent of Population by {op[2]}. Results: {percent_by_education(op[2])}"
                result.append(temp)
            elif op[1] == _parameters[1]:       #Ethnicities 
                temp = f"\nPercent of population by {op[2]}. Results: {percent_by_ethnicity(op[2])}"
                result.append(percent_by_ethnicity(op[2]))
            elif op[1] == _parameters[2]:       #Belowpovertylevel
                temp = f"\nPercent of population by{op[2]}. Results: {population_by_poverty_level()}"
                result.append(temp)
            else:       # arguments dont meet parameters
                print(_invalid)
                break
        elif op[0] == "population": # population by ()
            if op[1] == _parameters[0]:       #education
                temp = f"\nPopulation by {op[2]}. Results: {population_by_education(op[2])}"
                result.append(temp)
            elif op[1] == _parameters[1]:     #Ethniciites
                temp = f"\nPopulation by {op[2]}. Results: {population_by_ethnicity(op[2])}"
                result.append(temp)
            elif op[1] == _parameters[2]:     #belowpovertylevel(income)
                temp = f"\nPopulation below poverty level. Results: {population_by_poverty_level()}"
                result.append(temp)
            else:   # arguments dont meet parameters
                print(_invalid)
                break
        else:      # arguments dont meet parameters
            print(_invalid)
            break
process_ops()

if _displayflag == False: 
    print(result)


    """
   
    """