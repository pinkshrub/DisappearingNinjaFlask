from flask import Flask,render_template,request,redirect,session,flash
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja')
def ninjas():
	return render_template("ninja.html")

@app.route('/ninja/<color>')
def color(color):
	print color
	# This looks good, but if you are looking for improvements there are a ways to refactor this logic into few lines/comparisons. 
	# Don't worry though, it's not within the scope of this assignment. Good job!
	if( color == 'blue'):
		return render_template("index.html",color='/static/Ninjas/leonardo.jpg')
	elif( color == 'orange'):
		return render_template("index.html",color='/static/Ninjas/michelangelo.jpg')
	elif( color == 'red'):
		return render_template("index.html",color='/static/Ninjas/raphael.jpg')
	elif( color == 'purple'):
		return render_template("index.html",color='/static/Ninjas/donatello.jpg')	
	else:
		return render_template("index.html",color='/static/Ninjas/notapril.jpg')

app.run(debug=True)	
