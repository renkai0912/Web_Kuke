import csv

class Read_csv:
    @staticmethod
    def read_user():
        with open('D:\python\Web_kuke\csv\\username.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = []
            for row in reader:
                data.append(tuple(row))
                # print(data)
                return data
# a=Read_csv
# a.read_user()




