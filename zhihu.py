import requests,re,json
from contextlib import closing

class zhihu(object):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        self.target = 'https://www.zhihu.com/api/v4/questions/274197649/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=xxxxxx&platform=desktop&sort_by=default'
        self.pic = []
        self.text = []
        self.lis = []
        self.name = []

    def get_text(self,page):
        for i in range(0,page * 5,5):
            url = self.target.replace('xxxxxx',str(i))
            r = requests.get(url, headers=self.headers, )
            r.encoding = 'utf-8'
            r = json.loads(r.text)
            for each in r['data']:
                self.lis.append(each['content'])

                self.name.append(each['author']['name'])

    def optimization(self):
        html = []
        for txt in self.lis:
            txt = txt.replace('<p>', '')
            txt = txt.replace('</p>', '\n')
            txt = txt.replace('<br>', '')
            txt = txt.replace('<b>', '')
            txt = txt.replace('</b>','')
            html.append(txt)
        text = "\n\n\n\n\n\n\n\n\n\n\n".join(html)
        img= re.findall(r'img src="(https.*?jpg)"', text, re.S)
        for i ,j in enumerate(img):
            self.pic.append(img[i])
        txt = []
        for i in html:
            i = re.sub(r'(<figure>.*?</figure>)',"",i)
            i = re.sub(r'(<a.*?>.*?</a>)', "", i)
            self.text.append(i)

    def write_txt(self):
        with open(r'E:\test\1.txt','w+',encoding='utf-8') as f:
            for name in range(len(self.name)):
                f.write(self.name[name] + ':\n\n\n' + self.text[name] + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        for i,j in enumerate(self.pic):
            pic = requests.get(self.pic[i],headers=self.headers)
            with closing(pic) as r:
                with open(r'E:\test\pic\%s.jpg' % i,'ab+') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()

if __name__=='__main__':
    page = int(input('Please enter the page:\n'))
    zh = zhihu()
    zh.get_text(page)
    zh.optimization()
    zh.write_txt()
