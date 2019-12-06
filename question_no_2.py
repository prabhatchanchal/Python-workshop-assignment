n=input()
candies=[]
for i in range(int(n)):
  candies.append(i)
minp=int(input())
count=1
dynamic_idx=checcking_idx=minp
candies[0]='p'
while candies[checcking_idx]!='p':
    if candies[dynamic_idx]=='p':
        break
    candies[dynamic_idx]='p'
    count+=1
    dynamic_idx=dynamic_idx+minp
    if dynamic_idx>len(candies):
        temp=(len(candies)-(dynamic_idx - minp))
        dynamic_idx=minp-temp
    if dynamic_idx==len(candies):
        dynamic_idx=0
    checcking_idx=dynamic_idx
print(count)
© 2019 GitHub, Inc.
