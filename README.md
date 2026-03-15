# AiNewsletter

This repository contains the working base for the AI newsletter site and issue drafts.

## Python transcript helper

`youtube_transcript.py` fetches a transcript for a YouTube video URL.

Setup:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Run it:

```bash
.venv/bin/python youtube_transcript.py "https://youtube.com/watch?v=U6BdiJsIHC8"
```

If you want to call it with `python3`, activate the virtual environment first:

```bash
source .venv/bin/activate
python3 youtube_transcript.py "https://youtube.com/watch?v=U6BdiJsIHC8"
```

## Hugo site

The site lives in `hugo`.

Run locally:

```bash
cd hugo
hugo server
```

The local site is available at `http://localhost:1313/`.
