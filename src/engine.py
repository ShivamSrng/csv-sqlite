import os
import sqlite3
import pandas as pd
from time import time
from src.database.create_table import CreateTable
from src.database.retrieve_data import RetrieveData

class Engine:
  """
  It is responsible for serializing the execution of the program
  """


  def __init__(self, 
               db_configurations: dict) -> None:
    
    self.db_configurations = db_configurations
    
    try:
      os.remove(self.db_configurations["database"])
    except FileNotFoundError:
      pass


  def __create_database_connection(self) -> sqlite3.Connection:
    """
    It is responsible for creating the database connection
    
    Args:
      None
    
    Returns:
      sqlite3.Connection: provides the connection to the database
    """
    
    database = self.db_configurations["database"]
    return sqlite3.connect(database)
  

  def run(self) -> dict:
    """
    It is responsible for serializing the execution of the program
    
    Args:
      None
    
    Returns:
      response (dict): provides the response of the program at any stage
    """
    
    start = time()
    db_connection = self.__create_database_connection()
    
    table_creation_response = CreateTable(connection=db_connection).execute()
    if table_creation_response["status"] == "error":
      db_connection.close()
      return table_creation_response

    applicant_dataframe = pd.read_csv("data/applicant.csv")
    applicant_dataframe.to_sql("APPLICANT", db_connection, if_exists="replace", index=False)
    end = time()
    print(f"Data fetched from CSV and stored in the database in {end - start} seconds")
    print("\n")
    print("Retrieving data from the database")
    retrieval_response = RetrieveData(connection=db_connection).execute()
    if retrieval_response["status"] == "error":
      db_connection.close()
      return retrieval_response
    
    db_connection.close()
    return retrieval_response
    