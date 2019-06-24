def print_everything(**kwargs):
  i=0
  for key, thing in kwargs.items():
    print(f"{i}. {key} : {thing}")
    i+=1

print_everything(first='apple',second ='banana', third = 'cabbage',fourth='orange')
