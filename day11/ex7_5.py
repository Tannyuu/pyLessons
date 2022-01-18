
#file_r = open('sample.txt','r'))
#file_w = open('copy.txt','w')
#for line in file_r:
#    file_w.write(line)
#file_r:close()
#file_w:close()


file_r = input('コピー元のファイルパス>>')
file_r2 = open('file_r','r')
file_w = input('コピー後のファイルパス>>')
file_w2 = open('file_w','w')
for line in file_r:
    file_w.write(line)
file_r:close()
file_w:close()
