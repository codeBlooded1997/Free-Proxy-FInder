from flask import Flask, render_template, request, redirect
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

app = Flask(__name__) # creating app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scraper', methods=['GET', 'POST'])
def scraper():
    title_ls = []
    company_ls = []
    summary_ls = []
    if request.method == 'POST':
        print("Starting to scrpe...")
        job_title = request.form['title']
        location = request.form['location']
        indeed_url = "https://ca.indeed.com/jobs?q={}&l={}".format(job_title, location)
        print("Grabbing website...")
        page = requests.get(indeed_url)
        soup = bs(page.content, "html.parser")
        print("Parsing data...")
        result = soup.find(id='resultsCol')
        job_list = result.findAll('div', {'class': 'jobsearch-SerpJobCard'})
        for value in job_list:
            title = value.find('div', {'class': 'title'})
            company = value.find('span', {'class': 'company'})
            summary = value.find('div', {'class': 'summary'})

            if None in (title, company, summary):
                continue
            title_ls.append(title.text.strip())
            company_ls.append(company.text.strip())
            summary_ls.append(summary.text.strip())

        indeed_table = pd.DataFrame(
            {
                "Title": title_ls,
                "Company": company_ls,
                "Summary": summary_ls,
            }
        )
        return indeed_table
    else:
        print("Else is running")
        return redirect('/scraper')




if __name__ == "__main__":  # if we are running the app from command line(__main__)
    app.run(debug=True)  # it will turn on debug mode