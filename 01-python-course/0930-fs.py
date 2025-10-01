import csv


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

"--------------------------------------"


# 인코딩 타입을 정확히 작성해야 글자 등이 안깨짐
def to_csv_2(_list):
    file = open(
        "data_2.csv",
        "w",
        newline="",
        encoding="utf-8",
    )
    csvfile = csv.writer(file)
    for row in _list:
        csvfile.writerow(row)
        # to_csv(['1', '2', '3', '4'])


to_csv_2([["1", "2"], ["3", "4"]])
