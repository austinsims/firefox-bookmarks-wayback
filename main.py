from datetime import datetime 
import sqlite3
import sys
import waybackpy


def log(message: str):
    timestamp = datetime.now().isoformat()
    print(f'[{timestamp}] {message}')


def save(url: str):
    user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0'
    wayback = waybackpy.Url(url, user_agent)
    log(f'Start: {url}')
    try:
        archive = wayback.save()
        log(f'Done: {archive.archive_url}')
    except Exception as e:
        log(f'Error: {url}, {e}')


def get_query() -> str:
    query_file = open('query.sql', 'r')
    query = query_file.read()
    query_file.close()
    return query


def get_bookmark_urls() -> list[str]:
    bookmarks = []
    query = get_query()
    conn = sqlite3.connect('places.sqlite')
    cur = conn.cursor()
    for row in cur.execute(query):
        bookmarks.append(row[0])
    return bookmarks


def main():
    for url in get_bookmark_urls():
        save(url)


if __name__ == '__main__':
    main()

