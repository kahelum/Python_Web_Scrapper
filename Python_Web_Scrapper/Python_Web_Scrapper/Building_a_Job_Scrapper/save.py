import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode = "w", encoding='UTF8')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])   # .strip('\n') is error -> 'int' object has no attribute 'strip'
    for job in jobs:
        writer.writerow(list(job.values())  )# .strip('\n') is error 
                                             # -> 'dict_values' object has no attribute 'strip' 
                                                # 'list' object has no attribute 'strip'
                                                # 'int' object has no attribute 'strip' 
    return