file=open("групировки_альбомов2.txt").readlines()
string="digital"
dict_group_album={}
for i in file:
    file_split1=i.split("=>")
    name=file_split1[0]
    if name == string:
        file_split2=file_split1[1].split("<>")
        for j in file_split2[0:-1]:
            file_split3=j.split("::")
            print(file_split3)
            dict_group_album[file_split3[0]]=file_split3[1]

for i in dict_group_album.items():
    print(i)

