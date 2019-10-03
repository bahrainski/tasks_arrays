print('Введите количество кеглей и брошенных шаров')
num_kegl=int(input())
num_bould=int(input())
bowling=[]
for i in range (num_kegl):
    bowling.append('I')
for i in range (num_bould):
    first_skittle=int(input())
    second_skittle=int(input())
    for k in range(first_skittle-1, second_skittle):
        bowling[k]='.'
print(bowling)