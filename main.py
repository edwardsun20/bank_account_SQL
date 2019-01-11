import psycopg2 as pg2
from pprint import pprint

class DatabaseConnection:

#connect to database. user is postgres
    try:
        conn = pg2.connect(database='consumer_complaints', user='oracle', password = 'welcome1')
        conn.autocommit = True
        #cursor allows us to read/modify database
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE complaints(
            complaint_id text PRIMARY KEY,
            date text,
            product text,
            sub-product text,
            issue text,
            sub-issue text,
            consumer-complaint-narrative text,
            company-public response text,
            company text,
            state text,
            ZIP text,
            tags text,
            consent text,
            submitted text,
            date-sent text,
            company-response text,
            timely-response text,
            disputed text)
        """)

    except:
        pprint("Cannot connect to database")

    def select(self):
        self.cursor.execute('SELECT * FROM consumer_complaints')

    def create_table(self):
        create_table_command = "CREATE TABLE complaints(complaint_id text PRIMARY KEY)"
        self.cursor.execute(create_table_command)

if __name__  == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()