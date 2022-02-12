def gamma_epsilon():

    bitTable = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

    with open("input_day3.txt", mode="r") as file:

        for line in file.readlines():

            i = 0

            while i < 12:

                bitTable[i] += int(line[i])
                i += 1

        bitTable2 = []
        bitTable3 = []
        for item in bitTable:

            if item >= 500:
                item2 = 1
                item3 = 0
            else:
                item2 = 0
                item3 = 1

            bitTable2.append(item2)
            bitTable3.append(item3)

            gamma = ''.join(map(str, bitTable2))
            epsilon = ''.join(map(str, bitTable3))

            gamma = int(gamma, 2)
            epsilon = int(epsilon, 2)

        print(gamma * epsilon)