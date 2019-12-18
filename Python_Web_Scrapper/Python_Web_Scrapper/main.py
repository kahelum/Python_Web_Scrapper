from Building_a_Job_Scrapper import Extracting_indeed_pages as indeed

last_indeed_pages = indeed.extract_indeed_pages()

indeed_jobs = indeed.extract_indeed_jobs(last_indeed_pages)

print(indeed_jobs)
