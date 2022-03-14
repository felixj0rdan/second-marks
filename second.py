# Big_O notation
# complexity => O(n+n)
# = O(n)

import csv

def main(LIST):
    LIST.sort(key=lambda x: x[1])
    names = LIST[-1]
    print("Topper in Maths "+names[0])
    LIST.sort(key=lambda x: x[2])
    names = LIST[-1]
    print("Topper in Biology "+names[0])
    LIST.sort(key=lambda x: x[3])
    names = LIST[-1]
    print("Topper in English "+names[0])
    LIST.sort(key=lambda x: x[4])
    names = LIST[-1]
    print("Topper in Physics "+names[0])
    LIST.sort(key=lambda x: x[5])
    names = LIST[-1]
    print("Topper in Chemistry "+names[0])
    LIST.sort(key=lambda x: x[6])
    names = LIST[-1]
    print("Topper in Hindi "+names[0])
    ARR = []
    for i in LIST:
        arr1 = []
        arr2 = int(i[1])+int(i[2])+int(i[3])+int(i[4])+int(i[5])+int(i[6])
        arr1.append(i[0])
        arr1.append(arr2)
        ARR.append(arr1)
    ARR.sort(key=lambda x: x[1])
    arr2 = []
    for i in ARR:
        arr2.append(i[0])
    print("Best student in the class are "+arr2[-1]+", "+arr2[-2]+", "+arr2[-3]+".")


LIST = []
with open('Marks.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        LIST.append(line)
main(LIST)

