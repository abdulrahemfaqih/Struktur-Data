import os
os.system('cls')

data = {
    "A": [1, 2, 3, 4],
    "B": [],
    "C": []
}

def display(data):
    for key, value in data.items():
        print(f'{key}:')
        for item in value:
            print(f'|{item}|')

def move(asal, destinasi):
    disk = data[asal].pop(0)
    data[destinasi].insert(0, disk)

def towers(n, asal, bantuan, destinasi):
    if n == 1:
        print(f'Memindahkan lempengan 1 dari {asal} ke {destinasi}')
        move(asal, destinasi)
        display(data)
    else:
        towers(n - 1, asal, destinasi, bantuan)
        print(f'Memindahkan lempengan {n} dari {asal} ke {destinasi}')
        move(asal, destinasi)
        display(data)
        towers(n - 1, bantuan, asal, destinasi)

print('Pemindahan 4 lempengan dari A ke C dengan bantuan B')
display(data)
towers(4, 'A', 'B', 'C')



