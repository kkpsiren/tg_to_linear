from os import environ
import requests
from queries import get_users


def create_issue(title, description, priority, users, assignee):
    variables = {
        "input": {
            "title": title,
            "projectId": environ.get("PROJECT_ID"),
            "assigneeId": get_users(assignee)[0],
            "description": description,
            "labelIds": [environ.get("LABEL_ID")],
            "priority": priority,
            "stateId": environ.get("STATE_ID"),
            "teamId": environ.get("TEAM_ID"),
            "subscriberIds": get_users(users),
        }
    }

    headers = {
        "Authorization": f"{environ.get('API_KEY')}",
        "Content-Type": "application/json",
    }
    query = """
mutation IssueCreate($input: IssueCreateInput!) {
    issueCreate(input: $input) {
        success
        issue {
            url
        }
    }
}
    """

    data = {"query": query, "variables": variables}

    r = requests.post(environ.get("ENDPOINT"), headers=headers, json=data)
    return r.json()
