def logananalyzer(path):
    keyword = ["error", "failed", "down"]
    count = {key : 0 for key in keyword}
    try:
        total = 0
        with open(path, "r") as file:
            for line in file:
                total += 1
                for key in keyword:
                    if key in line:
                        count[key] += 1
            for key,value in count.items():
                print(f"\n{key} : {value}")
    except FileNotFoundError:
        print("The file is not found")


if __name__ == "__main__":
    path = input("Can you please give me the path ").strip()
    logananalyzer(path)
