import requests
import datetime

# Replace with your GitHub token
GITHUB_TOKEN = 'your_github_token'
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repo_info(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch repo info: {response.status_code}')

def get_commits(owner, repo, since=None):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'since': since} if since else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch commits: {response.status_code}')

def get_issues(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    params = {'state': 'open'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch issues: {response.status_code}')

def get_pull_requests(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    params = {'state': 'open'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch pull requests: {response.status_code}')

def analyze_maintenance_activity(owner, repo):
    repo_info = get_repo_info(owner, repo)
    print(f"Repository: {repo_info['full_name']}")
    print(f"Description: {repo_info['description']}")

    # Get commits in the last 90 days
    since_date = (datetime.datetime.now() - datetime.timedelta(days=90)).isoformat()
    commits = get_commits(owner, repo, since=since_date)
    print(f"Number of commits in the last 90 days: {len(commits)}")

    # Get open issues
    issues = get_issues(owner, repo)
    print(f"Number of open issues: {len(issues)}")

    # Get open pull requests
    pull_requests = get_pull_requests(owner, repo)
    print(f"Number of open pull requests: {len(pull_requests)}")

if __name__ == '__main__':
    owner = 'owner_name'
    repo = 'repo_name'
    analyze_maintenance_activity(owner, repo)
