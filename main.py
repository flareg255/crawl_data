import Url_str, Text_file_wr, time, urllib, os, glob
import pandas as pd
from pyquery import PyQuery as pq

class Main:
    url_str = Url_str.Url_str()
    urls = url_str.getUrls()

    text_file_wr = Text_file_wr.Text_file_wr()

    def getImg(self):
        cnt = 1

        resultItems = []

        for url in self.urls:
            time.sleep(3)

            data = pq(url)
            data = data(self.url_str.itemGroup)('li')('a')('img')

            for img in data:
                resultItem = {}

                if not pq(img).attr('src') == 'None':
                    resultItem['alt'] = pq(img).attr('alt')
                    resultItem['img_src'] = '<img src="../img/' + pq(img).attr('src').replace(self.url_str.delImgPath, '') + '">'
                    resultItem['img'] = pq(img).attr('src')

                    resultItems.append(resultItem)

                    print(resultItem)

                    try:
                        urllib.request.urlretrieve(resultItem['img'], self.url_str.imgDataPath)
                    except BaseException as e:
                        print(resultItem['img'])
                        print(e)

                    cnt+=1

        df = pd.DataFrame(resultItems)
        df.to_html(self.url_str.actNameDataPath, escape=False)
        df = df.drop('img_src', axis=1)
        df.to_csv(self.url_str.imgDataPath, header=False, index=False)
        print(df)


main = Main()
main.getImg()
