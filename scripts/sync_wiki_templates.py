#!/usr/bin/env python3
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

REPO = "GardenEric260122/lwy_wiki"
BRANCH = "main"
SRC_PATH = "wiki_dump/templates"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, "liwenya-wiki-template", "references", "templates")
EXCLUDE_FILE = os.path.join(BASE_DIR, "scripts", "exclude_templates.txt")
INDEX_FILE = os.path.join(DEST_DIR, "INDEX.md")

API = "https://api.github.com"
UA = {"User-Agent": "wenya-wiki-sync"}


def load_exclude():
    names = set()
    with open(EXCLUDE_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            names.add(line)
    return names


def api_get(url, raw=False, retries=3):
    headers = dict(UA)
    if raw:
        headers["Accept"] = "application/vnd.github.raw"
    else:
        headers["Accept"] = "application/vnd.github+json"
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
                continue
            raise
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
                continue
            raise
    raise RuntimeError(f"failed to fetch {url}")


def main():
    exclude = load_exclude()

    listing = json.loads(
        api_get(f"{API}/repos/{REPO}/contents/{SRC_PATH}?ref={BRANCH}")
    )
    all_names = [x["name"] for x in listing if x.get("type") == "file"]

    synced = sorted(
        n for n in all_names if n.endswith(".wiki") and n not in exclude
    )
    excluded = sorted(n for n in all_names if n in exclude)

    branch = json.loads(api_get(f"{API}/repos/{REPO}/branches/{BRANCH}"))
    sha = branch["commit"]["sha"]

    os.makedirs(DEST_DIR, exist_ok=True)
    for name in synced:
        quoted = urllib.parse.quote(name, safe="")
        content = api_get(
            f"{API}/repos/{REPO}/contents/{SRC_PATH}/{quoted}?ref={BRANCH}",
            raw=True,
        )
        with open(os.path.join(DEST_DIR, name), "wb") as f:
            f.write(content)

    for filename in os.listdir(DEST_DIR):
        if filename == "INDEX.md":
            continue
        if filename not in synced:
            os.remove(os.path.join(DEST_DIR, filename))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# wiki_dump/templates 镜像",
        "",
        f"- 同步时间：{now}",
        f"- 上游：https://github.com/{REPO}（{BRANCH}）",
        f"- 上游 commit：{sha}",
        f"- 路径：{SRC_PATH}",
        f"- 同步文件：{len(synced)} 个（黑名单排除 {len(excluded)} 个）",
        "- 策略：黑名单（见 scripts/exclude_templates.txt，可自行增删）",
        "",
        "## 同步文件",
        "",
    ]
    lines += [f"- {name}" for name in synced]
    lines += [
        "",
        "## 说明",
        "",
        "此目录由 .github/workflows/sync-wiki-templates.yml 每日北京时间 12:00 自动更新，请勿手动编辑。",
        "模板参数以上游模板源码为准；SKILL.md 中的表格仅为快速参考，两者不一致时以本镜像为准。",
        "",
    ]
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"synced {len(synced)} templates, excluded {len(excluded)}, upstream sha {sha}")
    for name in synced:
        print("  synced:", name)

    return 0


if __name__ == "__main__":
    sys.exit(main())