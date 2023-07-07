import os
from QueueProgram import *

os.system("cls")

def CPU_Scheduling():
    taskQueue = createQueue()
    temp = []
    amount = int(input("Jumlah proses yang akan dijadwalkan di CPU = "))
    for i in range(amount):
        name = input(f"Nama Proses ke-{i+1} : ")
        time = int(input('Waktu Proses : '))
        temp.append(name)
        temp.append(time)
        enqueue(taskQueue, temp)
        temp = []
    print()
    print(f'Antrian Proses : ')
    print(taskQueue)
    CPUTime = int(input("waktu proses CPU = "))
    print(f"antrian proses beserta waktunya : {taskQueue}")
    
    i = 1
    while not isEmpty(taskQueue): 
        print(f'Iterasi ke-{i}')
        i += 1
        remainTime = []
        task = dequeue(taskQueue)
        sisa = task[1] - CPUTime
        remainTime.append(task[0])
        remainTime.append(sisa)
        if remainTime[1] > 0 and remainTime[1] !=0:
            enqueue(taskQueue,remainTime)
            print(f'    proses {task[0]} sedang diproses, dan sisa waktu proses {task[0]} = {sisa}')
        elif remainTime[1] <= 0:
            print(f'   Proses {task[0]} selesai')
        print(f'    Data proses yang tersisa : {taskQueue}')
        remainTime = []





# CPUScheduling()

q = createQueue()
a = []
jumlah = int(input("Masukkan proses dalam CPU : "))
for i in range(jumlah):
    nama = input(f"Nama Proses {i} = ")
    waktu = int(input("Waktu proses : "))
    a.append(nama)
    a.append(waktu)
    enqueue(q,a)
    a = []
print()
waktu_proses = int(input("Waktu proses CPU : "))
print(q)
i = 1
while not isEmpty(q):
    print("Iterasi ke-"+str(i))
    i+=1
    b=[]
    item=dequeue(q)
    sisa=item[1]-waktu_proses
    b.append(item[0])
    b.append(sisa)
    if b[1]>0 and b[1]!=0:
        enqueue(q,b)
        print(f'proses {item[0]} sedang diproses, dan sisa proses {item[0]} = {sisa}')
    elif b[1] <= 0:
        print(" Proses "+str(item[0])+" selesai")
    print(" Data proses yang tersisa="+str(q))
    b = []

       
        
