## Overview:
This app will provide an ADA family tree to help us not only keep track of teachers and their cohort of students, but also visually map the growth of the ADA student network. Teachers will be treated as paretns and their respective leaves are students. Clicking on members of the tree will provide basic information (e.g. name, cohort, linkedIn, and optional capstone information). This app may be used by anyone in the ADA family who would like to connect or learn more about their fellow Adies.

### Product Plan
Product Plan: https://gist.github.com/JNEdrozo/84d61f563256436c853303e4172af2e9

### Project User Stories

**Authenticated Users:**
As a logged-in user, I can:
- view the entire ADA family tree
- add a member to the family tree (using a form)

As a logged-in user, when I:
- click on an ADA member, I can read their profile information: name, cohort, linkedIn, Optional Info: Capstone Info
- edit a member's profile info

**Public/Unauthenticated Users:**
As a non-logged in user, I can:
- contact ADA for viewing permissions (with links to ADA's website)

### Technologies
- Back-end: Python, Django framework with a postgreSQL database
- front-end: D3, bootstrap, html/css
- Hosting: Heroku to deploy
