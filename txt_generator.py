# settings
filename = 'testwrite'  # filename without .txt
format = 'A4'
orientation = 'PORTRAIT'
unit = 'mm'
library = 'DICT_6X6_250'


# writing text file
def write():
    for i in range(5):
        newpage()
        marker(5, 48, 200, i+1)


my_txt = open('./'+filename+'.txt', 'w')


def newpage():
    my_txt.write('\n')


def marker(x, y, size, id):
    my_txt.write('\n'+' '.join([str(x), str(y), str(size), str(id)]))


def main():
    # setting
    my_txt.write('FORMAT: '+format+'\n')
    my_txt.write('ORIENTATION: '+orientation+'\n')
    my_txt.write('UNIT: '+unit+'\n')
    my_txt.write('LIBRARY: '+library)
    # writing
    write()


if __name__ == '__main__':
    main()
