
fhand = open('mbox-short.txt')
for read in fhand:
    if read.startswith('X-DSPAM-CONFIDENCE:'):
        print(read)