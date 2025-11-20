# def product(arr):
#     if len(arr)<2:
#         return f"No products possible"
#     new_arr = []
#     for i in range(len(arr)):
#         product_val = 1
#         for j in range(len(arr)):
#             if j!=i:
#                 product_val *= arr[j]
#                 print(product_val)
#         new_arr.append(product_val)
#     return new_arr


# print(product([2]))


def product_except_self(arr):
    n = len(arr)
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    running = 1
    for i in range(n):
        prefix[i] = running
        running *= arr[i]

    running = 1
    for i in range(n-1, -1, -1):
        print(i)
        suffix[i] = running
        running *= arr[i]
    
    print(suffix)

    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result


print(product_except_self([1,2,3]))