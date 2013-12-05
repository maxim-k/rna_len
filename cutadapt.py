__author__ = 'Maxim K'

import os

intab = 'ACGT'
outtab = 'TGCA'

adapter = 'TGGAATTCTCGGGTGCCAAGGAACTC'
adapter_rev = adapter.translate(str.maketrans(intab, outtab))[::-1]

seq_path = 'E:\\Work\\sandbox\\seq\\'

for dirname, dirnames, filenames in os.walk(seq_path):
    for filename in filenames:
        file = open(os.path.join(dirname, filename), 'r')
        file_filter = open(os.path.join(dirname, filename).replace('seq', 'clean'), 'w')
        line0 = ''
        line1 = ''
        line2 = ''
        line3 = ''
        short_adapter = ''
        short_adapter_rev = ''
        for line in file:
            line0 = line1
            line1 = line2
            line2 = line3
            line3 = line
            if (line0) and (line0[0] == '@'):
                if (len(line1) >= 25) and (('+' in line2) and (len(line2) == 2)):
                    if not (short_adapter):
                        short_adapter = line0.split(sep=':')[-1].replace('\n', '')
                        short_adapter_rev = short_adapter.translate(str.maketrans(intab, outtab))[::-1]

                    if (line1.find(adapter) >= 0):
                        line1 = line1.replace(adapter, '')
                    else:
                        line1 = line1.replace(adapter_rev, '')

                    if (line1.find(short_adapter) >= 0):
                        line1 = line1.replace(short_adapter, '')
                    else:
                        line1 = line1.replace(short_adapter_rev, '')

                    if (line0[-1] != '\n'):
                        line0 += '\n'
                    if (line1[-1] != '\n'):
                        line1 += '\n'

                    file_filter.write(''.join([line0, line1, line2, line3]))


