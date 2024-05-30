# isinstance - para saber se o objeto é de determinado tipo

lista = ['a',1,1.1,True,[0,1,2],(1,2),{0,1},{'nome': 'Amanda'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))
    
    # se é int ou float
    elif isinstance(item, (int,float)):
        print('Num')
        print(item, item * 2)
    else:
        print('outro')