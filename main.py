from flask import Flask,render_template
from public import public
from admin import admin






app=Flask(__name__)
app.secret_key='alex'


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')


app.run(debug=True,port=5885,host="0.0.0.0")
# app.run(debug=True,port=5017,host="192.168.33.57")