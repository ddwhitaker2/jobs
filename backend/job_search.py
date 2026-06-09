# We need to create a set of functions to help with this search.

# The first one I want to create is a search_jobs function that will allow us to search through a db or list of job dictionaries to find the "matches" for a given search term.

def search_jobs(jobs, search_term):
    matches = []

    for job in jobs:
        if search_term.lower() in job["title"].lower() or search_term.lower() in job["description"].lower():
            matches.append(job)

    return matches