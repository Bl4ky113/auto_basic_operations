
from random import randint

def update_log (log_arr, msg=""):
    log_arr["log"].append(msg)

def division_process (num_1="", num_2="", max_decimals=4):
    results_obj = {}
    results_obj["log"] = []
    results_obj["results"] = []

    division_remaining = list(num_1).copy()
    for i in range(max_decimals):
        division_remaining.append("0")
    divisor = int(num_2)
    len_divisor = len(num_2)
    residue = "0"

    for i in range(len(division_remaining)):
        div_scope = division_remaining[i: i + len_divisor]
        div_scope.insert(0, residue)
        result = int("".join(div_scope)) // divisor

        update_log(results_obj, f"Division: {div_scope} / {divisor}")
        update_log(results_obj, f"""{"Can't do the " if result == 0 else ""}Division: {result}""")

        if result != 0:
            residue = str(int("".join(div_scope)) % divisor)
            update_log(results_obj, f"Residue: {residue}")
        else:
            residue = "".join(div_scope)

        results_obj["results"].append(result)

    results_obj["total"] = round(int("".join(num_1)) / divisor, max_decimals)

    return results_obj

if __name__ == "__main__":
    # num_div_1 = str(randint(10 ** 7, 10 ** 8))
    # num_div_2 = str(randint(1, 10))

    num_div_1 = "81274572"
    num_div_2 = "9"

    results = division_process(num_div_1, num_div_2)

    print(f"{num_div_1} / {num_div_2}")

    for key, val in results.items():
        if key == "log":
            for log in val:
                print(log)
        else:
            print(key, val)
