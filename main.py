import Url_str, time, urllib, os, glob, openpyxl, PIL
from pyquery import PyQuery as pq

class Main:
    url_str = Url_str.Url_str()

    urls = url_str.getUrls()

    def getImg(self):
        cnt = 1
        wb = None

        if len(glob.glob(self.url_str.excelDataPath)) == 0:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = 'data_sheet_1'
            wb.save(self.url_str.excelDataPath)
        else:
            wb = openpyxl.load_workbook(self.url_str.excelDataPath)

        for url in self.urls:
            time.sleep(3)

            data = pq(url)
            data = data(self.url_str.itemGroup)('li')('a')('img')

            sheet = wb['data_sheet_1']
            sheet.column_dimensions['A'].width = self.url_str.colAWidth
            sheet.column_dimensions['B'].width = self.url_str.colBWidth

            for img in data:
                resultItem = {}

                if not pq(img).attr('src') == 'None':
                    resultItem['alt'] = pq(img).attr('alt')
                    resultItem['img'] = pq(img).attr('src')
                    print(resultItem)

                    imgPath = os.path.join('../img/', resultItem['img'].replace(self.url_str.delImgPath, ''))

                    try:
                        urllib.request.urlretrieve(resultItem['img'], imgPath)
                        imgItem = openpyxl.drawing.image.Image(imgPath)
                        sheet.add_image( imgItem, 'b' + str(cnt) )
                        sheet.row_dimensions[cnt].height = self.url_str.rowHeight
                    except BaseException as e:
                        print(resultItem['img'])
                        print(e)
                    finally:
                        sheet['a' + str(cnt)] = pq(img).attr('alt')
                        sheet['c' + str(cnt)] = pq(img).attr('src')
                        wb.save(self.url_str.excelDataPath)

                        cnt+=1


main = Main()
main.getImg()
