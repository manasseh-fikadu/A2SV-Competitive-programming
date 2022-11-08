class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def get_time(h, m):
            return str(h) + ":" + str(m) if m >= 10 else str(h) + ":0" + str(m)

        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    yield get_time(h, m)