# The goal of this file is to establish a set of functions that will help us manage adding job data to the program.

def add_job(jobs, title, company, location, description, skills, apply_url):
    new_job = {
        "title": title,
        "company": company,
        "location": location,
        "description": description,
        "skills": skills,
        "apply_url": apply_url
    }
    jobs.append(new_job)

    return jobs