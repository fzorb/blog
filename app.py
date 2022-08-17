from flask import Flask, render_template, session, redirect, url_for, flash, request
from flaskext.markdown import Markdown
from os import listdir
from os.path import isfile, join
import os

app = Flask(__name__)
Markdown(app)

app.config['SECRET_KEY'] = 'SIdB8zv5m5vX3QHPxHD3GojV2chTSH8TkhbFWay7vF8gW6W2BKzhr9UknpP51X5hWTxUnVFbBtRfiAj0FFpLETpsxU7AGpc0XI0P47tccwd3ASs5at3zaFMsWnVU8V3f'

@app.before_request
def before_route():
  try:
    print(session['theme'])
    print(session['txtcl'])
  except KeyError:
    session['theme'] = 'light'
    session['txtcl'] = 'dark'


@app.route("/int/theme")
def change_theme():
  if session['theme'] == 'light':
    session['theme'] = 'dark'
    session['txtcl'] = 'light'
  else:
    session['theme'] = 'light'
    session['txtcl'] = 'dark'
  return redirect(url_for('index'))

@app.route("/")
def index():
  #list all files in the posts directory
  posts = [f for f in listdir('posts') if isfile(join('posts', f))]
  dates = []
  #for loop in posts to get the creation date of the file
  for post in posts:
    os.path.getctime("posts/" + post)
    dates.append(int(os.path.getctime("posts/" + post)))
  #order the posts by creation date
  posts = [x for _,x in sorted(zip(dates,posts))]
  return render_template("index.j2", posts=posts, crt = 0, dates = dates)

@app.route("/post/<file>")
def post(file):
  with open ("posts/" + file + ".md", "r") as f:
    content = f.read()
  return render_template("view.j2", content=content)
