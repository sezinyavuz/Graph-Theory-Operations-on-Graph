import sys

with open("output.txt", "w", encoding="utf-8") as f:
    with open(sys.argv[1], "r", encoding="utf-8") as file:

        dict = {}
        for i in file:
            name = i.split(":")[0]
            dict[name] = i.split(":")[1].replace("\n","").split(" ")


        with open(sys.argv[2], "r", encoding="utf-8") as file2:
            for i in file2:
                i = i.replace("\n","").split(" ")

                if i[0] == 'ANU':
                    if i[1] in dict:
                        f.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")
                    else:
                        dict[i[1]] = []
                        f.write("User '%s' has been added to the social network successfully\n" % (i[1]))

                if i[0] == 'DEU':
                    if i[1] not in dict:
                        f.write("ERROR: Wrong input type! for 'DEU'!--There is no user named '%s'!!\n" % (i[1]))
                    else:
                        f.write("User '%s' and his-her all relations have been deleted successfully\n" % (i[1]))
                        del dict[i[1]]
                        for a,j in dict.items():
                            for k in j :
                                if k == i[1]:
                                    j.remove(i[1])

                if i[0] == 'ANF':
                    if i[1] not in dict and i[2] in dict:
                        f.write("ERROR: Wrong input type! for 'ANF'! -- No user named '%s' found!!\n" % (i[1]))
                    if i[2] not in dict and i[1] in dict:
                        f.write("ERROR: Wrong input type! for 'ANF'! -- No user named '%s' found!!\n" % (i[2]))
                    if i[1] not in dict and i[2] not in dict:
                        f.write("ERROR: Wrong input type! for 'ANF'! -- No user named '%s' and '%s' found!!\n" % (i[1],i[2]))
                    if i[1] in dict and i[2] in dict:
                        if i[1] in dict[i[2]]:
                            f.write("ERROR: A relation between '%s' and '%s' already exists!!\n" % (i[1],i[2]))
                        else:
                            dict[i[1]].append(i[2])
                            dict[i[2]].append(i[1])
                            f.write("Relation between '%s' and '%s' has been added successfully\n" % (i[1],i[2]))


                if i[0] == 'DEF':
                    if i[1] not in dict and i[2] in dict:
                        f.write("ERROR: Wrong input type! for 'DEF'! -- No user named '%s' found!!\n" % (i[1]))
                    if i[2] not in dict and i[1] in dict:
                        f.write("ERROR: Wrong input type! for 'DEF'! -- No user named '%s' found!!" % (i[2]))
                    if i[1] not in dict and i[2] not in dict:
                        f.write("ERROR: Wrong input type! for 'DEF'! -- No user named '%s' and '%s' found!!\n" % (i[1],i[2]))
                    else:
                        if i[1] not in dict[i[2]]:
                            f.write("ERROR: No relation between '%s' and '%s' found!!\n" % (i[1],i[2]))
                        else:
                            dict[i[2]].remove(i[1])
                            dict[i[1]].remove(i[2])
                            f.write("Relation between '%s' and '%s' has been deleted successfully\n" % (i[1],i[2]))


                if i[0] == 'CF':
                    if i[1] not in dict:
                        f.write("ERROR: Wrong input type! for 'CF'! -- No user named '%s' found!\n" % (i[1]))
                    else:
                        count=0
                        for j in dict[i[1]]:
                            count +=1
                        f.write("User '%s' has '%s' friends\n" % (i[1],count))


                if i[0] == 'FPF':
                    if i[1] not in dict:
                        f.write("ERROR: Wrong input type! for 'FPF'! -- No user named '%s' found!\n" % (i[1]))
                    else:
                        if i[2] == '1':
                            count = 0
                            for j in dict[i[1]]:
                                count+=1
                            set1 = set()
                            for j in dict[i[1]]:
                                set1.add(j)
                            f.write("User '%s' has '%s' possible friends when maximum distance is 1\nThese possible friends:%s\n" % (i[1],count,str(sorted(set1)).replace("[","{").replace("]","}")))

                        if i[2] == '2':
                            setx = set()
                            for j in dict[i[1]]:
                                setx.add(j)
                                for k in dict[j]:
                                    setx.add(k)
                            setx.remove(i[1])
                            f.write("User '%s' has '%s' possible friends when maximum distance is 2\nThese possible friends: %s\n" % (i[1],len(setx),str(sorted(setx)).replace("[","{").replace("]","}")))

                        if i[2] == '3':
                            sety = set()
                            for j in dict[i[1]]:
                                sety.add(j)
                                for k in dict[j]:
                                    sety.add(k)
                                    for a in dict[k]:
                                        sety.add(a)
                            sety.remove(i[1])
                            f.write("User '%s' has '%s' possible friends when maximum distance is 3\nThese possible friends: %s\n" % (i[1], len(sety), str(sorted(sety)).replace("[","{").replace("]","}")))

                        if int(i[2]) > 3 or int(i[2]) < 1 :
                            f.write("ERROR: Maximum distance is out of range!!\n")

                if i[0] == 'SF':
                    if i[1] not in dict:
                        f.write("ERROR: Wrong input type! for 'SF'! -- No user named '%s' found!\n" % (i[1]))
                    else:
                        if int(i[2]) < 2 or int(i[2]) > 3:
                            f.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
                        else:
                            if i[2] == '2':
                                friendslist = []
                                for j in dict[i[1]]:
                                    for k in dict[j]:
                                        if k not in dict[i[1]]:
                                            friendslist.append(k)
                                for j in range(len(dict[i[1]])):
                                    friendslist.remove(i[1])
                                friendslist.sort()
                                setz2 = set()
                                setz3 = set()
                                for j in friendslist:
                                    if friendslist.count(j) == 2:
                                        setz2.add(j)
                                    if friendslist.count(j) == 3:
                                        setz3.add(j)
                                f.write("Suggestion List for '%s' (when MD is 2):\n" % (i[1]))
                                for j in setz2:
                                    f.write("'%s' has 2 mutual friends with '%s'\n" % (i[1], j))
                                for j in setz3:
                                    f.write("'%s' has 3 mutual friends with '%s'\n" % (i[1], j))
                                f.write("The suggested friends for '%s': " % (i[1]))
                                for j in setz2:
                                    f.write("'%s'," % (j))
                                for j in setz3:
                                    f.write("'%s'," % (j))
                                f.write("\n")

                            if i[2] == '3':
                                friendslist = []
                                for j in dict[i[1]]:
                                    for k in dict[j]:
                                        if k not in dict[i[1]]:
                                            friendslist.append(k)
                                for j in range(len(dict[i[1]])):
                                    friendslist.remove(i[1])
                                friendslist.sort()
                                set10 = set()
                                for j in friendslist:
                                    if friendslist.count(j) == 3:
                                        set10.add(j)
                                f.write("Suggestion List for '%s' (when MD is 3):\n" % (i[1]))
                                for j in set10:
                                    f.write("'%s' has 3 mutual friends with '%s'\n" % (i[1], j))
                                f.write("The suggested friends for '%s': " % (i[1]))
                                for j in set10:
                                    f.write("'%s'," % (j))
                                f.write("\n")


