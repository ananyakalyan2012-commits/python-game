place_lst=['london',"paris","greece","amsterdam","dubai"]

#iterating list items
tot_items=len(place_lst)
print(f'Total items in place_lst={tot_items}\n')
for i in range(len(place_lst)):
    print(f'item at index {i}={place_lst[i]}')

#get index num for paticular item
print(f'\nplace_lst = {place_lst}\n')
i=place_lst.index("greece")
print(f'index no. of greece={i}')


fruit_lst=["apple","banana","strawberry","kiwi","lemon"]
print(f'item at index -ve 2 = {fruit_lst[-2]}\n')
print(f'item at index -ve 4 = {fruit_lst[-4]}\n')

#sorting the list
(fruit_lst.sort())
print(fruit_lst,"\n")

#reversing the list items
fruit_lst.reverse()
print(fruit_lst,"\n")

print(fruit_lst[0:3],"\n")
print(fruit_lst[0:4],"\n")
print(fruit_lst[1:4],"\n")

for i in range(len(fruit_lst)):
    print(fruit_lst[i])
    if fruit_lst[i]=="lemon":
        print(f'{fruit_lst[i]}-found it\n')
    else:
        print(f'{fruit_lst[i]}-not found\n')
