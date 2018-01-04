## Capstone Overview
This app will provide an Ada family tree to help us not only keep track of teachers and their cohort of students, but also visually map the growth of the Ada student network. Clicking on members of the tree will provide basic information (e.g. name, cohort, linkedIn, and optional capstone information). This app may be used by anyone in the Ada family who would like to connect or learn more about their fellow Adies.

## Product Plan
Product Plan: https://gist.github.com/JNEdrozo/84d61f563256436c853303e4172af2e9

## Project User Stories
Target User: The web app is intended for current or former Ada students or staff who would like to see where they are in the Ada family social network expansion.

**Public/Unauthenticated Users:**

As a non-logged-in user, I can:
- log in as an existing user or,
- create a profile account to add to the existing Ada family tree using required info:
  - first name
  - last name
  - pronouns
  - Ada relationship (student, teacher, other)
  - Cohort Affiliation (students select their graduating class cohort and teachers/staff select the cohorts they have served)
  - Optional to include: Ada Internship Company, LinkedIn, Capstone Info, ADA/Life-Hacking Tips or mottos to live by

**Authenticated Users:**

As a logged-in user, I can:
- log in and view the entire Ada family tree
- edit my own profile info

As a logged-in user, when I:
- click on a member, I can read their profile information

## Technologies
- Back-end: Python, Django framework with a postgreSQL database
- front-end: D3, bootstrap, html/css
- Hosting: Heroku to deploy
