from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json

#creating a flask applicaiton instance 
app = Flask("__name__")

@app.route("/createJIRA",methods=['POST'])
def createJIRA():


    payload_json = request.get_json(silent=True) or {}

    comment_body = (payload_json.get("comment", {}).get("body") or "").strip()
    
    if comment_body != "/jira":
        return "No /jira command found — ignoring", 200


    url = "https://username.atlassian.net/rest/api/3/issue"

    API_TOKEN = ""

    auth = HTTPBasicAuth("vnsakinal@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "PYT"
        },
        "issuetype": {
        "id": "10040"
        },
        "summary": "First JIRA Ticket",
    },
    "update": {}
    } )


    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0',port=5000)