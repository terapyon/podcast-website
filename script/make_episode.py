from typing import Dict, List, Generator, Optional
import dataclasses  # for Test
from dataclasses import dataclass, field, asdict
from pathlib import Path
import feedparser  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

RSS_URL = "https://anchor.fm/s/14480e04/podcast/rss"
BASE_PATH = Path(".") / "src" / "episodes"
EPISODE_LIST_FILE = ".episode_list"

CONTENT_DATA = """---
{attr}
---
{main}

{audio}
"""

CONTENT_ATTR = """title: '{title}'
description: '{description}'
date: {published}
id: {id}
author: {author}
season: {itunes_season}
number: {itunes_episode}
length: {length}
audio_url: {audio_url}
meta:
 - name: og:title
   content: '{title}'
 - name: og:description
   content: '{description}'
 - name: og:image
   content: '{image_href}'"""

CONTENT_MAIN = """# {title}

Published: {published}

Season: {itunes_season} / Number: {itunes_episode}

# Note

{summary}
"""

CONTENT_AUDIO = """
<a-player 
:options="{{
  audio: [
    {{
        name: '{title}',
        artist: 'terapyon',
        url: '{audio_url}',
        cover: '{image_href}'
    }}
    ]
}}"
/>
"""


def _to_int(s: Optional[str]) -> int:
    if s is None:
        return 0
    if s.isdigit():
        return int(s)
    else:
        return 0


def _html_to_str(s: str) -> str:
    soup = BeautifulSoup(s, "html.parser")
    return soup.get_text().replace("'", "").replace("\n", " ")


@dataclass
class Episode:
    title: str
    summary: str
    links: List[Dict[str, str]]
    id: str
    author: str
    published: str
    image: Dict[str, str]
    # duration: int  # itunes_duration
    itunes_season: int  # season number
    itunes_episode: int  # episode number
    image_href: str = field(init=False)
    length: int = field(init=False)
    audio_url: str = field(init=False)
    description: field(init=False)

    def __post_init__(self) -> None:
        image_obj = self.image
        self.image_href = image_obj.get("href", "") if image_obj is not None else ""
        links = self.links
        for link in links:
            rel = link.get("rel")
            if rel == "enclosure":
                self.length = _to_int(link.get("length"))
                self.audio_url = link.get("href", "")
                break
        self.description = _html_to_str(self.summary)[:100]


def fetch_episode(url: str) -> List[Dict[str, Optional[str]]]:
    d = feedparser.parse(url)
    items = d.entries
    return items


def get_detail(item: Dict[str, Optional[str]]) -> Episode:
    field_values = [
        item.get(field.name) for field in dataclasses.fields(Episode) if field.init
    ]
    return Episode(*field_values)


def _get_int_filenames(path: Path) -> Generator[int, None, None]:
    for entry in path.iterdir():
        if entry.is_file():
            entry_prefix = entry.stem
            if entry_prefix.isdigit():
                yield int(entry_prefix)


def _get_last_filename(path: Path) -> int:
    filenames = list(_get_int_filenames(path))
    if not filenames:
        return 0
    sorted_filenames = sorted(filenames)
    last_filename = sorted_filenames[-1]
    return last_filename


def _new_filename(path: Optional[Path]) -> Path:
    if path is None:
        path = BASE_PATH
    last_filename_int = _get_last_filename(path)
    next_filename_int = last_filename_int + 1
    next_filename = f"{next_filename_int:0=4}.md"
    new_file = path / next_filename
    return new_file


def _episode_ids() -> Generator[str, None, None]:
    list_file = Path(".") / "script" / EPISODE_LIST_FILE
    if list_file.exists():
        with list_file.open("r") as f:
            for line in f:
                if line.strip():
                    yield line.strip()


def store_episode_id(id_) -> None:
    list_file = Path(".") / "script" / EPISODE_LIST_FILE
    with list_file.open("a") as f:
        f.write(id_)
        f.write("\n")


def _build_content_data(episode: Episode) -> str:
    attr = CONTENT_ATTR.format(**asdict(episode))
    main = CONTENT_MAIN.format(**asdict(episode))
    audio = CONTENT_AUDIO.format(**asdict(episode))
    data = CONTENT_DATA.format(attr=attr, main=main, audio=audio)
    return data


def _check_episode_id(id_: str) -> bool:
    episode_ids = set(_episode_ids())
    if id_ in episode_ids:
        return True
    else:
        return False


def create_page(episode: Episode, path: Optional[Path] = None) -> None:
    if _check_episode_id(episode.id):
        return None
    data = _build_content_data(episode)
    new_file = _new_filename(path)
    with new_file.open(mode="w") as f:
        f.write(data)
    store_episode_id(episode.id)
    return None


if __name__ == "__main__":
    url = RSS_URL
    items = fetch_episode(url)
    for item in reversed(items):
        detail = get_detail(item)
        # print(detail)
        if not _check_episode_id(detail.id):
            create_page(detail)

    # fields = dataclasses.fields(Episode)
    # for field in fields:
    #     if field.init:
    #         print(field.name)
    #     # breakpoint()
