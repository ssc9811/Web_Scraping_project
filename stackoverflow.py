import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def extract_job(result):
    title = result.find("a",{"class":"s-link"}).get_text()
    company, location = result.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    link = result["data-jobid"]
    return {'title' : title, 'company' : company, 'location' : location, 'link' : f"https://stackoverflow.com/jobs/{link}"} 

def job_search(last_page):
    job = []
    for page in range(int(last_page)):
        print(page)
        result = requests.get(f"{URL}&pg={page}")
        soup = BeautifulSoup(result.text, "lxml")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            jobs = extract_job(result)
            job.append(jobs)
    return job
        

def max_page():
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    pagination = soup.find("div",{"class":"s-pagination"}).find_all("a")

    page = []
    for pages in pagination[:-1]:
        a = pages.get_text(strip=True)
        page.append(a)
        last_page = page[-1]
    return last_page

last_page = max_page()
print(job_search(last_page))