#Python. HW_1

# 1) Создать переменную типа String -

variable_String='Phrase'
# 2) Создать переменную типа Integer

variable_Integer=1
# 3) Создать переменную типа Float
variable_Float=1.2
# 4) Создать переменную типа Bytes
variable_Bytes=bytes(10)
# 5) Создать переменную типа List
variable_List=[1,2,'word',3]

# 6) Создать переменную типа Tuple
variable_Tuple=('TEXT', )
# 7) Создать переменную типа Set
variable_Set={'a', 'b', 'c', 'd'}
# 8. Создать переменную типа Frozen set
variable_Frozen_set=frozenset({'a', 'b', 'c', 'd'})
# 9) Создать переменную типа Dict
variable_Dict = {1: "alpha", 2: "beta", 3: "omega"}
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(variable_String),variable_String)
print(type(variable_Integer),variable_Integer)
print(type(variable_Float),variable_Float)
print(type(variable_Bytes),variable_Bytes)
print(type(variable_List),variable_List)
print(type(variable_Tuple),variable_Tuple)
print(type(variable_Set),variable_Set)
print(type(variable_Frozen_set),variable_Frozen_set)
print(type(variable_Dict),variable_Dict)
#or
name_list_var = [variable_String, variable_Integer, variable_Float, variable_Bytes, variable_List, variable_Tuple,
                 variable_Set, variable_Frozen_set, variable_Dict]
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
variable_1 = 'All will be'
variable_2 = ' alright'
variable_3 = variable_1 + variable_2
print(variable_3)
# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
Integer_1=27
Integer_2=15
Integer_3=Integer_1+Integer_2
print(Integer_3)
# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
Integer_4=Integer_1/Integer_2
print(Integer_4)
# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
Integer_5=Integer_1*Integer_2
print(Integer_5)
# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
Integer_6=Integer_1//Integer_2
print(Integer_6)
# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
Integer_7=Integer_1 % Integer_2
print(Integer_7)
# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
Answer=(7 + 12)**3 + 7 * 4 - 44 / 2**4
print(Answer)
