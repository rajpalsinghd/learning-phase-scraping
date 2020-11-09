from flask import *


app=Flask(__name__)

@app.route("/")
def main_endpoint():
 return render_template("index.html")


app.run(port=4000)