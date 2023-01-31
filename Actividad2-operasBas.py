from flask import Flask,render_template
from flask import request

app=Flask(__name__)

@app.route("/operasbas",methods=["GET"])
def operasbas():
    return render_template("operasbas.html")

@app.route("/resultado",methods=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    res=int(n1)*int(n2)
    cadena="La multiplicacion es "
    n3=int(n2)
    while n3>0:
        if n3==1:
            cadena=cadena+"{}".format(n1)
        else :
            cadena=cadena+"{}".format(n1)+" + "
        n3=n3-1
    cadena=cadena+" = "+"{}".format(res)
    return render_template("resultado.html",cadena=cadena)

if __name__ == "__main__":
    app.run(debug=True,port=3000)