#circular rotation
list1=list(map(int,input().split()))
rotation=input("Enput number of rotation : ")
for i in range(int(rotation)):
  list1=[list1[-1]]+list1[:-1]
  print(f"After {i+1} rotation:",list1)
 '''
1 2 3 4 5 6 7 8 9
Enput number of rotation : 3
After 1 rotation: [9, 1, 2, 3, 4, 5, 6, 7, 8]
After 2 rotation: [8, 9, 1, 2, 3, 4, 5, 6, 7]
After 3 rotation: [7, 8, 9, 1, 2, 3, 4, 5, 6] 
'''
