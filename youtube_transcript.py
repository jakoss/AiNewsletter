#!/usr/bin/env python3

import argparse
import sys
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def extract_video_id(url: str) -> str:
    parsed = urlparse(url.strip())
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")

    if host in {"youtu.be", "www.youtu.be"}:
        if path:
            return path.split("/")[0]
        raise ValueError("Missing video ID in shortened YouTube URL.")

    if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [""])[0]
            if video_id:
                return video_id
        elif path.startswith("embed/") or path.startswith("shorts/"):
            parts = path.split("/")
            if len(parts) >= 2 and parts[1]:
                return parts[1]

    raise ValueError("Unsupported YouTube URL. Pass a full YouTube video URL.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a YouTube transcript and print it to stdout."
    )
    parser.add_argument("url", help="Full YouTube video URL")
    args = parser.parse_args()

    try:
        video_id = extract_video_id(args.url)
        transcript = YouTubeTranscriptApi().fetch(video_id)
        output = TextFormatter().format_transcript(transcript)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
