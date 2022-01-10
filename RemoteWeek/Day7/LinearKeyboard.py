t = int(input())
for i in range(t):
    min_time = 0
    times = []
    keyboard = input()
    s = input()
    for j in range(1, len(s)):
        prev = keyboard.index(s[j - 1]) + 1
        curr = keyboard.index(s[j]) + 1
        time = abs(prev - curr)
        min_time += time
    print(min_time)
    
 # time: O(n^2)
 # space: O(1) 
