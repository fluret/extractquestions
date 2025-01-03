import string


def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = "-".join(alph[n - i - 1: n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, "-")
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2:: -1]:
            ans.append(i)
    ans = "\n".join(ans)
    print(ans)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
