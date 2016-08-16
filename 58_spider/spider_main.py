import html_downloader
import html_outputer
import html_parser
import url_manager

class SpiderMain(object):
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,start,end):
        for i in range(start,end):
            url = 'http://bj.58.com/pbdn/0/pn{}/'.format(i)
            print('爬取第{}个列表页，网址是：{}'.format(i,url))
            html_cont = self.downloader.download(url)
            # 提取链接
            new_urls = self.parser.parser_url(html_cont)
            # 把提取待爬取的url放入url管理器中
            self.urls.add_new_urls(new_urls)
            # 判断url管理器中是否还有没有爬取的url
            while self.urls.has_new_url():
                # 从url管理器中提取待爬取的url
                new_url = self.urls.get_new_url()
                # 检查URL
                # print("待爬取的url",new_url)

                # 下载页面
                content = self.downloader.download(new_url)
                # 解析页面
                data = self.parser.parser_data(content)
                # 检查是否正确获取到data
                # print(data)
                # 把结果存入输出器
                self.outputer.collect_data(data)
            # 爬取完成后，输出结果
            self.outputer.output_text()
        print("脚本运行结束")



if __name__ =='__main__':
    obj_spider = SpiderMain()
    obj_spider.craw(1,4)