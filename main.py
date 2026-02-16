from flask import Flask, redirect, render_template, send_file

app = Flask(__name__)

@app.route("/")
def default():
    return redirect("/html/WYshd.html")

@app.route("/html/<filename>")
def html(filename):
    return render_template(filename)

@app.route("/images/<filename>")
def images(filename):
    return send_file("images/"+filename)