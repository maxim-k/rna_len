__author__ = 'Maxim K'

import os

seq_path = 'E:\\Work\\sandbox\\test\\'

for dirname, dirnames, filenames in os.walk(seq_path):
    for filename in filenames:
        file = open(os.path.join(dirname, filename), 'r')
        file_filter = open(os.path.join(dirname, filename).replace('test', ''), 'w')
        line0 = ''
        line1 = ''
        line2 = ''
        line3 = ''
        for line in file:
            line0 = line1
            line1 = line2
            line2 = line3
            line3 = line
            if(line0)and(line0[0] == '@'):
                        if(len(line1) >= 25)and(('+' in line2)and(len(line2) == 2)):
                            file_filter.write(''.join([line0, line1, line2, line3]))
