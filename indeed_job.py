import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def extract_job(job):
    title = job.find("h2",{"class":"title"}).find("a").get_text().strip()
    company = job.find("span",{"class":"company"}).get_text(strip=True)
    location = job.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    link = job["data-jk"]
    return {'title' : title, 'company' : company, 'location' : location, 'link' : f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={link}"}

def job_search(max_page):
    job = []
    for page in range (int(max_page)):
        print(page)
        result = requests.get(f"{URL}&start={LIMIT*page}")
        soup = BeautifulSoup(result.text, "lxml")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
            jobs = extract_job(result)
            job.append(jobs)
    return job

def max_page():
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    pagination = soup.find("div",{"class":"pagination"}).find_all("a")
    page = []
    for pages in pagination[:-1]:
        page.append(pages.string)
        last_page = page[-1]
    return last_page

def get_job():
    last_page = max_page()
    job = job_search(last_page)
    return job
    
