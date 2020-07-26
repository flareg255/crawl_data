import Url_str, time, urllib, os
from pyquery import PyQuery as pq

class Main:
    url_str = Url_str.Url_str()

    urls = url_str.getUrls()

    def getImg(self):
        resultItems = []

        for url in self.urls:
            time.sleep(3)

            data = pq(url)
            data = data(self.url_str.itemGroup)('li')('a')('img')

            for img in data:
                resultItem = {}

                if not pq(img).attr('src') == 'None':
                    resultItem['alt'] = pq(img).attr('alt')
                    resultItem['img'] = pq(img).attr('src')
                    urllib.request.urlretrieve(resultItem['img'], os.path.join('../img/', resultItem['img'].replace(self.url_str.delImgPath, '')))
                    resultItems.append(resultItem)

        return resultItems

main = Main()
print(main.getImg())
