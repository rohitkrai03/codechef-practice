def assign_jobs():
    total_tests = int(input())

    for test in range(total_tests):
        total_jobs, no_of_jobs_done = [int(x) for x in input().strip().split()]

        jobs_done = [int(x) for x in input().strip().split()]
        jobs_done = set(jobs_done)  # for sorting the array.
        jobs_left = [str(job) for job in range(1, total_jobs + 1) if job not in jobs_done]
        print(' '.join(jobs_left[::2]))
        print(' '.join(jobs_left[1::2]))


if __name__ == '__main__':
    assign_jobs()
