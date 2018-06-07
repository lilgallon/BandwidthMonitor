import psutil
import time

iostat = psutil.net_io_counters(pernic=False)
last_up_mib = iostat[0]/ (2**20)
last_down_mib = iostat[1]/ (2**20)

while True:
    time.sleep(1)

    iostat = psutil.net_io_counters(pernic=False)
    current_up_mib = iostat[0]/ (2**20)
    current_down_mib = iostat[1]/ (2**20)

    print(current_down_mib)

    up_speed = current_up_mib - last_up_mib
    down_speed = current_down_mib - last_down_mib
 
    print('Up speed: ' + str(up_speed) + ' MiB')
    print('Down speed: ' + str(down_speed) + ' MiB')

    last_up_mib = current_up_mib
    last_down_mib = current_down_mib
