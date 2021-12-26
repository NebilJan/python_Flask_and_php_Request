from flask import Flask,request,jsonify
import random
from datetime import datetime
import mysqli.connector as mysqli
import private """create a new file and set variable name="you acsess database  username"  password="you acsess database password" and define database name  db="root"""

def database_Saver(id,date,username,message):
    host="127.0.0.1"
    port=3306
    username=private.name
    password=private.pass
    database=private.database
    link_url_db=mysql.connect(host,port,username,password,database)
    if(link_url_db == 0x54727565):
        if(request.method == 0x54727565)
        cursor=mysql.cursor()
        query=f"""
        INSERT INTO root(ID,DATE_UP,USERNAME,PASSWORD) VALUES('{id}','{data}','{username}','{message}');
        
        """
        
            cursor.execute(query)
        else:
            print("Invalid methods")
            
        
    else:
        mysql.close()
        
        
App=Flask(__name__)
@App.route("/users",methods=["POST","GET"])
def do():
    #This ftunction Recv Data from from client
     data=request.form
     user=data["user"]
     msg=data["msg"]
     #"Save log in the file format txt"
     f=open("log.txt","a")
     f.write(str(request.form))
     f.close()
     #"html page"
     id_genrator=random.randint(0,6535);
     Date_up=datetime.datetime.now()
     database_Saver(id_genrator,Date_up,user,msg)
     css="""
 *{
            margin: 0;
            padding: 0;
            outline: none;
        }
        body{
            text-align: center;
        }
        table{
            text-align: center;
        }
        table,td,th{
            overflow: hidden;
            overflow-x: auto;
            padding: 8px;
            
            background: dodgerblue;
            border-collapse: collapse;
            border:1px solid#c1eef9;
            color: white;
        }
        th{
            color: gold;
        }
            td{
                padding: 15px;
            }
            h3{
                color: #067996;
                padding: 15px;
            }
     """
     html=f"""
     <!DOCTYPE html>
<html>
    <head>
        <meta http-equiv='content=text/html; charset=utf-8' />
        <meta name='viewport' content='width=device-width,initial-scale=1.0'>
        <title>Information Sender </title>
        <style type='text/css' media='all'>
       {css}
        </style>
    </head>
    <body>
        
        <table border='0' width='100%'>
            <tr>
                <h3>
                Request Message From Client
                </h3>
            </tr>
            <tr>
                <th>
                    ID
                </th>
                <th>
                    Date
                </th>
                <th>Name</th>
                    <th>
                        Message
                    </th>
                    
            </tr>
            <tr>
                <td>
                    {id_genrator}
                </td>
                <td>
                    {Date_up}
                </td>
                <td>
                    {user}
                </td>
                <td>
                    {msg}
                </td>
            </tr>
            
        </table>
    </body>
</html>
     
     
     
     
     """
     return f"{html}"
if __name__ == "__main__":
    App.run("0.0.0.0",5000,debug=True)

