import traceback
import sys
import requests

class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = """https://tieba.baidu.com/f?ie=utf-8&kw={}""".format(self.tieba_name) + "&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

    def get_url_list(self):
        #url_list = []
        #for i in range(1000):
        #    url_list.append(self.url_temp.format(i*50))
        #return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "F:\MyDownloads\Download\{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            print(html_str)
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


def main(argv):
    tieba_spider = TiebaSpider("凡人修仙传")
    tieba_spider.run()
    
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as result:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)
