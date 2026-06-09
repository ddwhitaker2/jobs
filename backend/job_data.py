# To start this we should first define what a job is. Usually, we would create a class, but I want to dumb it down as much as possible so I can learn as much as possible.
# So lets start by creating a dictionary to represent a job. That way we can find whats exactly in a job...

job = {
    "title" : "Software Engineer",
    "company" : "GitHub",
    "location" : "remote",
    "description" : "We are looking for a software engineer to join our team.",
    "skills" : ["Java", "JavaScript", "Python", "React"],
    "apply_url" : "https://example.com/jobs/apply"
}

# This dictionary represents what a job is and I can think of it like a cardboard box that contains all the information about the job.

# So how do we process many jobs? Lets use a list of dictionaries...

jobs = [{
    "title" : "Software Engineer",
    "company" : "GitHub",
    "location" : "remote",
    "description" : "We are looking for a software engineer to join our team.",
    "skills" : ["Java", "JavaScript", "Python", "React"],
    "apply_url" : "https://example.com/jobs/apply"
},
{
    "title" : "Software Engineer Intern",
    "company" : "Google",
    "location" : "Mountain View, CA",
    "description" : "We are looking for a software engineer intern to join our team.",
    "skills" : ["C++", "GoLang", "Python", "React"],
    "apply_url" : "https://example.com/jobs/apply"
},
{
    "title" : "Machine Learning Engineer",
    "company" : "Meta",
    "location" : "San Francisco, CA",
    "description" : "We are looking for a machine learning engineer to join our team.",
    "skills" : ["Python", "TensorFlow", "PyTorch", "Scikit-learn"],
    "apply_url" : "https://example.com/jobs/apply"
}]

# fix: Before it gets out of hand, I converted the "location" field to be lowercase