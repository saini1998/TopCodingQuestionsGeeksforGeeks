class solution:
    def printPlusMinus(self, n):
        for i in range(n):
            if i%2 == 0:
                print('+',end='')
            else:
                print('-',end='')
            
        print()



if __name__ == '__main__':
    n = int(input("Enter n: "))

    obj = solution()
    obj.printPlusMinus(n)

# def oddNumbers(l, r):
#     return list(range(l if l % 2 else l + 1, r + 1, 2))