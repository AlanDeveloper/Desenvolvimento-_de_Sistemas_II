import psycopg2

class serverDao():
    def connect(self): 
        banco = "dbname=DOIDAO user=postgres password=123456 host=localhost port=5432"
        return psycopg2.connect(banco)
