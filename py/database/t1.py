from contextlib import contextmanager
import pyodbc
import sys

@contextmanager
def open_db_connection(connection_string, commit=False):
    
    connection = pyodbc.connect(connection_string)
    
    cursor = connection.cursor()
    
    try:
        yield cursor
    except pyodbc.DatabaseError as err:
        error, = err.args
        sys.stderr.write(error.message)
        cursor.execute("ROLLBACK")
        raise err
    else:
        if commit:
            cursor.execute("COMMIT")
        else:
            cursor.execute("ROLLBACK")
    finally:
        connection.close()
        
ds_string = """DSN=PostgreSQL30;Database=maboss;UID=mabotech;PWD=mabouser"""

with open_db_connection(ds_string) as cursor:  
    
    x = cursor.execute("select now()")
    
    
    for i in x:
        print i    