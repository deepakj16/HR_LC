'''
Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

'''

if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2
    out=[]
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if (a+b+c)!=n:
                    #print([a,b,c])
                    out.append([a,b,c])
    print(out)