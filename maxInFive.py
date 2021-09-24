class solution:
    def fiveWala(self, n):

        s = list(map(int, str(n)))
        ans = []
        for i in range(len(s)):
            x = s.copy()
            if x[i] == 5:
                x.pop(i)
                s1 = [str(i) for i in x]
                res = int(''.join(s1))
                print("res ", res)
                ans.append(int(res))

        return max(ans)


if __name__ == '__main__':
    # n = int(input())
    m = 152595
    obj = solution()
    print(obj.fiveWala(m))

