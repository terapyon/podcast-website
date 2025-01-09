import feedparser
RSS_URL = "https://anchor.fm/s/14480e04/podcast/rss"


def fetch_episode(url: str) -> list[dict[str, str | None]]:
    d = feedparser.parse(url)
    items = d.entries
    return items


def get_title(item: dict[str, str | None]) -> str | None:
    return item.get("title")


def get_attr(item: dict[str, str | None], key: str) -> str | None:
    return item.get(key, "?")


def get_audio(item: dict[str, str | None]) -> tuple[str | None, str | None]:
    for link in item.links:
        if link.rel == "enclosure":
            return link.length, link.href
    return None, None


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) < 2:
        print("Usage: python make_title_list.py filename")
        sys.exit(1)
    filename = args[1]
    url = RSS_URL
    items = fetch_episode(url)
    with open(filename, "w") as f:
        for item in reversed(items):
            title = get_title(item)
            date = get_attr(item, "published")
            episode = get_attr(item, "itunes_episode")
            length, audio = get_audio(item)
            f.write(f"{episode},{date},{length},{audio},{title}")
            f.write("\n")
