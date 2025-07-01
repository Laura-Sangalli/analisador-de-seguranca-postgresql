import psycopg

class LoginMonitor:
    def __init__(self, host, dbname, user, password, port=5432):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
    
    def connect(self):
        try:
            self.conn = psycopg.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f"[!] Connection failed: {e}")