def write_qs(qs):
    with open("qs.txt", "w") as f:
        for i in qs:
            f.write(i + "\n")

def write_ans(ans):
    with open("ans.txt", "w") as f:
        for i in ans:
            f.write(i + "\n")

def read_qs():
    with open("qs.txt", "r") as f:
        qs = f.readlines()
    qs = [i.rstrip("\n") for i in qs]
    return qs

def read_ans():
    with open("ans.txt", "r") as f:
        ans = f.readlines()
    ans = [i.rstrip("\n") for i in ans]
    return ans


if __name__ == "__main__":
    from data import training_qs, answers

    write_qs(training_qs)
    qs = read_qs()
    write_ans(answers)
    ans = read_ans()

    assert(len(qs) == len(ans))
    assert(qs == training_qs)
    assert(ans == answers)