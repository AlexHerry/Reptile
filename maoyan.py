import requests
import re


class downloader(object):
    def __init__(self):
        self.target = 'https://maoyan.com/board/4?offset=xxx'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36/'
        }
        self.ranking = []
        self.name = []
        self.star = []
        self.time = []
        self.score = []

    def get_html(self, page):
        temp_ranking = []
        temp_name = []
        temp_star = []
        temp_time = []
        temp_score = []
        for i in range(0, page*10, 10):
            url = re.sub(r'\w+$', str(i), self.target, re.S)
            req = requests.get(url, headers=self.headers)
            temp_ranking.append(re.findall(r'board-index-\d+">(\d+)</i>', req.text, re.S))
            temp_name.append(re.findall(r'"name">.*?>(.*?)</a>', req.text, re.S))
            temp_star.append(re.findall(r'"star">.*?\s(.*?)\s</p>', req.text, re.S))
            temp_time.append(re.findall(r'"releasetime">(.*?)</p>', req.text, re.S))
            temp_score.append(re.findall(r'"integer">(.*?)</i>.*?"fraction">(\d)</i>', req.text, re.S))
        for i in temp_ranking:
            for j in i:
                self.ranking.append(j)
        for i in temp_name:
            for j in i:
                self.name.append(j)
        for i in temp_star:
            for j in i:
                j = re.sub(r'\s+', '', j)
                self.star.append(j)
        for i in temp_time:
            for j in i:
                self.time.append(j)
        for i in temp_score:
            for j in i:
                num = str(j[0]) + str(j[1])
                self.score.append(num)
        return req.text

    def get_txt(self):
        for i, j in enumerate(self.ranking):
            with open('ranking.txt', 'a+') as f:
                f.write('第 ' + j + ' 名: ' + self.name[i] + '\n' + self.star[i] + '\n' + self.time[i] + '\n' + '评分: ' +
                        self.score[i] + '\n\n\n\n\n\n\n\n')
        return 'OK!!!!'


if __name__ == '__main__':
    page = int(input('你要爬几页?\n'))
    print('准备链接:')
    rank = downloader()
    html = rank.get_html(page)
    txt = rank.get_txt()
