import sqlite3

class Register:
    def __init__(self,db):
       self.con=sqlite3.connect(db)
       self.cur=self.con.cursor()
       self.cur.execute('''create table if not exists Register
                        (id integer primary key,name text,lname text,name_course text ,password integer )''')
       self.con.commit()

    def select(self):
        self.cur.execute('select *from Register')
        return self.cur.fetchall()
    
    def insert(self,name,lname,name_course,password):
        self.cur.execute('''insert into register(id,name,lname,name_course,password) values (NULL,?,?,?,?)
                         ''',(name,lname,name_course,password))
        self.con.commit()
    
    def delete(self,id):
        self.cur.execute('delete from Register where id = ?',(id,))
        self.con.commit()
    
    def validate_user(self,password):
        self.cur.execute('select *from Register where password = ?',(password,))
        return self.cur.fetchone()

        








ri1=Register('D:/p_database/cours_db')
