import os
import string
def find_func():
    global panL
    filename = 'javaw.exe'
    disk_list = []
    itl = open(r'config//javalist.ini', 'w+')
    itl.write("")
    itl.close()
    def list_disk():
        for c in string.ascii_uppercase:
            disk = c + ":"
            if os.path.isdir(disk):
                disk = c + ":"
                disk_list.append(disk)
        pan = open(r'config//disklist.ini','w+')
        count = len(disk_list)
        w1 = 0

        for w1 in range(count):
            write_disk = disk_list[w1]+"\n"
            pan.write(write_disk)
            w1 = w1 + 1
        pan.close()

    def find_java():
        global panL
        result = []
        path = panL + '\\'
        i = 0
        for root, lists, files in os.walk(path):
            for file in files:
                if filename in file:
                    i = i + 1
                    wr1te = os.path.join(root, file)#搜索
                    print('%s' % (wr1te))
                    result.append(wr1te)
                    i = i + 1
        count = len(result)
        w1 = 0
        javalist = open(r'config//javalist.ini', 'a+')
        for w1 in range(count):
            write_java = result[w1] + "\n"
            javalist.write(write_java)
            w1 = w1 + 1
        javalist.close()
    list_disk()
    x = 0
    for x in range(len(disk_list)):
        panL = disk_list[x]
        find_java()
        x = x + 1