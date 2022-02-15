
from random import randint

def sum_process (sums_arr=[]):
    nums_arr = []
    results_arr = []
    max_len_num = 0

    for num in sums_arr:
        if len(num) > max_len_num:
            max_len_num = len(num)

        nums_arr.append(num)
    
    index = 0
    for num in nums_arr:
        num = list(num)

        while len(num) < max_len_num:
            num.append("0")
        
        nums_arr[index] = "".join(num)
        index += 1

    results_arr = list(nums_arr.pop(0))
    residue_result = ["0" for i in range(len(results_arr))]
    for i in range(len(nums_arr)):
        residue = "0"
        result_arr = []
        for j in range(len(results_arr)):
            result = str((int(results_arr[j][-1:]) + int(nums_arr[i][j])) + int(residue))

            if int(result) > 9:
                residue = result[:-1]
                residue_result[j] = str(int(residue_result[j]) + int(residue))
            else:
                residue = "0"

            result_arr.append(result)

        results_arr = result_arr
        residue = "0"

    index = 0
    for residue in residue_result:
        results_arr[index] = residue + results_arr[index][-1:]
        index += 1

    return results_arr

if __name__ == "__main__":
    arr_sum = []
    for i in range(randint(3, 4)):
        arr_sum.append(str(randint(10 ** 6, 10 ** 8)))

    # arr_sum = [
    #     "1111",
    #     "1111",
    #     "1111"
    # ]

    results = sum_process(arr_sum)

    print(" + ".join(arr_sum))
    print(f"total: {results}")




