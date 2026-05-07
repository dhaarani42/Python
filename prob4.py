if __name__ == '__main__':
    sc=[]
    ml=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst=[]
        lst.append(name)
        lst.append(score)
        ml.append(lst)
        sc.append(score)
        lst=None
    sc.sort()
    ml.sort()
    sec=sc[1]
    for i in ml:
        if sec==i[1]:
            print(i[0])
            
