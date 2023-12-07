import pandas as pd
import pickle
import streamlit as st

import numpy as np
import json
from sklearn.preprocessing import StandardScaler

    
# Define a new function
def custom_transform(new_data, X_train, scaler):
    """
    Transform new data using the same encoding and scaling as the training data.

    Parameters/Inputs:
    - new_data: DataFrame containing the new data to be transformed.

    Returns:
    - scaled_new: Transformed and scaled DataFrame ready for model prediction.

    Example:
    transformed_data = custom_transform(new_data)
    """
    # List of the encoded columns
    cat_col = ["region", "type", "laundry_options", "parking_options", "state"]
    
    for col in cat_col:
        
        # Use get_dummies on the new data
        encoded_new = pd.get_dummies(new_data[col], prefix=col, dtype=int)

    # Align columns in encoded_new to match columns in encoded_original
    encoded_new = encoded_new.reindex(columns=X_train.columns, fill_value=0)

    # Add other columns from new_data to encoded_new
    for col in new_data.columns:
        if col not in cat_col:
            encoded_new[col] = new_data[col]
            
            
    # Scaling the encoded new data
    scaled_new = scaler.transform(encoded_new)

    
    return scaled_new