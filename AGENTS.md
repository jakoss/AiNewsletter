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

## Editorial content

- Published issues live in `hugo/content/issues`.
- The canonical issue template is `hugo/content/issues/ai-newsletter-baseline.md`.
- The newsletter overview page lives in `hugo/content/about.md`.
- New issue drafts for the site should follow the editorial structure from `hugo/content/issues/ai-newsletter-baseline.md` unless there is a clear reason to diverge.
- The default editorial voice should stay practical, skeptical of hype, and aimed at developers working in IT.
- Prefer short editorial sections with a clear thesis, supporting context, practical takeaways, and curated source links.
- When summarizing external materials, be explicit when a summary is AI-generated and verified by humans.
- If a source cannot be summarized reliably, say so honestly instead of inventing or overclaiming.

## Standard issue structure

- `# Wydanie X - {data wydania}`
- `## Po co ten newsletter?`
- `### Jak powstaje ten newsletter`
- `## Teza na dziś: ...`
- `## Jak doszliśmy do obecnego momentu`
- `## Co z tym robić w praktyce?`
- `## Cytat na dziś`
- `## Materiały na start`

## Editorial workflow

1. Collect links, notes, and ideas in `Issues/content/materials`.
2. Shape rough drafts and source commentary in `Issues/content/drafts`.
3. When preparing a site issue, start from `hugo/content/issues/ai-newsletter-baseline.md`.
4. Adapt the template to the topic while preserving the newsletter's tone and structure.
5. Add or revise `hugo/content/about.md` when the overall editorial framing of the newsletter changes.
6. Publish finished pieces as Markdown content in `hugo/content/issues`.
7. Push to `main` to trigger the GitHub Pages deployment workflow.

## Deployment

- GitHub Pages deployment is defined in `.github/workflows/hugo.yml`.
- The workflow checks out submodules, builds the Hugo site from `hugo`, and publishes `hugo/public`.
- In GitHub repository settings, Pages should use `GitHub Actions` as the source.
