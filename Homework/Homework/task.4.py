import csv


def get_file():
    res = []
    try:
        with open("homework.csv", "r", encoding="utf8") as file:
            csv_reader = csv.reader(file)
            for i in csv_reader:
                for j in i:
                    res.append(j.replace(",", "."))


    except Exception as e:
        print(e)

    return res


print(get_file())


def get_number_only():
    res = get_file()
    try:
        with open("result.csv", "w", encoding="utf8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(res)
    except Exception as e:
        print(e)

    return ' '


print(get_number_only())