import os
import sys
from pathlib import Path

from my_module.functions import *
from my_module.test_functions import *

from datetime import date 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


def main():

    # Get file:
    file_name = 'study_data.csv' 
    data = get_file(file_name) 
    assert test_get_file

    # Get demographics:
    genders,result = get_demographics(data)
    assert test_get_demographics
    
    fig = go.Figure(data=[go.Table(header=dict(values=['Gender', 'Total Participants']),
                                 cells=dict(values=[genders, result]))])

    fig.update_layout(width=500, height=300)
    fig.update_layout(title="Study Demographics by Gender")

    fig.show()

    # calculate_age:
    group1,group2 = calculate_age(pd.DataFrame(data, columns=['participant_id','gender','birth_date'])) 
    assert test_calculate_age

    # Get gender by group:
    get_gender_by_group(group1,'Children 4 to 7','pink')    
    get_gender_by_group(group2,'Children 8 to 11','blue') 

    assert test_get_gender_by_group


    
if __name__ == "__main__":
    main()