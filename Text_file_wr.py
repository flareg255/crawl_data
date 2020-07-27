import os

class Text_file_wr:

    def fileWrite (self, path, str):
        modeType = 'a'
        print(str)
        if not os.path.isfile(path):
            modeType = 'w'

        with open(path, modeType, encoding='utf-8', newline='\n') as fileItem:
            fileItem.write('\n'.join(str))