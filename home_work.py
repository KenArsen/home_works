def max_three_numbers(*args):
    return max(args)

a, b, c = map(int, input().split())
print(max_three_numbers(a, b, c))