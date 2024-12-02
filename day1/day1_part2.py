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
        
        hash_map = {}
        for item in list2:
            hash_map[item] = hash_map.get(item, 0) + 1
        print(hash_map)
        
        similarity = 0
        for item in list1:
            similarity += int(item) * hash_map.get(item, 0)
        print(similarity)
        
            
if __name__ == "__main__":
    main()
