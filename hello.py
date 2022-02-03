from flask import Flask, render_template


# Creating Flask instance
app = Flask(__name__)

# Route Decorator
@app.route('/')
def index():
    return render_template("index.html")

# Invalid URL
@app.errorhandler(404)
def page_not_found(e): 
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e): 
    return render_template("404.html"), 500