import sqlite3
class MyDB:
    def __init__(self):
        self.conn = sqlite3.connect("rec.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" 
                            create table if not exists users(
                                name varchar(50) not null, 
                                admission varchar(8) primary key,
                                email varchar(50) not null,
                                phone varchar (12) not null
                            )
                            """)   
        

    def insertUser(self, name, admission, email, phone):
        try:
            self.cursor.execute("insert into users (name,admission,email,phone) values (?,?,?,?)", (name,admission,email,phone))
            self.conn.commit()
            return 1  
        except sqlite3.IntegrityError:
            return 2     
        except:
            return 3     

            
    def finduser(self,admission):
        self.cursor.execute("select * from users where admission = ?",(admission,))   
        rs = self.cursor.fetchone()
        return rs
    

    def deleteUser(self, admission):
        try:
            self.cursor.execute("delete from users where admission = ?", (admission,))       
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return 2  # No student found
            return 1  # Deletion successful
        except:
            return 3  # An error 
        

    def updateUser(self, name, admission, email, phone):
        try:
            self.cursor.execute("update users set name = ?, email = ?, phone = ? where admission = ?", (name, email, phone, admission))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return 2  # No student found to update
            return 1  # Update successful
        except:
            return 3  # An error occurred
     

    def showall(self):
        self.cursor.execute("select * from users")
        r = self.cursor.fetchall()
        return r 
    


if __name__ == "__main__":
    A = MyDB()        
    print(A.insertUser)
    print(A.finduser())
