from flask import Flask,request,jsonify
App=Flask(__name__)
@App.route("/users",methods=["POST","GET"])
def do():
     data=request.form
     user=data["user"]
     msg=data["msg"]
     f=open("log.txt","a")
     f.write(str(request.form))
     f.close()
     return f"Hi {user}  <br> thanx you msg: {msg}"
if __name__ == "__main__":
    App.run("0.0.0.0",5000,debug=True)

