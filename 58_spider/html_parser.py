from bs4 import BeautifulSoup
import re
class HtmlParser(object):

    def parser_url(self, html_cont):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.find_all('a',class_="t",href=re.compile('http://zhuanzhuan.58.com/detail/'))
        return urls



    def parser_data(self, content):

        soup = BeautifulSoup(content, 'lxml')
        category = soup.select('span.crb_i > a')[0].text
        title = soup.select('div.box_left_top > h1')[0].text
        view = soup.select('p > span.look_time')[0].text
        price = soup.select('div.price_li > span > i')[0].text
        place = soup.select('div.palce_li > span > i')[0].text

        category,title,view,price,place in zip(category,title,view,price,place)
        data = {
            'category':category,
            'title':title,
            'view':view,
            'price':price,
            'place':place
        }
        return data