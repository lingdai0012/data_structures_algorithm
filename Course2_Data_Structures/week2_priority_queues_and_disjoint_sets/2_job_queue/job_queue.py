# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at", "ended_at"])


def sift_up(workers: list, index: int):
    if index == 0:
        return
    parent = (index - 1) // 2
    if (workers[parent].ended_at > workers[index].ended_at) or (
        (workers[parent].ended_at == workers[index].ended_at)
        and (workers[parent].worker > workers[index].worker)
    ):
        workers[parent], workers[index] = (
            workers[index],
            workers[parent],
        )
        sift_up(workers, parent)
    else:
        return


def sift_down(workers: list, index: int):
    minimum_index = index
    if 2 * index + 1 > len(workers) - 1:
        return
    else:
        if (workers[2 * index + 1].ended_at < workers[minimum_index].ended_at) or (
            workers[2 * index + 1].ended_at == workers[minimum_index].ended_at
            and workers[2 * index + 1].worker < workers[minimum_index].worker
        ):
            minimum_index = 2 * index + 1

    if 2 * index + 2 <= len(workers) - 1:
        if (workers[2 * index + 2].ended_at < workers[minimum_index].ended_at) or (
            workers[2 * index + 2].ended_at == workers[minimum_index].ended_at
            and workers[2 * index + 2].worker < workers[minimum_index].worker
        ):
            minimum_index = 2 * index + 2

    if minimum_index != index:
        workers[minimum_index], workers[index] = workers[index], workers[minimum_index]
        sift_down(workers, minimum_index)
    return


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    # result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job
    result = []
    workers = [AssignedJob(ii, 0, 0) for ii in range(n_workers)]
    for job in jobs:
        earliest_worker = workers[0]
        assigned_worker = AssignedJob(
            earliest_worker.worker,
            earliest_worker.ended_at,
            earliest_worker.ended_at + job,
        )
        workers[0] = assigned_worker
        result.append(assigned_worker)
        sift_down(workers, 0)
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
