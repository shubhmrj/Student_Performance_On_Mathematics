import sys

from dataclasses import dataclass
import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformation()
        
    def get_data_transformer_object(self):
        '''
        This function si responsible for data transformation
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]  
            
            numerical_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="most_frequent")),
                    ('scaler',StandardScaler())
                ]
            ) 
            
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frquent")),
                    ('one_hot_encoder',OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )  
            
            preprocessor = ColumnTransformer(
                [
                    ('numerical_pipeline',numerical_pipeline,numerical_columns),
                    ("categorical_pipelines",categorical_pipeline,categorical_columns)
                    
                ]
            ) 
            
            return preprocessor      
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        
        try:
            pass
        
        except:
            pass