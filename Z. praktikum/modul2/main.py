def createQueue():
    q = []
    return q


def enqueue(q, data):
    q.insert(0, data)
    return q


def dequeue(q):
    return q.pop()


def size(q):
    return len(q)


def isEmpty(q):
    return q == []


def CPU_Scheduling():
    taskQueue = createQueue()
    temp = []
    amount = int(input("Jumlah proses yang akan dijadwalkan di CPU = "))
    for i in range(amount):
        name = input(f"Nama Proses ke-{i} : ")
        time = int(input("Waktu Proses : "))
        temp.append(name)
        temp.append(time)
        enqueue(taskQueue, temp)
        temp = []
    print()
    print(f"Antrian Proses : ")
    print(taskQueue)
    CPUTime = int(input("\nwaktu proses CPU = "))
    print(f"antrian proses beserta waktunya : {taskQueue}")

    i = 1
    while not isEmpty(taskQueue):
        print(f"Iterasi ke-{i} :")
        i += 1
        temp = []
        task = dequeue(taskQueue)
        sisa = task[1] - CPUTime
        temp.append(task[0])
        temp.append(sisa)
        if temp[1] > 0 and temp[1] != 0:
            enqueue(taskQueue, temp)
            print(
                f"     proses {task[0]} sedang diproses, dan sisa waktu proses {task[0]} = {sisa}"
            )
        elif temp[1] <= 0:
            print(f"     Proses {task[0]} telah selesai diproses")
        print(f"     Data proses yang tersisa : {taskQueue}")
        temp = []


CPU_Scheduling()
