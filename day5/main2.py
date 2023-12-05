# must add a newline to the end of the input file to work

def getSeeds(line):
    nums = line.split(': ')[1]
    nums = (nums.split(' '))
    return list(nums)

def mapData(destination, source, ranges, map):
    data_range = range(source, source + ranges)
    map[data_range] = destination
    return map

def initializeMaps(lines):
    all_maps = []
    for i in range(7):
        all_maps.append(dict())
    return all_maps

def getNewVal(key, mymap):
    for range_obj, v in mymap.items():
        if key in range_obj:
            return v + (key-range_obj.start)
    return key

def main():
    with open("input2.txt", 'r') as f:
        lines = f.readlines()
        seeds = getSeeds(lines[0].rstrip())
        all_maps = initializeMaps(lines)
        map = -1
        for line in lines[2:]:
            if "map" in line: # looking at a new map
                map += 1
                continue
            if line != "\n": # time to map
                line = line[:len(line)-1]
                nums = line.split(" ")
                dest = int(nums[0])
                src = int(nums[1])
                ran = int(nums[2])
            
                mapData(dest, src, ran, all_maps[map])
        # trying to find location
    # locations = []
    location = float('INF')
    count = 0
    for seed in seeds:
        if count%2 == 0:
            value = int(seed)
            count += 1
            continue
        for x in range(int(seed)):
            value += 1 # test all seeds in the range
            new_value = value
            for i in range(len(all_maps)):
                new_value = getNewVal(new_value, all_maps[i])
                # print(value)
                # print("seed: ", value+x, "new: ", new_value)
            if int(new_value) < location:
                location = new_value
        count += 1
    print(location)
        
        # seed_to_soil = all_maps[0]
        # soil_to_fert = all_maps[1]
        # fert_to_wat = all_maps[2]
        # wat_to_light = all_maps[3]
        # light_to_temp = all_maps[4]
        # temp_to_hum = all_maps[5]
        # hum_to_loc = all_maps[6]

if __name__ == "__main__":
    main()
