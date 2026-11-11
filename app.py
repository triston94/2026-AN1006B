from flask import Flask, request, render_template

app = Flask(__name__) # no changes to name

@app.route("/") # run this first

def index():
    return(render_template('index.html'))

if __name__ == "__main__":
    app.run()


