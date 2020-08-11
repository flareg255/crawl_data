from pyquery import PyQuery as pq
import Url_str, FileWr

class WebDataGet:

    fileWr = FileWr.FileWr()

    url_str = Url_str.Url_str()

    def getData(self, url, saveDirPath):

        data = pq(url)
        datas = data.find(self.url_str.elmPath)

        resultItem = []
        for i, elm in enumerate(datas):
            elementItem = pq(elm)

            imgElm = pq(elementItem).find('img')

            numberWorks = elementItem.find(self.url_str.elmSpan1)
            numberWorks = numberWorks.text().replace(self.url_str.elmDeleteText, '').strip()

            name2 = elementItem.find(self.url_str.elmSpan2)
            name2 = name2.text().strip()

            temp = {
                'toHtml': '<img src="../img/' + imgElm.attr('src').replace(self.url_str.delImgPath, '').strip() + '">' ,
                'name': imgElm.attr('alt'),
                'name2': name2,
                'numberWorks': numberWorks,
                'imgSrc': imgElm.attr('src').replace(' ', '%20').strip()
            }
            print(temp)
            resultItem.append(temp)

            self.fileWr.download_file_to_dir(temp['imgSrc'], saveDirPath)

        return resultItem