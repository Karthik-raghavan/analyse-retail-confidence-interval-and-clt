# This is a custom library created for data analysis made for personal use

# importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy as db
import logging


class data_structure:
    """
    This class shall be used for obtaining the basic information on the structure of data.

    Written By: Karthikraghavan
    Version: 1.0
    Revisions: None
    """

    def __init__():
        pass

    def get_basic_info(data):
        
        """
        Function to get the following information on the datset

        Input : Dataframe
        Output: 

        shape of the data
        total number of missing values in total(not taking columns in consideration)
        categorical and numerical variables
        number of distinct / unique values in the columns
        the unique values in categorical variables
        data types of variables and info on the dataset

        """
        print()
        print(f'Data has {data.shape[0]} rows and {data.shape[1]} columns.')
        print()
        print(f'Data has {data.isnull().sum().sum()} null values in total.')
        print()
        print()
        print('Categorical Columns:')
        print()
        print(data.select_dtypes(include='O').columns.to_list())
        print()
        print()
        print('Numerical Columns:')
        print()
        print(data.select_dtypes(exclude='O').columns.to_list())
        print()
        print()
        print('Number of Unique Values in Columns:')
        print()
        for col in data.columns:
            print(f"{col}:{data[col].nunique()}")
        print()
        print()
        print('Unique Values in Categorical Columns:')
        print()
        for col in data.select_dtypes(include = 'O').columns:
            print(f"{col}:{data[col].unique()}")
        print()
        print()
        print(f'Information on Dataset:')
        print()
        data.info()
        print()

    
    def value_counts_of_categories(data):
        """
        Function to display the value counts of categorical variables

        Input : Dataframe
        Output : value counts 
        """
        for col in data.select_dtypes(include = 'O').columns:
            print(data[col].value_counts())
            print()    

    def descriptive_statistics(data):
        """
        Function to display Descriptive statistics on **Categories** and **Numerical** variables 
        """
        print()
        print('Descriptive statistics on Categories variables:')
        print()
        print(data.select_dtypes(include='O').describe())
        print()

        print()
        print("Descriptive statistics on Numerical variables:")
        print()
        print(data.select_dtypes(exclude='O').describe(percentiles = [0,0.05,0.25,0.50,0.75,0.95,1]))
        print()

class database_connect:
    """
    This class shall be used for working with database using sqlalchemy and pymysql.

    Written By: Karthikraghavan
    Version: 1.0
    Revisions: None
    """

    def __init__():
        pass

    def establish_connect(database_name):
        """
        Function to create a connection to database
        """
        return db.create_engine(f"mysql+pymysql://root:admin@localhost/{database_name}")
    
    def create_database_table(data_type, data,table_name,engine,if_exists,**table_query):
        """
        Function to create a database table, 
        we have to provide:
            connection_engine, 
            table_name, 
            if_exists
                
        based on the type of data, has different options
            data_type = 'file' or 'dataframe'
            
        if file is given, we have read the data and create the table
        if dataframe is given, we have to create a connection and then create a table by giving a query.
        """
        print(f"Table Creation in progress")
        if data_type == 'file':
            pd.read_csv(data).to_sql(table_name, con = engine, index=False, if_exists=if_exists)

            print(f"Table Creation Completed")

        elif data_type == 'dataframe':
            with engine.connect() as connection:
                print(f"Executing Query")

                #print(table_query)
                connection.execute(db.text(table_query["table_query"]))
                print(f"Query Complete, Table Created")

            print(f"Wrting data to {table_name} table")
            data.to_sql(table_name, con = engine, index=False, if_exists=if_exists)

        print()
        print(f'{table_name} Table is created and data is stored')
        print()

            
class visualize:


    def __init__():
        pass

    def a():
        #logging.basicConfig(filename='log_files/eemployee_in_log.log',level=10,format='%(asctime)s:%(levelname)s:%(message)s')
        pass