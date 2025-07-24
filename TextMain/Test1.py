def hello(name):
    print(name)

def printInfo():
    print('aaa')
    print('bbb')
    print('ccc')

def main():
    name = input('your name: ')
    hello(name)
    printInfo()

# print(__name__) # __name__ >> 本檔案(Test1)
if __name__ == '__main__':
    main() 
# 如果是本檔案(test1)執行，就 ~ >> 也就是說這樣在test2 透過 import 呼叫就不會執行