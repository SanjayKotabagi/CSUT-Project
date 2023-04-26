import mysql.connector
import re
import hashlib


class Log_Reg:
    login_status = False
    def __init__(self):

        self.__conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "users_db")
        
        self.__cursor = self.__conn.cursor()



    def register(self,uname,pwd,email_id):
        
        query = 'select * from users where username="'+uname+'";'
        self.__cursor.execute(query)
        user = self.__cursor.fetchall()

        if len(user)!=0:
           return "Username already exists"

        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
        # compiling regex
        pat = re.compile(reg)
        # searching regex                
        mat = re.search(pat, pwd)
        # validating conditions
        if not mat:
            return "Password is not valid."
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(not(re.fullmatch(regex, email_id))):
            return "Invalid Email"
                                
        pwd = bytes(pwd,'utf-8')
        hashed_pwd = hashlib.sha3_256(pwd).hexdigest()

        query = "insert into users(username,password,email) values(%s,%s,%s)"
        values = (uname, hashed_pwd, email_id)

        try:
            self.__cursor.execute(query,values)
            self.__conn.commit()
            print("User registration successful.")
            return True
        except:
            print("Some unknown error occurred while creating employee.")

        return False


    def login(self,uname,pwd):

        query = 'select password from users where username="'+uname+'";'
        self.__cursor.execute(query)
        user = self.__cursor.fetchall()

        if len(user)==0:
           return "Invalid Username"
        
        pwd = bytes(pwd,'utf-8')
        hashed_pwd = hashlib.sha3_256(pwd).hexdigest()
        
        if hashed_pwd != user[0][0]:
            return "Invalid Password"
        
        query = 'select id from users where username="'+uname+'";'
        self.__cursor.execute(query)
        id = self.__cursor.fetchall()
        self.user_logs(id[0][0])

        print("User successfully logged in.")
        login_status = True
        return True


    def user_logs(self,id):

        query = "insert into users_logs(uid) values(%s)"
        values = (id,)

        try:
            self.__cursor.execute(query,values)
            self.__conn.commit()
            return True
        except:
            print("Some unknown error occurred while creating employee.")

        return False
