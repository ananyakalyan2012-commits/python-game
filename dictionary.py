#creating a dictionary
sample_dict={"name":"ananya","age":14,"state":"georgia",}
print(f'\ndict = {sample_dict}\n')

#total number of items in a dictionary
print(f' no. of items in sample dictionary ={len(sample_dict)}\n')

#to get the keys list only
print(f'keys = {sample_dict.keys()}\n')

#to get the values list only
print(f'values = {sample_dict.values()}\n')

#get the keys and values both using the for loop
for key in sample_dict.keys():
    print(key,sample_dict[key])
print("\n")

#to check if a key exist in a dictionary or not
if "country" in sample_dict:
    print(sample_dict["country"],"\n")
else:
    print("key does not exist \n")

# add a key-value pair into dictionary
sample_dict["city"]="atlanta"
print(sample_dict)

#delete a key-value pair
del(sample_dict["state"],)
print("\n",sample_dict)

#change the value of a dictionary
sample_dict["city"]="cumming"
print("\n",sample_dict)

#create another dictionary
classroom={"Student1":{"name":"Ananya",
                       "age":14,
                       "marks":[90,93,98,98,100,89]
                       },
                       
            "student2":{"name": "Harini",
                        "age":13,
                        "marks":[90,92,95,94,100,87]}        
                        }
print(classroom)
