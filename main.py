import matplotlib.pyplot as plt
# init val
cumulative = 0
maxi = 0
mini = 0
maxiNum = 0
miniNum = 0
steps = []

# get start and end input
start = int(input("Start: "))
end = int(input("End: "))

# make sure they are positive integers
while start <= 0 or end <= 0:
    print("Please enter valid inputs...")
    start = int(input("Start: "))
    end = int(input("End: "))

# save size of the data set
size = (end - start + 1)

# print title
print("Num \tRes \tCum")

# main loop
for i in range(start, end + 1):

    # init values or second loop
    j = i
    done = False
    counter = 0

    # second loop
    while not done:

        # collatz compute
        if j % 2 == 0:
            j /= 2
        else:
            j = (j * 3) + 1

        # increment counters
        counter += 1
        cumulative += 1

        # target reached
        if j == 1:

            # set flag
            done = True

            # add data to a list
            steps.append(counter)

            # set maximum
            if counter > maxi:
                maxi = counter
                maxiNum = i
            # set minimum
            if i == start:
                mini = counter
                miniNum = i
            elif counter < mini:
                mini = counter
                miniNum = i

    # print the individual number
    print(str(i) + "\t--\t" + str(counter) + "\t--\t" + str(cumulative))

# report stats
print("\n== REPORT ==")
print("MAX: " + str(maxiNum) + " required " + str(maxi) + " steps to compute.")
print("MIN: " + str(miniNum) + " required " + str(mini) + " steps to compute.")
print("AVG: " + "The average number of steps was: " + str(cumulative / size))

# init plot
dataRange = []

for i in range(1, size + 1):
    dataRange.append(i)

plt.plot(dataRange, steps)
plt.show()

# partitioned average report
pivot = 0
avgList = []
indexList = []

# get part size from user
pivot = int(input("\nEnter partition size: "))

# loop to be able to partite same data set
while pivot != -1:
    # divide steps into parts that have pivot number of elements each
    new_size = size - (size % pivot)
    parts = int(new_size / pivot)
    index = 0

    # loop for every single part
    for i in range(0, parts):
        part_sum = 0
        end_index = index + pivot

        # loop for every single element in the current part to find avg
        for j in range(index,  end_index):
            part_sum += steps[j]

        # calculate average
        new_avg = part_sum / pivot
        avgList.append(new_avg)
        indexList.append(index)

        # report
        print("Average of index (" + str(index) + "," + str(index + pivot) + ") is " + str(new_avg))

        # increment index by pivot to point to new part
        index += pivot

    plt.clf()
    plt.plot(indexList, avgList)
    plt.show()

    # get part size from user
    pivot = int(input("\nEnter partition size: "))
