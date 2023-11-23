import csv
import datetime
import pickle
import tables

# print('--------------------------------------- print_table unit test start ---------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Исходные данные:')
# print(tbl.data, '\n')
# print('Итоговые данные:')
# tbl.print_table()
# print('--------------------------------------- print_table unit test over ---------------------------------------')

# print('------------------------------------ get_rows_by_number unit test start -------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Исходные данные:')
# tbl.print_table()
# print()
# print('Итоговые данные:')
# print(tbl.get_rows_by_number(2, 3))
# print('------------------------------------- get_rows_by_number unit test over -------------------------------------')

# print('------------------------------------- get_rows_by_index unit test start -------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Исходные данные:')
# tbl.print_table()
# print()
# print('Итоговые данные:')
# print(tbl.get_rows_by_index("Франция", "Италия"))
# print('------------------------------------- get_rows_by_index unit test over -------------------------------------')


# print('----------------------------------- set&get_column_types unit test start -----------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Исходные типы столбцов:')
# print(tbl.get_columns_types())
# print(tbl.get_columns_types(True))
# print('\n', end='')
# tbl.set_column_types({1: int, 2: str}, True)
# tbl.set_column_types({'Бюджет': float, "Континент": str})
# print('Итоговые типы столбцов:')
# print(tbl.get_columns_types())
# print(tbl.get_columns_types(True))
# print('----------------------------------- set&get_column_types unit test over ------------------------------------')

# print('--------------------------------------- get_values unit test start ---------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Исходные данные:')
# tbl.print_table()
# print()
# print('Итоговые данные:')
# print(tbl.get_values(2))
# print('--------------------------------------- get_values unit test over ---------------------------------------')

# print('--------------------------------------- get_value unit test start ---------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data1.txt')
# print('Исходные данные:')
# tbl.print_table()
# print()
# print('Итоговые данные:')
# print(tbl.get_value(2))
# print('--------------------------------------- get_value unit test over ---------------------------------------')

# print('--------------------------------------- set_values unit test start ---------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Исходные данные:')
# tbl.print_table()
# print('\n')
# tbl.set_values("Африка", "Америка", column="Континент")
# tbl.set_values(1234, 321, column=2)
# print('Итоговые данные:')
# tbl.print_table()
# print('--------------------------------------- set_values unit test over ---------------------------------------')

# print('--------------------------------------- set_value unit test start ---------------------------------------')
# tbl = tables.Table()
# tbl.load_table('data1.txt')
# print('Исходные данные:')
# tbl.print_table()
# print('\n', end='')
# tbl.set_value(1520, column=2)
# tbl.set_value('Германия')
# print('Итоговые данные:')
# tbl.print_table()
# print('--------------------------------------- set_value unit test over ---------------------------------------')

#              -------------------------------------------EXTRAS-----------------------------------------------
# print('--------------------------------- 4) load_table(autoSetUp) unit test start ----------------------------------')
# tbl = tables.Table()
# tbl.load_table('data.txt')
# print('Без дополнений:')
# print(tbl.get_columns_types(), '\n')
# tbl2 = tables.Table()
# tbl2.load_table('data.txt', autoSetUp=True)
# print('С дополнениями:')
# print(tbl2.get_columns_types())
# print('---------------------------------- 4) load_table(autoSetUp) unit test over ----------------------------------')

# print('--------------------------------- 5) datetime unit test start ----------------------------------')
# tbl = tables.Table()
# tbl.load_table('data2.txt', autoSetUp=True)
# print('Типы данных')
# print(tbl.get_columns_types(), '\n')
# tbl.print_table()
# print('---------------------------------- 5) datetime unit test over ----------------------------------')

# print('--------------------------------- 3) concat & split unit test start ----------------------------------')
# tbl1 = tables.Table()
# tbl1.load_table('firstHalfData.txt')
# tbl1.print_table()
# print('\n')
# tbl2 = tables.Table()
# tbl2.load_table('secondHalfData.txt')
# tbl2.print_table()
# print('\n')
# tables.concat(tbl1, tbl2)
# tbl1.print_table()
# print("----- concat test over -----" + '\n')
# tbl3 = tables.Table()
# tbl3.load_table('dataToSplit.txt')
# tbl3.print_table()
# print()
# newT1, newT2 = tbl3.splitTable(3)
# print(newT1)
# print(newT2)
# print('---------------------------------- 3) concat & split unit test over ----------------------------------')

print('--------------------------------- 1, 2) multy load/save unit test start ----------------------------------')
testTable = tables.Table()
testTable.load_table('part1.csv')
testTable.print_table()
print()
tbl1 = tables.Table()
tbl1.load_table('part1.csv', 'part2.csv', 'part3.csv')
tbl1.print_table()
print()
# tbl1.save_table("savedPart1")

print('---------------------------------- 1, 2) multy load/save unit test over ----------------------------------')