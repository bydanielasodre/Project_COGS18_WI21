"""A collection of function for doing my project."""

from datetime import date 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def get_file(file_name):
    """Reads a csv and convert it to a dataframe. 

    Parameters
    ----------
    file_name: string
        Name of the file containing the data.
        
    Returns
    -------
    data: dataframe
       The dataframe of all the information in the file. 
    
    """ 

    data = pd.read_csv(file_name) # Uses pandas' read_csv function to open the file and have it as dataframe

    return data 



def get_demographics(data):
    """Reads the dataframe and calculate the ammount of boys and girls and creates a plot. 

    Parameters
    ----------
    data : dataframe
        The dataframe of all the information in the file.   
    
    Returns
    ----------
    nothing
    """ 
    
    result = data.groupby("gender")["participant_id"].count().dropna() # Counts total of participants and group them by gender


    genders = ['Female','Male']
    colors = ['orange','lightblue']

    
    #https://plotly.com/python/table/
    return result,genders
    
    
def calculate_age(data): 
    """Reads the dataframe and calculate the age of the participants based on today's date, and separates by two age groups.

    Parameters
    ----------
    data : dataframe
        The dataframe of all the information in the file.   
    
    Returns
    ----------
    a tuple of children ages 4 to 7, and children age 8 to 11.
    """ 
    
    today = date.today() # Get today's date

    ids = list(data['participant_id']) # For the calculation, we use the participant's id, their genders and their birth dates


    genders = list(data['gender'])
    dates = list(pd.to_datetime(data["birth_date"])) # Convert to the same format as today

    children_4to7 = []
    children_8to11 = []

    # Iterate over each kid
    for i in range(len(ids)):
        current_age =  today.year - dates[i].year - ((today.month, today.day) < (dates[i].month, dates[i].day))
        
        # If kid belongs to group below 7, append to list:
        if current_age <= 7:
            children_4to7.append((genders[i],current_age)) 
        # If it's from the second group, append to second list:
        elif 8 <= current_age <= 11:
            children_8to11.append((genders[i],current_age))
        # If kid it's too old, do nothing.
        else:
            continue
            
    return children_4to7,children_8to11





def get_gender_by_group(group,title,color):
    """Reads the dataframe and separates participants by age groups and genders.

    Parameters
    ----------
    group : a list of tuples containing age and gender for an specific group.
    title : figure title.
    color : bar color.
    
    Returns
    ----------
    a tuple of children ages 4 to 7, and children age 8 to 11 and their respective gender. 
    """ 
    
    boys = 0
    girls = 0

    # Iterate over each kid from the group list of tuples
    for kid in group:
        # If the index from the tuple is equals to 'M', it's a boy
        if kid[0] == 'M':
            boys += 1
        # otherwise, it's a girl
        else:
            girls += 1
    
    gender = ['Boys', 'Girls']
    score = [boys,girls] # Score contains the sum of all boys and girls of the group
    
    # Plots the result
    plt.bar(gender, score, color = color)
    plt.ylabel('Total')
    plt.title(title)
    plt.show()
    
    return gender,score


# The End 

   
    

