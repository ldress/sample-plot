import pandas as pd
import os

def load_data(data_path):
    # Get the absolute path to the data file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, '..', '..', data_path))
    
    # Load the data
    data = pd.read_csv(full_path)
    return data
