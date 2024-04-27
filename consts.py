import configparser


class SQLiteDBConsts:
  """
  SQLite database constants
  """


  def __init__(self) -> None:
    self.config_parser = configparser.ConfigParser()
    self.config_parser.read("config.ini")
  

  def get_database_configurations(self) -> dict:
    """
    Provides the database configurations
    
    Args:
      None
    
    Returns:
      dict: provides the necessary database configurations
    """
    
    database_configurations = self.config_parser["APPLICANTDB"]
    return database_configurations