if __name__ == "__main__":
    n = int(input())
    set1 = set(map(int, input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans.sort()
    for i in ans:
        print(i)
