import sqlite3
from src.database.db_utilities import DBUtilities


class CreateTable:
  """
  It is responsible for creating the tables in the database
  """


  def __init__(self, 
               connection: sqlite3.Connection) -> None:
    self.db_utilities = DBUtilities(
      connection=connection
    )
  

  def execute(self) -> None:
    """
    It is responsible for creating the table in the database
    
    Args:
      None
    
    Returns:
      None
    """
    
    try:
      query_to_create_table = (
        """
        CREATE TABLE IF NOT EXISTS APPLICANT (
          APPLICANTID INTEGER NOT NULL UNIQUE,
          APPLICATION_DATE VARCHAR(255),
          FIRST_NAME VARCHAR(255) NOT NULL,
          LAST_NAME VARCHAR(255),
          GENDER VARCHAR(255),
          DATE_OF_BIRTH DATE,
          EMAIL VARCHAR(255) NOT NULL,

          CONSTRAINT PEOPLE_PK 
          PRIMARY KEY (APPLICANTID)
        );
        """
      )
      return self.db_utilities.execute_query(
        query=query_to_create_table,
        description_about_query="Creating table 'APPLICANT'"
      )
    except sqlite3.Error as error:
      return {
        "status": "error",
        "error_code": error.args[0],
        "description": "Error while creating table",
        "query": query_to_create_table,
        "result": None
      }