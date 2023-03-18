def MergeString(s,t):
    r=""
    for i in range(min(len(s),len(t))):
       r=r+s[i]+t[i]
    return r+t[len(t)-len(s)+1:len(t)]
print(MergeString("abc","defgh"))
