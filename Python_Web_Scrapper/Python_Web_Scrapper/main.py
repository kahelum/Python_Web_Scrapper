from Building_a_Job_Scrapper import Extracting_indeed_pages as get_indeed
from Building_a_Job_Scrapper import Extracting_stackoverflow_pages as get_stackoverflow
from Building_a_Job_Scrapper import save

indeed_jobs = get_indeed.get_jobs()
stackoverflow_jobs = get_stackoverflow.get_jobs()

jobs = indeed_jobs + stackoverflow_jobs

save.save_to_file(jobs)
