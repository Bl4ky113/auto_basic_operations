
from random import randint

def update_log (log_arr, msg=""):
    log_arr["log"] = msg

def division_process (num_1="", num_2="", max_decimals=4):
    results_obj = {}
    results_obj["log"] = []
    results_obj["results"] = []
    arr_num = list(num_1)
    division_remaining = arr_num.copy()
    divisor = num_2

    for i in range(len(arr_num)):
        div_scope = division_remaining[i: i + len(divisor)]
        result = int("".join(div_scope)) / int(divisor)
        residue = int("".join(div_scope)) % int(divisor)

        update_log(results_obj, f"Division: {div_scope} / {divisor}")

        if result >= 1:
            results_obj["results"].append(str(result))
            update_log(results_obj, f"Divided: {result}")
        else:
            results_obj["results"].append("0")
            update_log(results_obj, f"Can't divide: 0")

    return results_obj

if __name__ == "__main__":
    # num_div_1 = str(randint(10 ** 7, 10 ** 8))
    # num_div_2 = str(randint(1, 10))

    num_div_1 = "81274572"
    num_div_2 = "9"

    results = division_process(num_div_1, num_div_2)

    print(f"{num_div_1} / {num_div_2}")

    for key, val in results.items():
        print(key, val)
