#test=10
#print("МНЕ " +str(test) + " ЛЕТ")

# Простые операции

#print((1+3)**2)
#print(7%(5//2))

#  Работа со строками

#name=input("kak vas zovut?  ")
#print("Vas zovut "+name)
#Калькулятор
#a=input('Vvedite pervoiye chislo: ')
#b=input('Vveidte vtoroiye chislo: ')
#print(int(a)+int(b))
#print('privet'*4)
#count=input("skolko raz umnojit? ")
#print(name*int(count))
#print(4*'2')

#Типы данных, переменные

#print(int("3"+"4"))
#print(float("210"*int("2")))
#spam=2
#eggs=3
#del spam
#eggs=4
#spam=5
#print(spam*eggs)
#x='Test'
#x*=3
#print(x)

#Управляющие структуры

#print("test">"Tesf")
#pogoda="DOJDI"
#time="Noch"
#if pogoda=="ZIMA":
#	print("Seichas ochen holodno")
#	if time=="Noch":
#		print("A eshe seichas noch")
#	elif time=="Utro":
#		print("Ti zavtrakal hot???")
#	else:
#		print("seichas konechno svetlo, no ochen holodno")
#if pogoda=="DOJDI":
#	print("Seichas Dojd")
#vvedite pravilni parol
#parol=input("Vvedi parol: ")
#if parol== '123':
#	print("vi vveli pravilni parol")
#else:
#	print("vi vveli nepravilni parol, dostup zapreshen")

# Множественные условия, приоритетность операторов

#pogoda="DOJD"
#time="Hoch"
#if pogoda=="DOJD" and (time=="Noch" or time=="Vecher"):
#	print("Kakaiya-to stroka")
#if not pogoda=="Zima":
#	print("Chto-to")
#if not True:
#	print("1")
#elif not(1+1==3):
#	print("2")
#else:
#	print("3")	

# Циклы

#i=1
#while i<=5:
#	print(i)
#	i=i+1
#j=1
#while 1==1:
#	print("privet "+str(j))
#	j+=1
#	if j==10001:
#		break
# Четное число
#number=0
#while number<=1000:
#	number+=1
#	if(number%2)!=0:
#		continue;
#	print("Chetnoie chislo: " + str(number))

# Списки

#test=[1,2,3,4, 5, 7, 8, 1, 4, 6]
#print(test+[7,8,9])
#print("v massive:  "+str(len(test)))
#print(max(test))
#print(test.count(4))
#test. reverse()
#print(test)
#text="Privet"
#print(text[2])
#txt=['David',  'Max', 'Kate']
#if 'Anna' in txt:
#	print('Anna zdes')
#if 'Anna' not in txt:
#	print('Anna ne zdes')
#words=["Hello"]
#words. append("world")
#print(words[1])
#nums=[9, 8, 7, 6, 5]
#nums.append(4)
#nums.insert(2, 11)
#print(len(nums))

# Диапозоны, обход списков

#Только четные числа  если получить
#numbers=list(range(0, 101, 2))
#print(numbers)
#nums=list(range(3, 15, 3))
#print(nums[2])
#numb=[1,2,3,4,5]
#i=0
#length=len(numb)-1
#while i<=length:
#	print(str(numb[i])+'!')
#	i+=1
#for element in numb:
#	print(str(numb))
#for test in range(15):
#	print("privet")
#list=[1, 1, 2, 3, 5, 8, 13]
#print(list[list[4]])
#Разберём [list  [4] это число 5 можете проверить
#А теперь заменим [list  [4] на 5 получается print ( list [ 5 ] )

#Свои функции

#def print_spam():
#	print('spam')
#	print('spam')
#	print('spam')
#print_spam()
#def multiply(number):
#	print(number*2)
#multiply(5)
#def max(x,y):
#	if x>y:
#		return x
#	else:
#		return y
#x=float(input("Chislo 1: "))
#y=float(input("Chislo 2: "))
#print(max(x,y))

# Комментарии, docstring

#def privet():
#	''' Описание функции'''
#	print('Hello wold '+name+'!')
#print(privet.__doc__)
#def read_name():
#	return ':::' +input('Vvedite vashe imiya: ')+':::'
#print(read_name())
#def shout(word):
#	return word+'!'
#speak=shout
#output=speak('shout')
#print(output)

#  Модули, рандом, SDL

#import random
#import math
#from random import randint
#from math import *
#print(random.randint(1,100))
#for i in range(19):
#	print(random.randint(5,100))
#num=10
#print(math.sqrt(num))	
#print(randint(1,10))
#from math import sqrt as my_sqrt, pi
#print(my_sqrt(25))

# Используем PyPi

# Введения в исключения

#ImportError
#IndexError
#NameError
#SyntsxError
#TypeError
#print("test"+5)
#ValueError
#try:
#	print(7/0)
	#eval("print(7/4)a")
#except (ZeroDivisionError,  NameError):
#except ZeroDivisionError:
	#pass
	#print("Poimano iskliucheniye DeleniyePoNuliyu")
#except SyntaxError:
#	print("Poimano iskliucheniye SintaksicheskaiyaOshibka")
#except:
#	print("Poimano iskliucheniye ..kakoie to")
#finally:
#	print('Konec poimki')
#print("Programma Zavershena! ")
#try:
#	pogoda='Plohaiya'
#	if pogoda=='Plohaiya':
#		raise TypeError('TEST')
#except TypeError:
#	print ("Poimano isklucheniye TypeError")
#class HowdyHoError(Exception):
#	pass
#raise HowdyHoError('TEST')

