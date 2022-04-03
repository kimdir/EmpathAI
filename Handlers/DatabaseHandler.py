import pandas as pd
import sqlalchemy as alc

class DatabaseHandler:
    def __init__(self):
        # TODO: Determine server credentials
        self.DSNFileName = "EmpathAI_ODBC"
        self.InitiateConnection()

    def InitiateConnection(self):
        self.engine = alc.create_engine("access+pyodbc://@" + self.DSNFileName)
        print("Successful connection to database...")

    def CloseConnection(self):
        self.engine.dispose()
        print("Successfully terminated database connection.")

    def SaveToDB(self,targetTable,dataToInsert):
        # Check for correct count of columns to data
        #columnCount = self.cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = " + targetTable)
        #if columnCount != len(dataToInsert.columns):
        #    print("Data size mismatch, cancelling save...")
        #    return

        # Copy data into table if counts match
        dataToInsert.to_sql(targetTable, con = self.engine, if_exists = 'append')
        print("Successfully saved dataframe to database!")

    def LoadFromDB(self):
        pass

    def debug(self):
        #print(self.cursor.execute("SELECT (*)"))
        pass

if __name__ == ("__main__"):
    DBHandler = DBHandler()
    DBHandler.InitiateConnection()
