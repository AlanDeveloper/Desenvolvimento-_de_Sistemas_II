import psycopg2

class serverDao():
    def connect(self): 
        banco = "dbname=DOIDAO user=postgres password=postgres host=localhost port=5432"
        return psycopg2.connect(banco)
