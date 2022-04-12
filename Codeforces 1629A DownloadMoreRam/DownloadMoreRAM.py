for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ram = [[a[i], b[i]] for i in range(n)]
    
    ram.sort()
    
    for i in range(len(ram)):
        if ram[i][0] <= k:
            k += ram[i][1]
            
    print(k)
