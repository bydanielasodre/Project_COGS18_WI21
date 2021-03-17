"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

def test_get_file():
    assert isinstance(file_name,str)
    assert os.path.exists(file_name)
    
    return None
    
def test_get_demographics(data):
    assert callable(calculate_age)
    assert isinstance(data,pd.DataFrame)

    return None

def test_calculate_age():
    assert callable(calculate_age)
    assert isinstance(data,pd.DataFrame)
    assert isinstance(calculate_age(data),tuple)
    assert all(isinstance(m,list) for m in calculate_age(data))

    return None

def test_get_gender_by_group():
    assert callable(get_gender_by_group)
    assert isinstance(group,tuple)
    assert isinstance(title,str)
    assert isinstance(color,str)
         
    return None    
        

# The End



         
