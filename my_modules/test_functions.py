"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

def test_get_file():
    assert isinstance(file_name,str)
    assert os.path.exists(file_name)

    return None
    
def test_get_demographics(data):
    result = data.groupby("gender")["participant_id"].count().dropna() 
    genders = ['Female','Male']
    colors = ['orange','lightblue']

    fig = go.Figure(data=[go.Table(header=dict(values=['Gender', 'Total Participants']),
                                   cells=dict(values=[genders, result]))])

    fig.update_layout(width=500, height=300)
    fig.update_layout(title="Study Demographics by Gender")

    fig.show()
    
def test_calculate_age():
    assert callable(calculate_age)
    assert isinstance(data,pd.DataFrame)
    assert isinstance(calculate_age(data),tuple)
    assert all(isinstance(m,list) for m in calculate_age(data))

def test_get_gender_by_group():
    assert callable(get_gender_by_group)
    
    #get_gender_by_group(group,title,color):
    #assert isinstance(data,pd.DataFrame)
    #assert isinstance(calculate_age(data),tuple)
    #assert all(isinstance(m,list) for m in calculate_age(data))


         
