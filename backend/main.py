# The goal of this project is to create a service that can scrap over job posting to find jobs and internships that would be beneficial for me to apply to.

# Imports from our own modules
from job_data import jobs
from job_search import search_jobs
from job_manager import add_job

# main
results = search_jobs(jobs, "software")
print(results)

# testing add job mechanic
jobs = add_job(jobs, "Data Sci", "Amazon", "remote", "We are looking for a data scientist from a t100 university that is knowledgeable in these skills and can contribute to leadership", ["Python", "DB management", "SQL", "Machine Learning"], "https://example.com/jobs/apply")

print(jobs)

