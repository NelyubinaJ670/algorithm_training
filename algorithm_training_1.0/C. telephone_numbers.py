""" 
Телефонные номера в адресной книге мобильного телефона имеют один из следующих 
форматов: +7<код><номер>, 8<код><номер>, <номер>, где <номер> — это семь цифр, 
а <код> — это три цифры или три цифры в круглых скобках. Если код не указан, 
то считается, что он равен 495. Кроме того, в записи телефонного номера может 
стоять знак “-” между любыми двумя цифрами (см. пример). На данный момент в 
адресной книге телефона Васи записано всего три телефонных номера, и он хочет 
записать туда еще один. Но он не может понять, не записан ли уже такой номер
в телефонной книге. Помогите ему! Два телефонных номера совпадают, если у них 
равны коды и равны номера. Например, +7(916)0123456 и 89160123456 — это один 
и тот же номер.

Формат ввода
В первой строке входных данных записан номер телефона, который Вася хочет 
добавить в адресную книгу своего телефона. В следующих трех строках записаны 
три номера телефонов, которые уже находятся в адресной книге телефона Васи. 
Гарантируется, что каждая из записей соответствует одному из 
трех приведенных в условии форматов.

Формат вывода
Для каждого телефонного номера в адресной книге выведите YES (заглавными буквами), 
если он совпадает с тем телефонным номером, который Вася хочет добавить 
в адресную книгу или NO (заглавными буквами) в противном случае.

Пример 1

Ввод	            Вывод
8(495)430-23-97
+7-4-9-5-43-023-97  YES
4-3-0-2-3-9-7       YES
8-495-430           NO

Пример 2

Ввод	            Вывод
86406361642
83341994118         NO
86406361642         YES
83341994118         NO

Пример 3

Ввод	            Вывод
+78047952807
+78047952807        YES
+76147514928        NO
88047952807         YES

"""

y = input().replace('(', '').replace(')', '').replace('-', '')
x = input().replace('(', '').replace(')', '').replace('-', '')

print(x)


def general_form():
    "Привожу к единому виду и кол-ву цифр в номере."
    if len(x) == 11:
        x[0] = '8'
    if len(x) == 7:
        x[:0] = ['8', *'495']



for i in x:
    if 


def input_number():
    "Ввод данных."
    new_number = input().replace('(', '').replace(')', '').replace('-', '')
    numbers = []
    old_number = input().replace('(', '').replace(')', '').replace('-', '')