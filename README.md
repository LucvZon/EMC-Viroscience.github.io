# EMC Viroscience Website

This repository contains the Quarto source code for the EMC Viroscience website, hosted at [https://lucvzon.github.io/EMC-Viroscience.github.io/](https://lucvzon.github.io/EMC-Viroscience.github.io/). The site serves as a central hub for bioinformatics workflow manuals, tool documentation, blog posts, and relevant links for the group.

[![Deploy Quarto Website](https://github.com/LucvZon/EMC-Viroscience.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/LucvZon/EMC-Viroscience.github.io/actions/workflows/deploy.yml)

## Technology

*   **Content & Structure:** [Quarto](https://quarto.org/)
*   **Hosting:** [GitHub Pages](https://pages.github.com/)
*   **Deployment:** Automated via [GitHub Actions](./.github/workflows/deploy.yml)

## Repository Structure

*   `_quarto.yml`: Main website configuration (navigation, sidebars, etc.).
*   `index.qmd`: Homepage content and top-level listings.
*   `posts/`: Source `.qmd` files for blog posts and multi-part manuals. See contribution guide for naming conventions.
*   `repos/`: Source `.qmd` files defining specific repository links listed on the homepage.
*   `.github/workflows/`: Contains the CI/CD workflow for automatic deployment.
*   `docs/`: **(Generated Output)** This directory contains the rendered website. It is automatically generated and deployed by GitHub Actions. **Do not commit changes to this directory manually.**

## Local Preview

To preview the website locally before contributing:

1.  Ensure you have [Quarto installed](https://quarto.org/docs/get-started/).
2.  Clone this repository: `git clone https://github.com/EMC-Viroscience/EMC-Viroscience.github.io.git`
3.  Navigate to the directory: `cd EMC-Viroscience.github.io`
4.  Run: `quarto preview`
5.  This will render the site locally and open it in your default web browser.
    *Note: Remember not to commit the `docs/` directory generated during local preview.*

## Contributing

We welcome contributions! Please see the detailed guide on the website:

*   **[How to Contribute Manuals and Content](https://lucvzon.github.io/EMC-Viroscience.github.io/contribute/add_manuals.html)**

In summary, the process involves:
1.  Forking the repository.
2.  Creating a new branch for your changes.
3.  Adding or editing source files (primarily `.qmd` files in `posts/` and potentially `_quarto.yml`).
4.  Committing **only the source file changes** to your branch.
5.  Pushing your branch to your fork.
6.  Opening a Pull Request against the `main` branch of this repository.
7.  Once merged, GitHub Actions will automatically render and deploy your changes.