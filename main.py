from indeed_job import get_job as indeed_get_jobs
from stackoverflow import get_job as stack_get_jobs
from save import save

indeed_jobs = indeed_get_jobs()
stack_jobs =  stack_get_jobs()

jobs = indeed_jobs + stack_jobs
save(jobs)
