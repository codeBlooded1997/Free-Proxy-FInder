from flask import Flask, render_template

app = Flask(__name__) # creating app

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":  # if we are running the app from command line(__main__)
    app.run(debug=True)  # it will turn on debug mode