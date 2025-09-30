def to_csv(_list):
    file = open("data_1.csv", "w", encoding="utf-8", newline="")
    print(f"---bf---")
    for row in _list:
        write_row = ""
        for element in row:
            print(f"row cur: {row}")
            write_row += f"{element}, "
            file.write(write_row + "\n")
    file.close()


to_csv(["1", "2", "3", "4"])
