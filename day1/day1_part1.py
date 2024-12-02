import re
def main():
    with open("day1/input.txt", "r") as file:
        lines = file.readlines()
        list1 = []
        list2 = []
        for line in lines:
            line = line.replace("\n", "")
            RE = re.compile(' +')
            line = re.sub(RE, " ", line)
            line = line.split(' ')
            list1.append(line[0])
            list2.append(line[1])
        list1 = sorted(list1)
        list2 = sorted(list2)
        
        distance = 0
        for i in range(max(len(list1), len(list2))):
            max_num = max(int(list1[i]), int(list2[i]))
            min_num = min(int(list1[i]), int(list2[i]))
            distance += max_num - min_num
        print(distance)
            
if __name__ == "__main__":
    main()
