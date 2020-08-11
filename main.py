import Url_str, FileWr, MkdirDaily, WebDataGet, time, urllib, os, glob
import pandas as pd
from pyquery import PyQuery as pq

class Main:
    url_str = Url_str.Url_str()
    urls = url_str.getUrls()

    mkdirDaily = MkdirDaily.MkdirDaily()

    fileWr = FileWr.FileWr()

    webDataGet = WebDataGet.WebDataGet()

    def getImg(self):

        dirPaths = self.mkdirDaily.mkdirMake()

        resultItems = []

        for url in self.urls:
            time.sleep(2)

            tempAry = self.webDataGet.getData(url, dirPaths[1])
            resultItems.extend(tempAry)

        df = pd.DataFrame(resultItems)
        df = df.drop('imgSrc', axis=1)
        df.to_html(os.path.join(dirPaths[0], self.url_str.nameHtmlPath), escape=False, index=False)
        df = df.drop('toHtml', axis=1)
        df.to_csv(os.path.join(dirPaths[0], self.url_str.nameDataPath), header=False, index=False)

main = Main()
main.getImg()
