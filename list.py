# create a list
frnd_lst = ["harini","tanvi","natalia","jessica","sri","tanvi"]
print(f' Friend list = {frnd_lst}\n')

# total items in a list
print(f'No. of items  = {len(frnd_lst)}\n')

#to check no of times item (tanvi) appears in list
print(f'no of times tanvi occurs = {frnd_lst.count("tanvi")}\n')

# add item. using append() only one iten can be added at a time
frnd_lst.append("aditi")
print(f' Friend list = {frnd_lst}\n')

#deleting an item from a list
frnd_lst.remove("tanvi")
print(f' Friend list = {frnd_lst}\n')

#deleting an item using pop()uses index to delete item
frnd_lst.pop() #no idex will remove last item
print(f' Friend list = {frnd_lst}\n')
