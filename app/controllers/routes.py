from app import app
from flask import Flask, render_template


@app.route("/")
@app.route("/Home")
def index():
	return render_template('base.html')