import os, datetime, random

class MkdirDaily:

    def mkdirMake(self):
        new_dir_path = '../' + datetime.datetime.now().strftime("%Y%m%d")

        if os.path.exists(new_dir_path):
            new_dir_path = new_dir_path + str(random.randint(11111,99999))

            if os.path.exists(new_dir_path):
                new_dir_path = new_dir_path + str(random.randint(11111,99999))

        os.mkdir(new_dir_path)

        paths = (new_dir_path + '/data', new_dir_path + '/img')

        os.mkdir(paths[0])
        os.mkdir(paths[1])

        return paths