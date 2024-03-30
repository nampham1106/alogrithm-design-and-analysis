def Activity_selector(A):
    S = [A["a1"]]
    j = 1
    for i in range(2, len(A)+1):
        if (A["a" + str(i)][0] >= A["a" + str(j)][1]):
            S.append(A["a" + str(i)])
            j = i
    return S

if __name__ == "__main__":
    # activity: name: (time_start, time_end)
    activities = {
        "a1": (1, 3),
        "a2": (2, 5),
        "a3": (4, 7),
        "a4": (1, 8),
        "a5": (5, 9),
        "a6": (8, 10),
        "a7": (9, 11),
        "a8": (11, 14),
        "a9": (13, 16),
    }
    activities = dict(sorted(activities.items(), key=lambda item: item[1][1]))
    print(f'Activity after sort in increasing order of end time: {activities}')
    print(f'solution: {Activity_selector(activities)}')