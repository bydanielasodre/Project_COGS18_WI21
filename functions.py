"""A collection of function for doing my project."""
from datetime import date 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def get_file(file_name):
    """faz alguma coisa
    :param file_name: int
    :param data: dataframe
    """
    data = pd.read_csv(file_name)

    return data 


def get_demographics(data):
    result = data.groupby("gender")["participant_id"].count().dropna() 
    genders = ['Female','Male']
    colors = ['orange','lightblue']

    return result,genders
    
#https://plotly.com/python/table/




# It's only showing on my draft_one
# Error here, it's not allowing me to get today's date, when inside functions.p
# Write a text code and parameters for these variables


    
def calculate_age(data): 
   
    #error here, it's not allowing me to get today's date
    today = date.today() 

    ids = list(data['participant_id'])
    genders = list(data['gender'])
    dates = list(pd.to_datetime(data["birth_date"]))

    children_4to7 = []
    children_8to11 = []

    for i in range(len(ids)):
        current_age =  today.year - dates[i].year - ((today.month, today.day) < (dates[i].month, dates[i].day))

        if current_age <= 7:
            children_4to7.append((genders[i],current_age)) 
        elif 8 <= current_age <= 11:
            children_8to11.append((genders[i],current_age))
        else:
            continue
            
    return children_4to7,children_8to11




def get_gender_by_group(group,title,color):
   
    boys = 0
    girls = 0

    for kid in group:
        if kid[0] == 'M':
            boys += 1
        else:
            girls += 1
    
    gender = ['Boys', 'Girls']
    score = [boys,girls]
    
    plt.bar(gender, score, color = color)
    plt.ylabel('Total')
    plt.title(title)
    plt.show()
    
    return gender,score