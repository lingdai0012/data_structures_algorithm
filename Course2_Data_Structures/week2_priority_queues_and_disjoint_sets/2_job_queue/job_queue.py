# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at", "ended_at"])


class Binary_Complete_Tree:
    def __init__(self):
        self.__nodes = []

    def insert(self, node: AssignedJob):
        self.__nodes.append(node)
        self.sift_up(len(self.__nodes) - 1)

    def sift_up(self, index: int):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.__nodes[parent].ended_at > self.__nodes[index].ended_at:
            self.__nodes[parent], self.__nodes[index] = (
                self.__nodes[index],
                self.__nodes[parent],
            )
        else:
            return

    def sift_down(self, ii: int):
        minimum_index = ii
        if (
            2 * ii + 1 < len(self.__nodes)
            and self.__nodes[2 * ii + 1].ended_at < self.__nodes[minimum_index].ended_at
        ):
            minimum_index = 2 * ii + 1

        if (
            2 * ii + 2 < len(self.__nodes)
            and self.__nodes[2 * ii + 2].ended_at < self.__nodes[minimum_index].ended_at
        ):
            minimum_index = 2 * ii + 2

        if minimum_index != ii:
            self.__nodes[ii], self.__nodes[minimum_index] = (
                self.__nodes[minimum_index],
                self.__nodes[ii],
            )
            self.sift_down(minimum_index)
        else:
            return

    def extract_minimum(self):
        if self.is_empty():
            return
        else:
            latest_node = self.__nodes[0]
            self.__nodes[0] = self.__nodes[-1]
            self.__nodes = self.__nodes[:-1]
            self.sift_down(0)
            return latest_node

    def is_empty(self):
        return self.__nodes == []

    def show_nodes(self):
        return self.__nodes


# class Queue:
#     def __init__(self):
#         self.__items = []

#     def enqueue(self, key):
#         self.__nodes.append(key)

#     def dequeue(self):
#         return self.__nodes.pop(0)

#     def is_empty(self):
#         return self.__items == []

#     def peek(self):
#         return self.__items[0]


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    # result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job
    result = []
    tree = Binary_Complete_Tree()
    workers = list(range(n_workers))
    for job in jobs:
        if len(workers) > 0:
            worker = workers.pop(0)
            assignedJob = AssignedJob(worker, 0, job)
            tree.insert(assignedJob)
            result.append(assignedJob)
        else:
            quickiest_thread = tree.extract_minimum()
            assignedJob = AssignedJob(
                quickiest_thread.worker,
                quickiest_thread.ended_at,
                quickiest_thread.ended_at + job,
            )
            tree.insert(assignedJob)
            result.append(assignedJob)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
