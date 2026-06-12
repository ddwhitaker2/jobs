// Grab the results container from the HTML
const results = document.getElementById("results");

// This function displays jobs on the page
function displayJobs(jobsToDisplay) {
    results.innerHTML = "";

    for (const job of jobsToDisplay) {
        const jobCard = document.createElement("div");
        jobCard.classList.add("job-card");

        jobCard.innerHTML = `
            <h2>${job.title}</h2>
            <p><strong>Company:</strong> ${job.company}</p>
            <p><strong>Location:</strong> ${job.location}</p>
            <p>${job.description}</p>
            <p><strong>Skills:</strong> ${job.skills.join(", ")}</p>
            <a href="${job.apply_url}" target="_blank">Apply</a>
        `;

        results.appendChild(jobCard);
    }
}