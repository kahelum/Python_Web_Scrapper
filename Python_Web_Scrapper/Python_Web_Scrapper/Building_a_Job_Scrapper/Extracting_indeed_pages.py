import requests
from bs4 import BeautifulSoup

indeed_URL = "https://www.indeed.com/jobs?q=python&limit=50"

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


