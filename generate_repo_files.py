# generate_repo_files.py

import requests
import os
import shutil

# --- Configuration ---
ORG_NAME = "EMC-Viroscience"
API_URL = f"https://api.github.com/orgs/{ORG_NAME}/repos"
OUTPUT_DIR = "_generated_repos"

def fetch_repos():
    """Fetches repository data from the GitHub API."""
    print(f"Fetching repositories for organization: {ORG_NAME}...")
    try:
        # We can sort by 'pushed' to get the most recently updated repos first
        params = {'sort': 'pushed', 'direction': 'desc', 'per_page': 100}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print("Successfully fetched repository data.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return None

def create_qmd_files(repos):
    """Creates a .qmd file for each repository."""
    if not repos:
        print("No repositories to process.")
        return

    # Clean up old generated files by removing and recreating the directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Created output directory: {OUTPUT_DIR}")

    # Create a .qmd file for each repo
    for repo in repos:
        # Skip archived repositories
        if repo.get('archived', False):
            continue

        file_name = f"{repo['name']}.qmd"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        
        # Use description if available, otherwise provide a default
        description = repo.get('description') or "No description available."
        # Sanitize description to avoid breaking YAML (e.g., quotes)
        description = description.replace('"', '\\"').replace("'", "\\'")

        # Create the YAML frontmatter content for the .qmd file
        content = f"""---
title: "{repo['name']}"
description: "{description}"
href: "{repo['html_url']}"
---
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
    print(f"Generated {len(repos)} .qmd files in {OUTPUT_DIR}.")

if __name__ == "__main__":
    repositories = fetch_repos()
    if repositories:
        create_qmd_files(repositories)
