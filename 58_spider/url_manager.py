class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            new_url = url.get('href')
            page_url = new_url.split('?')[0]
            # 检查url
            # print("提取url",page_url)
            if page_url not in self.new_urls and page_url not in self.old_urls:
                self.new_urls.add(page_url)


    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url