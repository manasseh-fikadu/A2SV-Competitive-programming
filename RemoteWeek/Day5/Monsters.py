count = 0
        time = 0
        s = sorted([d/s for d, s in zip(dist, speed)])
        for x in s:
            if time < x:
                count += 1
                time += 1
            else:
                break
        return count
