import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
}
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return

        response = requests.get(url)
        if response.status_code != 200:
            return
        return response.text
