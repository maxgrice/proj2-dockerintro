from flask import Flask, render_template, abort 
import os

app = Flask(__name__) # request.args.get("name") /?name=file.html

# Decorator: @ calls the function below
@app.route("/<filename>") # by default, only listens to GET requests
def findfile(filename): # name given to specfic route
    path = "templates/" + filename
    if filename.find("//")!=-1 or filename.find("~")!=-1 or filename.find("..")!=-1:
        abort(403)
    else:
        if os.path.isfile(path):
            return render_template(filename) # sends 200/OK by default
        else:
            abort(404)

@app.errorhandler(404) # route to handle 404 error code
def error_404(e):
	return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e): # route to handle 403 error code
	return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0') 

# host='0.0.0.0' means that web app is accesible to any device on the network
# @app.route("/") refers to website root (ie. http://127.0.0.1:5000/)
