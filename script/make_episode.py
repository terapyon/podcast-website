from typing import Dict, List, Optional
import dataclasses  # for Test
from dataclasses import dataclass, field
import feedparser  # type: ignore

RSS_URL = "https://anchor.fm/s/14480e04/podcast/rss"


def _to_int(s: Optional[str]) -> int:
    if s is None:
        return 0
    if s.isdigit():
        return int(s)
    else:
        return 0


@dataclass
class Episode:
    title: str
    summary: str
    links: List[Dict[str, str]]
    id_: str
    author: str
    published: str
    image: str
    # duration: int  # itunes_duration
    season: int  # itunes_season
    number: int  # itunes_episode
    length: int = field(init=False)
    audio_url: str = field(init=False)

    def __post_init__(self) -> None:
        links = self.links
        for link in links:
            rel = link.get("rel")
            if rel == "enclosure":
                self.length = _to_int(link.get("length"))
                self.audio_url = link.get("href", "")
                break


def fetch_episode(url: str) -> List[Dict[str, Optional[str]]]:
    d = feedparser.parse(url)
    items = d.entries
    return items


def get_detail(item: Dict[str, Optional[str]]) -> str:
    for key, value in item.items():
        print(key)
        print(value)
        print("======")
    return "Done"


if __name__ == "__main__":
    url = RSS_URL
    # items = fetch_episode(url)
    # # print(items)
    # for item in items[:1]:
    #     detail = get_detail(item)
    #     print(detail)
    fields = dataclasses.fields(Episode)
    for field in fields:
        if field.init:
            print(field.name)
        # breakpoint()
