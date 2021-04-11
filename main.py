from datetime import datetime 
from typing import List
import sqlite3
import sys
import traceback
import waybackpy


query = """
select distinct
  pl.url
from
  moz_bookmarks bk_child
  join moz_bookmarks bk_parent on bk_child.parent = bk_parent.id
  join moz_places pl on bk_child.fk = pl.id
where
  url like 'http%'
order by
  bk_child.dateAdded desc
"""


def log(message: str):
    timestamp = datetime.now().isoformat()
    print(f'[{timestamp}] {message}', flush=True)


def save(url: str):
    user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0'
    log(f'Start: {url}')
    try:
        wayback = waybackpy.Url(url, user_agent)
        archive = wayback.save()
        log(f'Done: {archive.archive_url}')
    except Exception as e:
        log(f'Error: {url}, {e}')
        log(traceback.format_exc())


def get_db_path() -> str:
    usage = 'Usage: main.py /path/to/firefox/places.sqlite'
    assert len(sys.argv) == 2, usage
    assert sys.argv[1].endswith('places.sqlite'), usage
    return sys.argv[1]


def get_bookmark_urls() -> List[str]:
    bookmarks = []
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    for row in cur.execute(query):
        bookmarks.append(row[0])
    return bookmarks


def main():
    log('Run Start')
    for url in get_bookmark_urls():
        save(url)
    log('Run End')


if __name__ == '__main__':
    main()

