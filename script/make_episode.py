from typing import Dict, List, Generator, Optional
import dataclasses  # for Test
from dataclasses import dataclass, field
from pathlib import Path
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
    id: str
    author: str
    published: str
    image: str
    # duration: int  # itunes_duration
    itunes_season: int  # season number
    itunes_episode: int  # episode number
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


def get_detail(item: Dict[str, Optional[str]]) -> Episode:
    field_values = [
        item.get(field.name) for field in dataclasses.fields(Episode) if field.init
    ]
    return Episode(*field_values)


def _get_filenames(path: Path) -> Generator[str, None, None]:
    for entry in path.iterdir():
        if entry.is_file():
            entry_prefix = entry.stem
            if entry_prefix.isdigit():
                yield entry_prefix


def _get_last_filename(path: Path) -> str:
    filenames = list(_get_filenames(path))
    sorted_filenames = sorted(filenames)
    last_filename = sorted_filenames[-1]
    return last_filename


def create_page(episode: Episode, path: Optional[Path] = None) -> None:
    if path is None:
        path = Path(".") / "src" / "episodes"
    last_filename = _get_last_filename(path)
    print(last_filename)
    return None


if __name__ == "__main__":
    url = RSS_URL
    items = fetch_episode(url)
    for item in items[:1]:
        detail = get_detail(item)
        # print(detail)
        create_page(detail)

    # fields = dataclasses.fields(Episode)
    # for field in fields:
    #     if field.init:
    #         print(field.name)
    #     # breakpoint()