# Работа с файлами, assert, len, with

#def exc(text):
#	assert text != ' '
#	print(str(text)+'!')
#exc(' ')
#def test(number):
#	assert number>0, " Number > 0"
#	print(str(number))
#test(-10)
#r, w, a, b
#file=open('test.txt', 'r')
#print(file.read())
#file.close()
#
#filename=input("Ukajite file: ")
#file=open(filename, 'r')
#print(file.read())
#print(len(file.read()))
#file.close()
#
#file=open('test.txt', 'w')
#file.write('Priver, Mir')
#file.close()
#
#filename=input('Vvedite jelaemoe imiya file: ')
#text=input('Kakoi text hotite pomestit v file: ')
#file=open(filename, 'w')
#file.write(text)
#file.close()
#
#file=open('test.txt', 'r')
#print(file.read(6))
#print(file.read(3))
#print(file.read(1024*100))
#file.close()
#
#file=open('test.txt', 'a')
#file.read(' TEST')
#file.close()
#
#file=open("somefile.txt", "r")
#for i in range(21):
#	print(file.read(8))
#file.close()
#Программа для копирования файлов
#filename1=input('Kakoi file zabekapit? ')
#filename2='backup_'+filename1
#file1=open(filename1, 'rb')
#file2=open(filename2, 'w'b)
#file2.write(file1.read())
#file1.close()
#file2.close()
#print('kopirovanie uspeshno zaversheno!')
#
#file=open('test.txt', 'r')
#strings=file.readlines()
#for string in strings:
#	print(strings)
#file.close()
#print('kopirovanie uspeshno zaversheno!')
#
#with open('test.txt', 'r') as f:
#	print(f.read())
#print('kopirovanie uspeshno zaversheno!')

# Новые типы данных None Dictionary

#foo=print()
#if foo==None:
#	print(1)
#else:
#	print(2)
#
#test={
#	"kluch1":"znach1", 
#	"kluch2":"znach2",
#	"kluch3":false, 
#	"kluch4":{
#		"vloj kluch1":"vloj znach1"
#	}
#}
#print(test["kluch1"])
#
#primes={1:2, 2:3, 4:7, 7:17}
#print(primes[primes[4]])
#
#contacts={
#	"Andreiy":"899036",
#	 "Nitita":"546547657", 
#	 "Dasha":"47657567567"
#}
#testing=input('kogo ishem? ')
#if testing in contacts:
#	print('Kontack naiden: '+contacts[testing])
#else:
#	print('kontackt ne naiden! ')
#print(contacts.get("Andreiy", "Nomer ne naiden"))
#
#fib={1:1, 2:1, 3:2, 4:3}
#print(fib.get(4, 0)+fib.get(7.5))

# Комментирование, pass, кортежи

#'''mogostrochni kommentari'''
#def main():
#	pass
#print("test")
#
#digits= 1,2,3,4,5,6
#names=("John", "James", "Jack")
#print(names[0])
#tuple=(1, (1, 2,3))
#print(tuple[1])

# Срез списка

#digits=[1,2,3,4,5,6,7,8,9,10]
#digits2=digits[2:5]
#digits2=digits[:3]
#digits2=digits[::2]
#digits2=digits[-3]
#digits2=digits[::-1]
#print(digits2)
#sqs=[0,1,4,9,16,25,36,49,64]
#print(sqs[4:7])
#digits2=range(2,101)[::2]
#for i in digits2
#	print(i)
#sqs=0, 1 , 4, 9, 16, 25, 36, 49, 64, 81
#print(sqs[7:5:-1]) 

# Форматирование строк

#%s, %d, %f
#person_name='Djessi'
#age=21
#print('privet, %s!\nTebe uje %d god' % (name=person_name, age))
#print('Privet, {0}!\nTebe uje {1} god'.format(name, age))
#print('{0}{1}{0}'.format('abra', 'cad'))
#human={
#	'name': 'Jessy', 
#	'age':21
#}
#print('Imya: {person[name]}\n Vozrast: {person[age]}'. format(person=human))
#
#input_str='Jessy'
#^, <, >
#print('{0:*^10}'.format(input_str))
#length=10
#if(len(input_str)%2):
#	length+=1
#print(('{0:*^'+str(length)+'}').format(input_str))

# Функции для работы со строками и числами

#fruits=['Limoni', 'Yabloki', 'Kivi', 'Ananas', 'Klubnika']
#members='James, Jonny, Jack, John'
#print(' - '.join(fruits))
#print('Privet, Petr '.replace('Petr', 'Aleksandr'))
#name=input('vashe imya: ')
#if(name.startswith('А')):
#if(name.lower().startswith('а') or name.lower().startswith('a')):
#	print('начинается с буквы А')
#else:
#	print('добропожаловать')
#input_str=input('Vvedite hot chtonit: ')
#print(input_str.lower())
#word='Helloing'
#if(word.endswith('ing')):
#	print('Hello ING')
#else:
#	print('WTF?')
#print(min([5, 10, 5, 7, 2,1]))
#print(abs(-1000))
#print(sum([2,3, 5,7]))
#print(members.split(','))