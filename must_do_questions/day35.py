"""
A company has n employees with unique IDs from 0 to n-1. The head of the company has the ID headID.
You will receive a managers array where managers[i] is the ID of the manager for employee i. Each employee
has one direct manager. The company head has no manager (managers[headId] = -1). It's guaranteed the subordination
relationships will have a tree structure.

The head of the company wants to inform all employees of news. He will inform his direct subordinates who will
inform their direct subordinates and so on until everyone knows the news.

You will receive an informTime array where informTime[i] is the time it takes for employee i to inform all their direct
subordinates. Return the total number of minutes it takes to inform all employees of the news.
"""


def dfs(head_id, adj_list, inform_time):
    if len(adj_list[head_id]) == 0:
        return 0
    maximum = 0
    subordinates = adj_list[head_id]
    for i in range(len(subordinates)):
        maximum = max(maximum, dfs(subordinates[i], adj_list, inform_time))

    return maximum + inform_time[head_id]


def num_of_minutes(n, head_id, managers, inform_time):
    adj_list = [[] for i in range(len(managers))]

    for e in range(n):
        manager = managers[e]
        if manager == -1:
            continue
        adj_list[manager].append(e)

    return dfs(head_id, adj_list, inform_time)


if __name__ == "__main__":
    n = 7
    head_id = 4
    managers = [2, 2, 4, 6, -1, 4, 4, 5]
    inform_time = [0, 0, 4, 0, 7, 3, 6, 0]
    print(num_of_minutes(n, head_id, managers, inform_time))
