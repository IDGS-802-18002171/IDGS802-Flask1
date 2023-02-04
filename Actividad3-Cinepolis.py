from flask import Flask,render_template
from flask import request
from flask import flash, redirect, url_for
import time

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/operasbas",methods=["GET"])
def operasbas():
    return render_template("FormCine.html")

@app.route("/resultado1",methods=["POST"])
def resultado():
    des=0
    des1=0
    if request.form['txtNom'] and request.form['txtNumCom' ] and request.form['rdb'] and request.form['txtNumBol']:
        nom=request.form.get("txtNom")
        numCom=request.form.get("txtNumCom")
        rdb=request.form.get("rdb")
        numBol=request.form.get("txtNumBol")
        total=int(numCom)*int(numBol)*12
        if int(numBol)>7:
            flash("No mas de 7")
        if 5<int(numBol)<8:
            des=total*.15
        if 2>int(numBol)>=5:
            des=total*.10
        if rdb=="Si":
            des1=total*.10
        cadena=""
        cadena=cadena+"El nombre es {} ".format(nom)+"\n"
        cadena=cadena+"#Compradores {} ".format(numCom)+"\n"
        cadena=cadena+"Targeta Cineto {} ".format(rdb)+"\n"
        cadena=cadena+"Boletas posibles {} ".format(int(numBol)*7)+"\n"
        cadena=cadena+"#Boletas solicitadas {} ".format(numBol)+"\n"
        total=total-des-des1
        des=des+des1
        cadena=cadena+"Total ${} ".format(total)+"\n"
        cadena=cadena+"Descuento aplicado ${} ".format(des)+"\n"
        if int(numBol)<=7:
            return render_template("FormCine.html",cadena=cadena)
        else :
            return render_template("FormCine.html")
    else:
        return 'Favor de llenar todos los campos de forma adecuada'

if __name__ == "__main__":
    app.run(debug=True,port=3000)