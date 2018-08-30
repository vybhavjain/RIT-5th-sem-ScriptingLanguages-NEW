words=dict()
with open('myfile.txt','rb') as file:
    for word in (word for line in file for word in line.split()):
        if word in words:
            words[word]+=1
        else:
            words[word]=1

words=dict(sorted(words.items(),key=lambda x:x[1],reverse=True))
