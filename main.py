from src.engine import Engine
from consts import SQLiteDBConsts


if __name__ == "__main__":
  db_configurations = SQLiteDBConsts().get_database_configurations()
  engine = Engine(
    db_configurations=db_configurations
  )
  response = engine.run()
  if response["status"] == "error":
    print(response)