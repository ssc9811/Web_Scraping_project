import csv

def save(jobs):
    f = open("job.csv","w", encoding="utf-8-sig",newline="")
    writer = csv.writer(f)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return