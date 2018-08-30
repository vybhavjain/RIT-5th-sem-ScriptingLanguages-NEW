def cus_rec(i,lis):
    if i==len(lis)-1:
        return lis[i]
    else:
        from_future=cus_rec(i+1,lis)
        return  lis[i] if lis[i]>from_future else from_future

print(cus_rec(0,[int(input('Please enter {} the number'.format(i+1))) for i in range(5)]))
