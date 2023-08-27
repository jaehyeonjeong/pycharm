import psutil

cpu = psutil.cpu_freq()
print(cpu)  #CPU의 속도를 출력합니다.

cpu_core = psutil.cpu_count(logical=False)
print(cpu_core) #CPU의 물리코어 수를 출력합니다.

memory = psutil.virtual_memory()
print(memory) #메모리의 정보를 출력합니다.

disk = psutil.disk_partitions()
print(disk) #디스크의 정보를 출력합니다.

net = psutil.net_io_counters()
print(net) #네트워크를 통해 보내고 받은 데이터량을 출력합니다.