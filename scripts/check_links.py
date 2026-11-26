#!/usr/bin/env python3
"""Check repository-local Markdown links; optionally review external HTTP URLs."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def references(path):
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    targets = re.findall(r"\]\(([^\s)]+)\)", text)
    targets += re.findall(r'<(?:img|a)\b[^>]*(?:src|href)="([^"]+)"', text)
    return targets


def remote_check(url):
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Awesome-AI-Agents-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=8) as response:
            return url, response.status, response.url
    except urllib.error.HTTPError as exc:
        return url, exc.code, ""
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return url, None, type(exc).__name__


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", action="store_true", help="Also request external URLs; uncertain results are warnings")
    args = parser.parse_args()
    errors = []
    external = set()
    local_count = 0
    for path in sorted(ROOT.glob("*.md")):
        for target in references(path):
            url = urllib.parse.urlsplit(target)
            if url.scheme in {"http", "https"}:
                if url.hostname != "img.shields.io":
                    external.add(target)
                continue
            if url.scheme or not url.path:
                continue
            local_count += 1
            destination = (path.parent / urllib.parse.unquote(url.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"{path.name}: missing local target {target}")
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    print(f"Checked {local_count} local link targets; {len(errors)} missing. Found {len(external)} unique external URLs.")
    if args.remote:
        with ThreadPoolExecutor(max_workers=8) as pool:
            for url, status, detail in pool.map(remote_check, sorted(external)):
                if status and 200 <= status < 400:
                    if detail != url:
                        print(f"REDIRECT {url} -> {detail}")
                else:
                    print(f"REVIEW {status or detail} {url}")
        print("Remote results require review: HEAD restrictions, authentication, rate limits, and temporary failures can resemble broken links.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
