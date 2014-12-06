

import pyodbc

pyodbc.pooling=False

def test():

    ds_string = """DSN=PostgreSQL30;Database=maboss;UID=mabotech;PWD=mabouser"""

    conn = pyodbc.connect(ds_string)

    cursor = conn.cursor()

    x = cursor.execute("select now()")
    
    
    for i in x:
        print i
    cursor.close()
    del cursor
    conn.close()

def main():
    test()
    
    
if __name__ == "__main__":
    main()