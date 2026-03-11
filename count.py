def m(count):
    c=0
    l=[]
    for word in count:
        if len('word')>1 and word[0] == word[-1]:
            c+=1
            l.append(word)
    print("List of words with first and last character same: ", l)
    return c
k=m(['2212', 'helh', '8888', 'fnfirfrihfbh', 'fjnrpijf'])
print("number of words with first and last character same: ", k)
