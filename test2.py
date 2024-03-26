import jieba
f = open('data.txt','r')   
lines = f.readlines()
f.close()
f = open('out.txt','w')    
for line in lines:     
    line=line.strip()              #删除每行首尾可能出现的空格
    wordList =jieba.lcut(line)         #用结巴分词，对每行内容进行分词
    f.writelines('\n'.join(wordList))  #将分词结果存到文件out.txt中
f.close()
