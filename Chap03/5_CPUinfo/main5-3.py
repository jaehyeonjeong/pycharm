import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1) #CPU의 사용량을 1초동안의 평균값을 구합니다.
    #interval의 시간을 조절하여 평균을 구하는 시간을 조절할 수 있습니다. 이 줄에서 1초동안 측정한 후 다음 줄로 이동합니다.
    print(f'CPU사용량: {cpu_p}%') #CPU의 사용량을 출력합니다.

    memory = psutil.virtual_memory() #사용가능한 메모리를 출력합니다.
    memory_avail = round(memory.available/1024**3, 1)
    print(f'사용 가능한 메모리: {memory_avail}GB')

    net = psutil.net_io_counters() #네트워크에서 보내고 받은 크기를 출력합니다.
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent, 1) #현재(curr_sent)측정한 값에서 이전에(prev_sent)측정한 값을 빼면 1초 동안 보내는 데이터를 구할 수 있습니다.
    recv = round(curr_recv-prev_sent, 1) #현재(curr_recv)측정한 값에서 이전에(prev_recv)측정한 값을 빼면 1초 동안 받은 데이터를 구할 수 있습니다.

    print(f'보내기: {sent}MB 받기: {recv}MB') #1초 동안 보내고 받은 데이터를 출력합니다.

    prev_sent = curr_sent
    prev_recv = curr_recv
    #이전의 값에 현재 값을 바인딩합니다. 이전의 값을 가지고 있어야 현재값과 비교하여 1초동안 얼마를
    #보내었는지 계산을 할 수 있기 때문입니다.
