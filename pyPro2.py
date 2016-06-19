import random, string
#add 把变更录入到索引中
#pull 取得远端数据库的内容
def rand_str(num, length = 7):
    f = open('Activation_code.txt', 'wb')
    for i in range(num):
        chars = string.letters + string.digits
        s = [random.choice(chars) for i in range(length)]
        f.write(''.join(s) + '\n')
    f.close()
 
if __name__ == '__main__':
    rand_str(200)
