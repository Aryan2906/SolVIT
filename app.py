import mysql.connector as cnx
import streamlit
cn=cnx.connect(user='sql12768941',password='f8r1Ev7x2d',host='sql12.freesqldatabase.com',database='sql12768941')
if cn.is_connected()==True:
    print("Connected")
else:
    print("Error")