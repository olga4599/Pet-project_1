per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000

deposit = []
first_bank = int(money * per_cent['ТКБ'] / 100)
second_bank = int(money * per_cent['СКБ'] / 100)
third_bank = int(money * per_cent['ВТБ'] / 100)
forth_bank = int(money * per_cent['СБЕР'] / 100)

deposit = [first_bank, second_bank, third_bank, forth_bank]

print(deposit)

max_deposit=max(deposit)
print('Максимальная сумма, которую вы можете заработать: ', max_deposit)