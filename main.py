from Dataset_creation import create_data
from Training import train
from Recognition import recognize
n = int(input("How many faces do you want to register?"))
data = {}
for i in range(n):
    id = input("Enter id ")
    name = input("Enter name ")
    create_data(id,name)
    data[id] = name
train()
recognize(data)
