Work in progress
==

Inspired by [this rust thread](https://www.reddit.com/r/rust/comments/44u4mg/rust_contributorswanted_list/)

Long term vision
===

A sortable, filter-able megatable of FOSS **binaries** and **libraries** being developed in rust, with a focus on developing reports specifically about what projects are looking for contributers

crates.io optimizes for being a relatively simple way to quickly find the package you likely want for this situation. This repo optimizes for providing lots of information about lots of packages at once (without a lot of clicking) relevant to their position in the world of tools built in rust. Like crates.io it is specifically targeted with developers in mind.

Basic approach
====
Data is scraped from crates and github and a TOML is automatically generated / updated for each project. People with projects not on github or listed on crates (e.g. a binary whose source is hosted elsewhere than github) can add them manually by creating a TOML and place it in the ```project_list``` directory, using the ```sample-project-description.toml``` file as a guide

Certain data in each toml, even those scraped from github, can only have certain values set by manual edits, usually only by people who are associated with the project.

```
    example: possible values for looking for new contributors:
        * Unspecified (default, can be set by anyone at all if status is abandoned)
        * No 
        * Skilled Only
        * Yes
        * up for adoption (ie. owner can and will take time to vet people)
        * abandoned (can be set by anyone at all, automatically switched to when no commits in last three months.)
```

these project tomls store two things:

* information that can be used to download the repo and get other contextual information like its license or popularity
* information specified by those knowledgeable of the project as to things requiring up-to-date familiarity with the project.

The python script in the src/ directory then takes the information in this toml and uses it to scrape up-to-date contextual information about each project depending on where this information may be available (e.g. github projects have "stars", cargo crates have "number of downloads").

Using that information, for each locale it then compiles a gigantic json of the information that will be displayed in the webpage for that locale, and injects it through an asset pipeline into a copy of that webpage. all pages are then uploaded to the gh-pages branch

Additionally, for each locale, a markdown file is created that is specifically geared towards projects looking for contributors. It filters out all projects where the "looking for contributors" status is either "unspecified" or "no"

