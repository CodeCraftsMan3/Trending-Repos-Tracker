import requests
import os

def fetch_trending_repositories():
    url = "https://api.github.com/search/repositories?q=created:>2023-01-01&sort=stars&order=desc"
    response = requests.get(url)
    return response.json().get("items", [])

def update_readme(trending_repositories):
    with open("README.md", "w") as readme_file:
        readme_file.write("# Trending Repositories\n\n")
        for repo in trending_repositories:
            readme_file.write(f"- [{repo['name']}]({repo['html_url']}): {repo['description']}\n")

if __name__ == "__main__":
    trending_repositories = fetch_trending_repositories()
    update_readme(trending_repositories)