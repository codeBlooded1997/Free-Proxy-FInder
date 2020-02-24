from flask import Flask, render_template, request, send_from_directory
from scraper import *

app = Flask(__name__) # creating app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/results')
def results():
    scraper = ProxyScraper()
    scraper.run()

    return render_template('results.html', proxies=scraper.results)

@app.route('/download')
def doawnload():
    return send_from_directory('', 'proxies.csv', as_attachment=True)
if __name__ == "__main__":  # if we are running the app from command line(__main__)
    app.run(debug=True, threaded = True)  # it will turn on debug mode

