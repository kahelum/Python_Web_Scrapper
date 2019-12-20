import requests
from bs4 import BeautifulSoup

LIMIT = 50
indeed_URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(indeed_URL)
    #print(indeed_result) 정상 작동 확인

    soup = BeautifulSoup(result.text, "html.parser")      # 페이지가 총 몇개인지
    #print(indeed_soup) 정상 작동 확인

    pagination = soup.find("div", {"class" : "pagination"})      # pagination 부분만 찾기
    #print(pagination) 정상 작동 확인

    links = pagination.find_all('a')        # 링크 찾기

    pages = []                              # 링크를 리스트로 정리
    """
    for link in links:
       #pages.append(link.find("span").string)     # 각 링크안에 span 찾아서 string만 리스트에 넣기
      pages.append(link.string)                   # anchor = 'a' 가 있고 그 요소안에 string이 오직 하나 있다면
                                                # anchor에서 바로 string을 실행해도 됨 (BeautifulSoup이 알아서 찾아줌)                                                            
    #pages = pages[0:-1]        아래와 같은 결과.
    pages = pages[:-1]
    print(pages)
    """

    for link in links[:-1]:
        pages.append(int(link.string))
    #print(pages)
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("div", {"class" : "title"}).find('a')["title"]
    company = html.find("span", {"class" : "company"})
    try: #if company:  # 회사이름이 없는 경우 company_anchor = company.find('a')에서 None 오류가 발생해서 try / except적용 or if / eles사용
        company_anchor = company.find('a')
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
    except: #else:
        company = "Unknown" #company = None
    company = company.strip()
    location = html.find("div",{"class" : "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, "link": f"https://www.indeed.com/viewjob?jk={job_id}"}

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed page : {page}")
        result = requests.get(f"{indeed_URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)       # result = html
            jobs.append(job)
    return jobs


def get_jobs():
    last_indeed_pages = extract_indeed_pages()
    indeed_jobs = extract_indeed_jobs(last_indeed_pages)
    return indeed_jobs
