#Дано цілі n та m. Вивести на екран всі дільники числа m, взаємно прості з n.


while True:
    while True:
        try:
             n = int(input())
             m = int(input())
             break
        except ValueError:
            print("Ne mychay komp,vvedi number")



    list1=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            list1.append(i)



    for k in range (len(list1)):
        if n%list1[k]==0 and m%list1[k]==0:
            print(list1[k])


    exite = input('push 1 if you want to start razok')
    if exite =='1':
        continue
    break
