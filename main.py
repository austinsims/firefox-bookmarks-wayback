import waybackpy

def save(url: str):
    user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0'
    wayback = waybackpy.Url(url, user_agent)
    print(f'[Start] {url}')
    archive = wayback.save()
    print(f'[Done] {archive.archive_url}')

def main():
    save('https://en.wikipedia.org/wiki/Michael_Grecco')

if __name__ == '__main__':
    main()

