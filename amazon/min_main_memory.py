class Solution:
    def perform(self, processes, m):
        if processes is None:
            return 0
        if m == 0:
            return sum(processes)

        l = 0
        r = 0
        n = len(processes)
        max_sum = 0
        coun = 0
        while r < n:
            if r - l + 1 > m:
                coun -= processes[l]
                l += 1
            coun += processes[r]
            max_sum = max(max_sum, coun)
            r += 1
        return sum(processes) - max_sum


if __name__ == "__main__":
    processes = [10, 4, 8, 13, 20]
    m = 2
    s = Solution()
    print(s.perform(processes, m))