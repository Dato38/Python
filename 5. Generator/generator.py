'''Данная программа очень простая, она брет два случайных
слова из файла words.txt и комбинирует их
Зачем это нужно?
При комбинировании слов включается фантазия, позволяющая
представить какую вещь можно было бы создать, скомбинировав
два предмета или их свойства
Данный подход примняется в ТРИЗ для генерации идей, и
изобретений'''
import random#1 Импортируем библиотеку
mas=[]#2 создаем пустой список
f=open(u'words.txt', 'r')#3 Открываем файлы со словами (существит)
for x in f:#4 и в цикле
    mas.append(x.replace('\n',''))#5 добавляем их всех в массив, добавляя знак переноса строки
l=len(mas)-1#6 получаем длину этого массива
z=''
print('-----------------------------------------')
print('Генератор идей на основе случайного скрещивания предметов')#
print('-----------------------------------------')
print('Нажимайте Enter для генерации пар')#
print('\n')
while(z!='exit'):#7 и пока не напечатаем exit
    a=random.randint(0,l)#8 сгенерируем 2 случайных числа а
    b=random.randint(0,l)#8 и b с диапозоном от 0 до длина массива
    print(mas[a]+'-'+mas[b])# 9 и печатаем случайные строчки из файла words.txt после чего мы получаем различные комбинации случайных предметов
    z=input('')#        