#!/usr/bin/env python3
"""Static CSS flow audit for PES Arena.

Reports selectors that can mask state-driven UI: exact cross-file duplicates,
!important density, display:none/visibility:hidden selectors and repeated selectors
inside the room stylesheet. Keyframes are ignored.
"""
from __future__ import annotations
import collections
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSS_FILES = [ROOT / "static/style.css", *sorted((ROOT / "static/css").glob("*.css"))]
TEMPLATES = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in (ROOT / "templates").rglob("*.html"))


def blocks(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    # remove keyframes before selector parsing
    text = re.sub(r"@(?:-webkit-)?keyframes\s+[^\{]+\{(?:[^{}]*\{[^{}]*\})+\s*\}", "", text, flags=re.S)
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", text, flags=re.S):
        raw, body = m.group(1).strip(), m.group(2)
        if raw.startswith("@") or raw in {"from", "to"} or re.fullmatch(r"\d+%", raw):
            continue
        yield raw, body


selector_files = collections.defaultdict(set)
internal_counts = collections.Counter()
hiding = []
important_by_file = {}

for path in CSS_FILES:
    text = path.read_text(encoding="utf-8", errors="ignore")
    important_by_file[path.relative_to(ROOT).as_posix()] = text.count("!important")
    local = collections.Counter()
    for raw, body in blocks(text):
        for selector in [" ".join(s.split()) for s in raw.split(",") if s.strip()]:
            selector_files[selector].add(path.relative_to(ROOT).as_posix())
            local[selector] += 1
            if re.search(r"(?:display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?:\D|$))", body, re.I):
                hiding.append((path.relative_to(ROOT).as_posix(), selector))
    if path.name == "arena_room_v2.css":
        internal_counts.update(local)

cross = [(s, sorted(v)) for s, v in selector_files.items() if len(v) > 1]
room_repeat = [(s, c) for s, c in internal_counts.items() if c > 1]

print("PES Arena CSS Flow Audit")
print("========================")
print(f"CSS files: {len(CSS_FILES)}")
print(f"!important total: {sum(important_by_file.values())}")
print(f"Cross-file exact duplicate selectors: {len(cross)}")
print(f"Repeated selectors inside arena_room_v2.css: {len(room_repeat)}")
print(f"Selectors that can hide UI: {len(hiding)}")
print("\n!important by file")
for f, count in sorted(important_by_file.items(), key=lambda x: -x[1]):
    if count:
        print(f"  {count:4d}  {f}")
print("\nRoom repeated selectors (top 30)")
for s, count in sorted(room_repeat, key=lambda x: (-x[1], x[0]))[:30]:
    print(f"  x{count:<2} {s}")
print("\nCross-file duplicate selectors (non-keyframe, top 40)")
for s, files in sorted(cross, key=lambda x: (-len(x[1]), x[0]))[:40]:
    print(f"  {s} -> {', '.join(files)}")
print("\nState-hiding selectors relevant to room/invite (top 40)")
for f, s in [x for x in hiding if any(k in x[1] for k in ("room", "invite", "modal", "hidden"))][:40]:
    print(f"  {f}: {s}")
