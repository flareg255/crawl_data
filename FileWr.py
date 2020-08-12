import os, urllib
import pandas as pd

class FileWr:

    def fileWrite (self, path, str):
        modeType = 'a'
        print(str)
        if not os.path.isfile(path):
            modeType = 'w'

        with open(path, modeType, encoding='utf-8', newline='\n') as fileItem:
            fileItem.write('\n'.join(str))

    def fileReadtoDf (self, url, sortKey):
        htmlTableList = pd.read_html(url, encoding = 'utf-8')
        df = htmlTableList[0]
        df = df.sort_values(sortKey)

        return df

    def download_file(self, url, dst_path):
        try:
            with urllib.request.urlopen(url) as web_file:
                data = web_file.read()
                with open(dst_path, mode='wb') as local_file:
                    local_file.write(data)
        except urllib.error.URLError as e:
            print(e)

    def download_file_to_dir(self, url, dst_dir):
        self.download_file(url, os.path.join(dst_dir, os.path.basename(url)))