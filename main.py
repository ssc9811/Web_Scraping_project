import requests
from bs4 import BeautifulSoup

URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def job_search(max_page):
    for page in range (int(max_page)):
        result = requests.get(f"{URL}&start={page}")
        print(result.status_code)


def max_page() :
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    pagination = soup.find("div",{"class":"pagination"}).find_all("a")
    page = []
    for pages in pagination[:-1]:
        page.append(pages.string)
        max_page = page[-1]
    return max_page

max_page = max_page()
job_search(max_page)