# GitHub to Jira Issue Sync (Webhook Based Integration)

This project automates the creation of Jira tickets from GitHub issues using GitHub webhooks and a Flask-based API. When a developer comments "/jira" on a GitHub issue, the system automatically creates a corresponding Jira ticket. This helps development teams track bugs, analyze tasks, and maintain a record of issues resolved over a period of time.

## Project Overview

Teams often raise issues directly on GitHub, but use Jira for planning, sprint management, and long-term tracking. Manually transferring issues from GitHub to Jira can be repetitive and error-prone.

This project solves that by providing an automated workflow:
1. A GitHub issue is created.
2. A team member comments "/jira" on the issue.
3. GitHub sends a webhook to the Flask API hosted on AWS EC2.
4. The server verifies the comment text.
5. If the comment is exactly "/jira", a Jira issue is created through the Jira REST API.
6. If the comment is anything else, the webhook is ignored.

## How it Works

GitHub webhook -> Flask API -> Jira REST API -> Jira ticket is created.

Only the "/jira" command triggers Jira issue creation. All other comments are safely ignored.

## Architecture Flow

GitHub Issue Comment  
↓  
GitHub Webhook  
↓  
Flask API (Hosted on AWS EC2)  
↓  
Jira REST API  
↓  
Jira Ticket Created

## Technology Used

- Python (Flask)
- GitHub Webhooks
- Jira Cloud REST API
- Requests library
- AWS EC2 (deployment)
- Optional local tunneling (ngrok) for development

## Repository Structure

project/
│── github_jira.py
│── README.md
│── requirements.txt

### Deploying on AWS EC2
This project was deployed on an EC2 instance. Basic steps:

1. Launch an EC2 instance.
2. SSH into the instance.
3. Install Python and pip.
4. Clone the repository.
5. Install dependencies using: pip install -r requirements.txt
6. Run the Flask app
7. Open the required port (e.g., 5000) in the EC2 security group.
8. Use the EC2 public IP as your webhook URL.


## Features
- Automatically creates Jira tickets only when "/jira" is commented.
- Prevents accidental Jira ticket creation.
- Helps developers track open and closed issues.
- Maintains a clear record of issues resolved within a given timeframe.
- Supports both EC2 deployment and local development through tunneling.

## Future Enhancements
- Add support for sending the Jira ticket link back to GitHub as a comment.
- Map GitHub issue title and body to Jira fields.

## License
This project is open for personal and educational use.
