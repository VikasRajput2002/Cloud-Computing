import sys
cur_station = None
# station_count
# sum_temps

for line in sys.stdin:
    station_count = 0
    sum_temps = 0

    try:
        line = line.split('\t')
        station, temp = line[0], float(line[1])

        if station != cur_station:
            if cur_station != "":
                print("%s\t%s\t%s"%(cur_station, sum_temps, station_count))
            cur_station = station
            station_count = 1
            sum_temps = temp
        else:
            station_count += 1
            sum_temps += temp
    except:
        pass
        
print("%s\t%s\t%s"%(cur_station, sum_temps, station_count))