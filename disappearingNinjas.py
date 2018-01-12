# Assignment: Disappearing Ninja
# Build a flask application with the below functionality.

# This exercise will help you practice URL routing, using views, and rendering static content.

# These are the routes that you need to set up:

# 1 On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
# 2 When user visits /ninja, it should display all four Ninja Turtles 
# (Leonardo, Michelangelo, Raphael, and Donatello)

# 3 /ninja/[ninja_color], should display the corresponding Ninja Turtle 
# (grab the color parameter out of the requested URL)
# If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
# /ninja/orange - Ninja Turtle Michelangelo.
# /ninja/red - Ninja Turtle Raphael
# /ninja/purple - Ninja Turtle Donatello
# 
# 4 If a user tries to hack into your web app by specifying a color or string combination other 
# than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, 
# then display the image notapril.jpg
# You'll need to remember how to use static files for this assignment. 
# Take a minute to refresh your memory back to the static files section if you need to :)

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#1
@app.route('/')
def index():
  return render_template("noNinja.html")

#2
@app.route('/ninja')
def ninja():
  return render_template("ninja.html")

#3
@app.route('/ninja/<color>')
def turtlecolor(color):
  return render_template("ninja.html", mycolor = color)
   

app.run(debug=True) # run our server

# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)
# @app.route('/users/<username>/<myid>')
# def show_user_profile(username,myid):
#     print "*" * 80, username
#     print "*" * 80, myid
#     return render_template("index.html", user = username, id1 = myid)
# app.run(debug=True)