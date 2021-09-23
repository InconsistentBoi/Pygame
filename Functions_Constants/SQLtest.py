import mysql.connector as sql
import pygame
from Functions_Constants import counters, constants, mfunc

def sql_input(user_text, pw_text):

    try:
        if user_text=="":
            raise Exception()
        mycon = sql.connect(host='localhost',user='root',database='learning',password='password')
        cursor = mycon.cursor()

        cursor.execute("select max(sno) from account;")
        curr_sno=cursor.fetchall()[0][0] + 1
        sql_command = '''insert into account values (%s, %s, %s);'''

        create = (curr_sno, user_text, pw_text)

        cursor.execute(sql_command, create)
        mycon.commit()
        mycon.close()
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 10,10

    except:
        counters.draw_text("haha noob",constants.font,(255,255,255), constants.WIN, 1000,0)
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 1000,10

def sql_login(user_text, pw_text):
    try:
        if user_text=='':
            raise Exception()
        
        mycon = sql.connect(host='localhost',user='root',database='learning',password='password')
        cursor = mycon.cursor()

        sql_command = '''select uname from account where uname=%s and pword=%s;'''

        sign_in = (user_text, pw_text)

        cursor.execute(sql_command, sign_in)

        data = cursor.fetchall()
        for rec in data:
            if rec == '':
                raise Exception()
            else:
                return True
        mycon.close()
        
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 10,10
        

    except:
        counters.draw_text("haha noob",constants.font,(255,255,255), constants.WIN, 1000,0)
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 1000,10






    
