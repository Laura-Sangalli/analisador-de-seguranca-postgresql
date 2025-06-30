import psycopg

class InsertDeleteMonitor:
    def __init__(self, host, dbname, user, password, port=5432):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.conn = None
        self.cur = None

    def Plot_Inserts(self):
        pass

    def PlotDeletes(self):
        pass                 