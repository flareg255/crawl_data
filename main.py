import Url_str, File_wr, MkdirDaily, time, urllib, os, glob
import pandas as pd
from pyquery import PyQuery as pq

class Main:
    url_str = Url_str.Url_str()
    urls = url_str.getUrls()

    mkdirDaily = MkdirDaily.MkdirDaily()

    file_wr = File_wr.File_wr()

    def getImg(self):

        dirPaths = self.mkdirDaily.mkdirMake()

        resultItems = []

        for url in self.urls:
            time.sleep(2)

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

                    self.file_wr.download_file_to_dir(resultItem['img'], dirPaths[1])

        df = pd.DataFrame(resultItems)
        df.to_html(os.path.join(dirPaths[0], self.url_str.nameHtmlPath), escape=False)
        df = df.drop('img_src', axis=1)
        df.to_csv(os.path.join(dirPaths[0], self.url_str.nameDataPath), header=False, index=False)
        print(df)


main = Main()
main.getImg()
