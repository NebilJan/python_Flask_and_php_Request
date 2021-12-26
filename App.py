from flask import Flask,request,jsonify
import random,datetime
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
     Date_up=datetime.now()
     html=f"""
     <!DOCTYPE html>
<html>
    <head>
        <meta http-equiv='content=text/html; charset=utf-8' />
        <meta name='viewport' content='width=device-width,initial-scale=1.0'>
        <title>Information Sender </title>
        <style type='text/css' media='all'>
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

