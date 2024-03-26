import jieba
f = open('out.txt','r')    #以读的方式打开文件
words = f.readlines()
f.close()
D={}
for w in words:        #词频统计
    D[w[:-1]]=D.get(w[:-1], 0) + 1
print("曹操出现次数为:{}  ".format(D['曹操']))