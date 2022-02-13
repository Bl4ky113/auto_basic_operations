
from random import randint
from auto_sum import sum_process

def multiplication_process (mult_1="", mult_2=""):
    results_obj = {}

    num_1 = mult_1[::-1]
    num_2 = mult_2[::-1]

    lvl_mult = 0
    index = 0
    residue = [0 for i in range(len(num_1))]
    for mult in num_1:
        results_obj[f"{index + 1} - {mult}"] = []

        i = 0
        while i < lvl_mult:
            results_obj[f"{index + 1} - {mult}"].append("0")
            i += 1

        for num in num_2:
            result = str((int(num) * int(mult)) + int(residue[index]))

            if int(result) > 9:
                residue[index] = str(result)[:-1]
            else:
                residue[index] = "0"

            results_obj[f"{index + 1} - {mult}"].append(result)
    
        lvl_mult += 1
        index += 1

    sum_arr = []
    index = 0
    for val_arr in results_obj.values():
        val_sum = []
        for val in val_arr:
            val_sum.append(val[-1:])
        
        val_sum.append(residue[index])
        sum_arr.append("".join(val_sum))
        index += 1

    results_obj["sum"] = sum_process(sum_arr)

    results_obj["total"] = int(mult_1) * int(mult_2)

    return results_obj

if __name__ == "__main__":
    # num_mult_1 = str(randint(10 ** 2, 10 ** 3))
    # num_mult_2 = str(randint(10 ** 2, 10 ** 3))

    num_mult_1 = "12345"
    num_mult_2 = "12345"

    results = multiplication_process(num_mult_1, num_mult_2)

    index = 0
    print(f"operation: {num_mult_2} x {num_mult_1}")
    print(list(num_mult_2[::-1]))
    for key, val in results.items():
        print(key, val)