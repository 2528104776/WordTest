import random,os


words = []
os.remove('../每日单词.txt')

with open('专升本单词.txt')as file:
    f = file.read().split('\n')

def random_word():
    num = random.randint(1, 3464)
    print(f[num])
    words.append(f[num])

def get_words():
    global words
    for i in range(20):
        random_word()
    words = list(set(words))
    if len(words)==20:
        print('已随机提取20个无重复单词')
    else:
        print('检测到重复！')
        for i in range(20-len(words)):
            random_word()
    for word in words:
        with open('../每日单词.txt','a',encoding = 'utf-8')as file:
            file.write(word + '\n')
            print('写入成功！')
            
def removal():
    times=0
    for i in f:
        if i not in words:
            with open('专升本单词222.txt','a',encoding = 'utf-8')as file:
                file.write(i + '\n')
                times+=1
    print(times)
        
        



get_words()
removal()
