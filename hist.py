__author__ = 'Maxim K'

import os

def write_dic(dic, file, header):
    file.write('%s\n' %(header))
    for key in dic:
        file.write('%s %d\n' % (key, dic[key]))

def if_add(dic, val):
    if val in dic:
        dic[val] +=1
    else:
        dic[val] = 1

#sam_path = 'E:\\Work\\sandbox\\hg19\\sam_0_mismatch'
#sam_len = {}
#sam_count = 0
#sam_seq_len = 0
#
#for dirname, dirnames, filenames in os.walk(sam_path):
#    for filename in filenames:
#        file = open(os.path.join(dirname, filename), 'r')
#        for line in file:
#            if not('@' in line):
#                line = line.split()
#                if_add(sam_len, len(line[9]))
#                sam_seq_len += len(line[9])
#                sam_count += 1
#
#print(sam_seq_len/sam_count)
#file = open('E:\\Work\\sandbox\\hg19\\sam_0mm_len.txt', 'w')
#write_dic(sam_len, file, 'len count')

seq_path = 'E:\\Work\\sandbox\\clean'
seq_len = {}
seq_count = 0
seq_seq_len = 0

for dirname, dirnames, filenames in os.walk(seq_path):
    for filename in filenames:
        file = open(os.path.join(dirname, filename), 'r')
        for line in file:
            if (not('@' in line))and(not('#' in line))and(not('#' in line))and(not('+' in line)):
                    if_add(seq_len, len(line))
                    seq_seq_len += len(line)
                    seq_count += 1

print(seq_seq_len/seq_count)
file = open('E:\\Work\\sandbox\\seq_len.txt', 'w')
write_dic(seq_len, file, 'len count')


