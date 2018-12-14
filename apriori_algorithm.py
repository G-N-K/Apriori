def dataset():

    data=[['m','o','n','k','e','y'],['d','o','n','k','e','y'],['m','a','k','e'],['m','u','c','k','y'],['c','o','o','k','e'],['n','a','v','e','e','n']]
    s=set([])

    for i in range(len(data)):

        for j in range(len(data[i])):
            s=s|set(data[i][j])
    s=list(s)

    for i in range(len(s)):
        s[i]=frozenset(s[i])

    return tuple(s),data

def frequency_of_items(data,s):
    count=[]
    for i in range(len(s)):
        c=0
        for j in range(len(data)):
            if s[i].issubset(data[j]):
                c+=1
        count.append(c)
    return count
def supp_list(count,itemset,sup):
    new=[]
    for i in range(len(count)):
        if count[i]>sup:
            new.append(itemset[i])
    if len(new)==1:
        return tuple(new)

    new1=[]
    for i in range(len(new)-1):
        for j in range(i+1,len(new)):
            c=new[i].union(new[j])
            new1.append(c)
    new1=set(new1)

    return tuple(new1)

#done with finding frequent items
def combinations(length,x,combo=[]):
    if len(x)==length:
        if x not in combo:
            combo.append(x)
            combo.sort()
        return combo
    else:
        for i in range(len(x)):
            red=x[:i]+x[i+1:]
            combo=combinations(length,red,combo)
    return combo
def support1(x,confidence,itemset):

    length=len(x)

    key=list(itemset.keys())[length-1]

    values=itemset[key]

    list_keys=[sorted(i) for i in (list(map(list,key)))]
    x=sorted(x)
    index=list_keys.index(x)

    return 3/values[index]
def main():
    s,data=dataset()
    min_support=2
    min_confidence=0.7
    intial=s
    itemset={}
    while len(s)>=1:
        itemset[s]=frequency_of_items(data,s)
        j=0
        for i in itemset[s]:
            if i>min_support:
                j=1
        if j==0:
            del(itemset[s])
            break
        elif len(itemset[s])==1:
            if itemset[s][0]>=min_support:
                break
            else:
                del(itemset[s])
                break
        s=supp_list(itemset[s],s,min_support)

    if intial==s:
        print('there are no frquent items for given support value')
    else:
        s=list(map(list,s))[0]

        print('the frequent items are',s)
        dlt=set([])

        for i in range(len(s)-1,0,-1):

            list_x=combinations(i,s,combo=[])
            for i in list_x:
                if set(i).issubset(dlt):
                    continue
                else:
                    support=support1(i,min_confidence,itemset)
                    if support>min_confidence:
                        not_in=[]
                        for j in s:
                            if j not in i:
                                not_in.extend(j)
                        print(i,'-->',not_in)

                    else:
                        dlt.union(set(i))
    return

main()



