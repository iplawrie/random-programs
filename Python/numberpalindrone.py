import sys

"""def palindroneCheck(num):
    length = len(num)-1
    for index, x in enumerate(num):
        if num[index] != num[length-index]:
            return False
    return True
"""
def palindroneCheck(num):
    flippedNum = int(str(num)[::-1])
    if num == flippedNum:
        return True
    return flippedNum
            
            
            
def main(argv):
    num = int(argv)
    print(num)
    flippedNum = palindroneCheck(num)
    while(flippedNum != True):
        num += flippedNum
        print(num)
        flippedNum = palindroneCheck(num)

if __name__ == '__main__':
    main(sys.argv[1])