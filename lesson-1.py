

"""""
#Задание№1
a = 5
b = 10
print(a,b)
y = int(input("Введите число: "))
print(y)
x = input("Введите ваше имя:")
print(x)


#Задание№2
time = int(input("Введите время в секундах: "))
hours = time//3600
print(hours)
minutes = (time - hours*3600)//60
print(minutes)
seconds = time - hours*3600 - minutes*60
print(seconds)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

#Задание№3
n = int(input("Введите число : "))
sum = n + n*11 + n*111
print("Сумма чисел n + nn + nnn - %d" %sum)


#Задание№4
n = int(input("Введите целое положительное число "))
max = n % 10

while n >= 1:
    n = n // 10
    
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break


#Задание№5
income = int(input("Введите выручку: "))
taxes = int(input("Введите расходы: "))
if income > taxes :
    prib = income - taxes
    print("Прибыль равна -", prib)
else:
    ubit = taxes - income
    print("Убыток равен -", ubit)
if prib > 0 :
    rent = prib/income
    print("Рентабельность составила: ", rent)
pers = int(input("Введите число сотрудников: "))
pers_prib = prib/pers
print("Прибыль на одного сотрудника составила: ", pers_prib)


#Задание№6
a = int(input("a = "))
b = int(input("b = "))
i = 1
while a < b :

    print(i,"-ый день :",a)
    a = a + a * 0.1
    i = i + 1

print("Ответ: на", i, "день спортсмен достиг результата не менее", b, "км")
"""""

