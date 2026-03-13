# AGENTS

This repository is the working base for a company AI newsletter.

## Purpose

- `Issues/content/materials` stores gathered source material, notes, and reference links for upcoming issues.
- `Issues/content/drafts` stores in-progress issue drafts before they are turned into site content.
- `hugo` contains the Hugo site that renders newsletter content as a website.

## Hugo setup

- The site in `hugo` is built with [Hugo](https://gohugo.io/).
- The site content and default user-facing copy should be written in Polish.
- The theme is `hugo-coder`, added as a git submodule at `hugo/themes/hugo-coder`.
- To run the Hugo site locally, navigate to the `hugo` directory and run `hugo server`. The site will be available at `http://localhost:1313/`.

## Deployment

- GitHub Pages deployment is defined in `.github/workflows/hugo.yml`.
- The workflow checks out submodules, builds the Hugo site from `hugo`, and publishes `hugo/public`.
- In GitHub repository settings, Pages should use `GitHub Actions` as the source.

## Typical flow

1. Collect links, notes, and ideas in `Issues/content/materials`.
2. Shape each issue in `Issues/content/drafts`.
3. Publish finished pieces as Markdown content in `hugo/content/issues`.
4. Push to `main` to trigger the GitHub Pages deployment workflow.
