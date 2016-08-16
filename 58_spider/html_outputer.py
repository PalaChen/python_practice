class HtmlOutputer(object):
    def __init__(self):
        self.datas= []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_text(self):
        with open(r'D:\python3\58_spider\info.txt','w') as file:
            for data in self.datas:
                file.writelines('分类：{}\t,题目：{}\t,浏览人数：{}\t,价格：{}\t,区域：{}\t\n'.\
                        format(data['category'],data['title'],data['view'],data['price'],\
                               data['place']))