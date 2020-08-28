from bs4 import BeautifulSoup
import requests

URL = "https://stackoverflow.com/jobs?q=python"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def job_search(last_page):
    for page in range(int(last_page)):
        result = requests.get(f"{URL}&pg={page}")
        print(result.status_code)

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
job_search(last_page)