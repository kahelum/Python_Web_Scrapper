import requests
from bs4 import BeautifulSoup

stackoverflow_URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def extract_stackoverflow_pages():
    result = requests.get(stackoverflow_URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)
    
def extract_job(html):
    title = html.find("div", {"class" : "-title"}).find("h2").find("a")["title"]
    return {'title': title}

def extract_stackoverflow_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{stackoverflow_URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_stackoverflow_pages = extract_stackoverflow_pages()
    jobs = extract_stackoverflow_jobs(last_stackoverflow_pages)
    return jobs