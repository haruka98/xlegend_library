class Table:
    version = ""
    columns = 0
    delimiter = ""
    content = []

    def __init__(self, file_name):
        with open(file_name, encoding="big5hkscs") as file:
            input = file.readlines()
            if input[0][0] == "|":
                self.delimiter = "|"
            elif "," in input[0]:
                self.delimiter = ","
            else:
                raise Exception("Can't read", file_name)
            if self.delimiter == ",":
                self.version = input[0].split(self.delimiter)[0]
                self.columns = int(input[0].split(self.delimiter)[1])
            else:
                self.version = input[0].split(self.delimiter)[1]
                self.columns = int(input[0].split(self.delimiter)[2])
            to_add = [""]
            counter_bars = 0
            for i in range(1, len(input)):
                if counter_bars == self.columns:
                    counter_bars = 0
                    to_add[0] = "".join(to_add[0].splitlines())
                    if len(to_add[0]) > 0:
                        self.content.append(to_add)
                    to_add = [""]
                for j in input[i].strip("\n"):
                    if j == self.delimiter:
                        counter_bars += 1
                        if counter_bars < self.columns:
                            to_add.append("")
                    else:
                        to_add[counter_bars] += j
                if counter_bars < self.columns:
                    to_add[counter_bars] += "\n"
            to_add[0] = "".join(to_add[0].splitlines())
            if len(to_add[0]) > 0:
                self.content.append(to_add)

    def write(self, file_name):
        with open(file_name, "w", encoding="big5hkscs") as file:
            if self.delimiter == ",":
                file.write(self.version + self.delimiter + str(self.columns) + self.delimiter + "\n")
            else:
                file.write(self.delimiter + self.version + self.delimiter + str(self.columns) + self.delimiter + "\n")
            for line in self.content:
                for i in range(self.columns):
                    file.write(str(line[i]))
                    file.write(self.delimiter)
                file.write("\n")
