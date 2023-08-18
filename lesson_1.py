# Программа реализует игру "Чехорда".
# Когда у пользователя запрашиваются различные данные
# и далее смешиваясь вся полученная информация выдается на консоль.
print("Здравствуйте, меня зовут Python!")
name = input("Как зовут вас? ")
print("Приятно познакомиться " + name + "! Вы являетесь моим создателем :)")
print("Давайте сыграем в игру 'Чехорда.'")
who = input("Кто? ")
with_whom = input('С кем? ')
where = input('Где? ')
when = input('Когда? ')
what_doing = input("Что делали? ")
what_were_they_told = input('Что им сказали? ')
how_did_it_end = input('Что все закончилось? ')
print(who + ' ' + with_whom + ' ' + where + ' ' + when + ' ' + what_doing + ' ' + what_were_they_told + ' ' + how_did_it_end)
