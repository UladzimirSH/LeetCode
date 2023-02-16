from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        if '0000' == target:
            return 0

        queue = [[[0, 0, 0, 0], 0]]
        seen = [0] * 10000

        while queue:
            queue_element = queue.pop(0)
            target_candidate = queue_element[0]
            turn = queue_element[1] + 1
            for i in range(4):
                k = target_candidate.copy()
                if k[i] == 9:
                    k[i] = 0
                else:
                    k[i] = k[i] + 1

                l = target_candidate.copy()
                if l[i] == 0:
                    l[i] = 9
                else:
                    l[i] = l[i] - 1

                k_str = str(k[0]) + str(k[1]) + str(k[2]) + str(k[3])
                k_int = int(k_str)
                l_str = str(l[0]) + str(l[1]) + str(l[2]) + str(l[3])
                l_int = int(l_str)

                if k_str == target or l_str == target:
                    return turn

                if k_str in deadends:
                    seen[k_int] = 1
                if l_str in deadends:
                    seen[l_int] = 1

                if seen[k_int] == 0:
                    seen[k_int] = 1
                    queue.append([k, turn])

                if seen[l_int] == 0:
                    seen[l_int] = 1
                    queue.append([l, turn])

        return -1


solution = Solution()
print(solution.openLock(
    ["5557", "5553", "5575", "5535", "5755", "5355", "7555", "3555", "6655", "6455", "4655", "4455", "5665", "5445",
     "5645", "5465", "5566", "5544", "5564", "5546", "6565", "4545", "6545", "4565", "5656", "5454", "5654", "5456",
     "6556", "4554", "4556", "6554"], "5555"))
# print(solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
print(solution.openLock(["0101"], "0000"))
