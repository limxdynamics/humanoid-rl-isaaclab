# Copyright (c) 2025, LimX Dynamics Technology Co., Ltd.
# SPDX-License-Identifier: Apache-2.0

"""Documentation checks: local links resolve, in-page anchors exist, the two
READMEs keep the same structure, and published images carry no EXIF data."""

import re
from pathlib import Path

import pytest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
READMES = [ROOT / "README.md", ROOT / "README_cn.md"]
LINK_RE = re.compile(r'(?:\]\(|src="|href=")([^)"\s]+)')
FENCE_RE = re.compile(r"```.*?```", re.S)


def _body(path: Path) -> str:
    return FENCE_RE.sub("", path.read_text(encoding="utf-8"))


def _anchor(heading: str) -> str:
    text = re.sub(r"[^\w\- 一-鿿]", "", heading.strip().lower())
    return text.replace(" ", "-")


@pytest.mark.parametrize("readme", READMES, ids=lambda p: p.name)
def test_local_links_and_anchors_resolve(readme):
    body = _body(readme)
    anchors = {_anchor(h) for h in re.findall(r"^#+ (.+)$", body, re.M)}
    broken = []
    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("#"):
            if target[1:] not in anchors:
                broken.append(target)
            continue
        if not (ROOT / target.split("#")[0]).exists():
            broken.append(target)
    assert not broken, f"broken links in {readme.name}: {broken}"


def test_readmes_have_the_same_number_of_sections():
    counts = [len(re.findall(r"^#{1,3} ", _body(p), re.M)) for p in READMES]
    assert counts[0] == counts[1], counts


@pytest.mark.parametrize(
    "image",
    sorted(p for p in (ROOT / "source" / "limx_rl_forge" / "docs").iterdir() if p.suffix in {".png", ".jpg"}),
    ids=lambda p: p.name,
)
def test_images_have_no_exif(image):
    with Image.open(image) as im:
        assert len(im.getexif()) == 0
