def number_of_trees(n):
    if n == 0:
        return 1
    total = 0
    for i in range(n):
        left = number_of_trees(i)
        right = number_of_trees(n - i - 1)
        total += left * right
    return total


if __name__ == "__main__":
    n = 11
    for i in range(n):
        print(number_of_trees(i))
