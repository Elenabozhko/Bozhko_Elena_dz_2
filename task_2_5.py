"""Создать вручную список, содержащий цены на товары(10-20) """

prise = [57.8, 46.51, 97, 47.25, 55.41, 87.02, 88, 89.99, 93.02, 95, 94, 86.90]

# вывести цены через запятую в одну строку
for x in prise:
    r = int(x)
    kk = (x - r) * 100
    print(f'{r} руб {kk:02.0f} коп', end = ' , ' )


# # сортировка по возрастанию
# prise.sort()
# print(prise)
# for summa in prise: print(summa, end = ' , ')

# # на убывание
# prise_desc = sorted(prise,reverse=True)
# print(prise_desc)




