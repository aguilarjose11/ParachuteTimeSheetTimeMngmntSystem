import pyodbc

'''
    This is the class in charge of connecting to the parachute MSSQL SERVER.
    Methods:
     * Connectdb(): Connectdb
        - constructor makes connection with the MSSQL server
     * getcursor(): pyodbc.cursor
     * authenticate(user: String, psw: String): bool
     * reconnect(): void
     * getpersonalinfo(): (string)
     * updatepersonalinfo(info: (String))
     * newuser(info: [string]): bool
     * deluser(user: string, psw: string): bool
     * deldata(): void
     * close(): void

    Variables:
     * exec
     * connectionString
'''
class Connectdb():

    '''
        Constructor connects to the db
    '''
    def __init__(self):
        self.connectionstring = "Driver={SQL Server};Server=tcp:parachute.database.windows.net,1433;Database=ParachuteDB;Uid=parachute@parachute;Pwd=P@r@chute;Encrypt=yes;TrustServerCertificate=no;"
        try:
            self.exec = pyodbc.connect(self.connectionstring)
        # only if error in connection string.
        except pyodbc.InterfaceError:
            print("Error with SQL Connection String. Go to github repo to learn more.")
            exit(1)
        # only if no internet.
        except pyodbc.OperationalError:
            print("No internet. Connection failed.")
            exit(1)
        # succesfull connection.
        self.cursor = self.exec.cursor()

    def getcursor(self):
        return self.cursor

    def authenticate(self, user, psw):
        sql = "SELECT * FROM parachute WHERE Usr=? AND Psw=?"
        result = self.cursor.execute(sql, user, psw)
        return (len(result) == 1)

    def reconnect(self):
        self.exec = pyodbc.connect(self.connectionstring)
        self.cursor = self.exec.cursor()

    def getpersonalinfo(self):
        pass

    def updatepersonalinfo(self, info = []):
        pass
    '''
        Shall create a new user based on the info provided by the list.
        The list follows this format:
        - [Department, last name, first name, username, password]
    '''
    def newuser(self, info = []):
        def nextid(self):
            self.reconnect()
            sql = "SELECT MAX(ID) FROM parachute"
            val = self.cursor.execute(sql).fetchall()[0][0]
            self.close()
            if val is None:
                return 0
            else:
                return val + 1

        if(len(info) != 0):
            self.reconnect()
            sql = "INSERT INTO parachute (?, ?, ?, ?, ?, ?);"
            self.cursor.execute(sql, info[0], info[1], info[2], info[3], info[4], nextid())
            sql ="""
                CREATE TABLE ? (
                    Din time,
                    Dout time,
                    TTime float,
                    Desc VARCHAR(225),
                    ID int
                )
            """
            self.cursor.execute(sql, info[3])
            self.cursor.commit()
            self.close()

    def deluser(self, user, psw):
        pass

    def deldata(self):
        pass

    def close(self):
        exec.close()
