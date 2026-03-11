class CountyDemographics:
    # Initialize a new CountyDemographics object.
    # input: the county's age demographics data as a dictionary
    # input: the county's name as a string
    # input: the county's education demographics data as a dictionary
    # input: the county's ethnicities demographics data as a dictionary
    # input: the county's income demographics data as a dictionary
    # input: the county's population demographics data as a dictionary
    # input: the county's state as a string
    def __init__(self,
                  age: dict[str,float],
                  county: str,
                  education: dict[str,float],
                  ethnicities: dict[str,float],
                  income: dict[str,float],
                  population: dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state
    def __repr__(self):
        return (f"county: {self.county},\n {self.state},\b {self.age},\n {self.education},\n {self.income},\n {self.population},\n {self.ethnicities}")


    # Provide a developer-friendly string representation of the object.
    # input: CountyDemographics for which a string representation is desired. 
    # output: string representation
    #def __repr__(self):
       
    def states():
        state_abbr = [
            "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
            "DC"
        ]
        return state_abbr
    def filter_paramters():
        _parameters = [ 'Education', 'Ethnicities', 'Persons Below Poverty Level','Income']
        return _parameters 
    
    def __str__(self):
        return f"{self.County}, {self.State}\nEducation: {self.Education}\nIncome: {self.Income}\n"
   
            
