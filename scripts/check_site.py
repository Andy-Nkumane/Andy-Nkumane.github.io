"""Check the static site's local links, assets, and basic HTML contracts."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
VOID_ELEMENTS = set("area base br col embed hr img input link meta param source track wbr".split())


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.errors = []
        self.stack = []
        self.headings = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag not in VOID_ELEMENTS:
            self.stack.append(tag)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append("Duplicate ID: " + attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        if tag == "html" and not attrs.get("lang"):
            self.errors.append("Missing document language")
        if tag == "img":
            for name in ("src", "alt", "width", "height"):
                if name not in attrs:
                    self.errors.append("Image missing " + name)
        if tag == "meta" and attrs.get("property") == "og:image" and attrs.get("content"):
            self.links.append(attrs["content"])
        for name in ("href", "src"):
            if name in attrs:
                if not attrs[name]:
                    self.errors.append("Empty " + name + " on " + tag)
                else:
                    self.links.append(attrs[name])

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append("Unexpected closing tag: " + tag)
        else:
            self.stack.pop()


def validate_site():
    parser = SiteParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    parser.close()
    referenced_images = set()
    if parser.stack:
        parser.errors.append("Unclosed tags: " + ", ".join(parser.stack))
    if parser.headings != 1:
        parser.errors.append("Expected exactly one h1")
    for link in parser.links:
        url = urlsplit(link)
        normalized_path = unquote(url.path).lstrip("/")
        if normalized_path.startswith("images/"):
            referenced_images.add(normalized_path)
        if url.scheme or url.netloc:
            continue
        if url.path:
            path = ROOT / normalized_path
            if not path.is_file():
                parser.errors.append("Missing local file: " + link)
        if url.fragment and url.path in ("", "index.html", "/index.html"):
            if unquote(url.fragment) not in parser.ids:
                parser.errors.append("Missing anchor: " + link)
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    for reference in re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", css):
        url = urlsplit(reference.strip())
        normalized_path = unquote(url.path).lstrip("/")
        if normalized_path.startswith("images/"):
            referenced_images.add(normalized_path)
        if not url.scheme and not url.netloc and url.path:
            if not (ROOT / normalized_path).is_file():
                parser.errors.append("Missing CSS asset: " + reference)
    images_directory = ROOT / "images"
    if images_directory.is_dir():
        for image in images_directory.iterdir():
            relative_path = image.relative_to(ROOT).as_posix()
            if image.is_file() and relative_path not in referenced_images:
                parser.errors.append("Unreferenced image file: " + relative_path)
    for error in parser.errors:
        print("FAIL: " + error)
    if parser.errors:
        return 1
    print("PASS: HTML nesting, unique IDs, heading, image attributes, local links, anchors, CSS assets, and image inventory")
    print("External URLs and browser accessibility require separate verification.")
    return 0


if __name__ == "__main__":
    sys.exit(validate_site())
