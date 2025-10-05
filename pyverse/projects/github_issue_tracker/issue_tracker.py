# Author: Ayush Yadav
# GitHub: https://github.com/AyushYadav256
# Description: CLI tool to fetch open issues from any GitHub repo using GitHub API

import requests

def fetch_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch issues. Status Code: {response.status_code}")
        return

    issues = response.json()
    if not issues:
        print("✅ No open issues found.")
        return

    print(f"\n📋 Open Issues in {owner}/{repo}:\n")
    for issue in issues:
        print(f"🔹 #{issue['number']} - {issue['title']}")
        print(f"   🔗 {issue['html_url']}\n")

if __name__ == "__main__":
    print("🐙 GitHub Issue Tracker CLI")
    owner = input("Enter repo owner (e.g., itsmedeepak): ")
    repo = input("Enter repo name (e.g., PyVerse): ")
    fetch_issues(owner, repo)
