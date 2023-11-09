# esto va a ir del 1 al 9, y va a ir de 1 en uno incrementandose, si queremos ir de otro numero
# ponemos range(1,11,3) esto va a ir de 3 en 3
# for number in range(1,10):
#     print(number)
total = 0
for number in range(1, 101):
    total += number

print(total)