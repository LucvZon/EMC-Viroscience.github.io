import requests
import os
import yaml 

# --- Configuration ---
ORG_NAME = "EMC-Viroscience"
API_URL = f"https://api.github.com/orgs/{ORG_NAME}/repos"
OUTPUT_FILE = "repo-listing.yml"

def fetch_repos():
    """Fetches repository data from the GitHub API."""
    print(f"Fetching repositories for organization: {ORG_NAME}...")
    try:
        params = {'sort': 'pushed', 'direction': 'desc', 'per_page': 100}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        print("Successfully fetched repository data.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return None

def create_listing_yaml(repos):
    """Creates a single YAML file with the repository listing."""
    if not repos:
        print("No repositories to process.")
        return

    repo_list = []
    for repo in repos:
        # Skip archived repositories
        if repo.get('archived', False):
            continue

        description = repo.get('description') or "No description available."
        
        # This structure matches your original manual listing
        repo_item = {
            'path': repo['html_url'],
            'title': repo['name'],
            'description': description
        }
        repo_list.append(repo_item)

    # Write the list of dictionaries to a YAML file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(repo_list, f, default_flow_style=False, sort_keys=False)
        
    print(f"Generated repository listing at: {OUTPUT_FILE}")

if __name__ == "__main__":
    repositories = fetch_repos()
    if repositories:
        create_listing_yaml(repositories)
