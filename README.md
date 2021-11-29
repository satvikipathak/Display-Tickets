# Zendesk Intern Coding Challenge 2022

I have made a flask application that has two endpoints- `/tickets` fetches all the tickets in the account and `/tickets/{ticket-id}` lets the user view details on a single ticket.

Attributes displayed in the list view:
1. Id
2. Subject
3. Priority
4. Status

Attributes displayed in the single ticket view:
1. Id
2. Subject
3. Priority 
4. Status
5. Description
6. Requester/Requester Id
7. Assignee/Assignee Id
8. Updated at

Requester and Assignee Id are displayed when the names of either one are not present in the response.

## Requirements

1. Python 3.8
2. Your favourite IDE (I use VSCode)

## Setup
1. Clone the repository
2. Install flask using pip
3. Open the app.conf file present in the config directory. Enter your subdomain and oauth token
3. Run `python server.py` on the terminal
4. Navigate to the URL in the output
5. Go to `/tickets` to see all the tickets
6. Go to `/tickets/{ticket-id}` to view details on a particular ticket