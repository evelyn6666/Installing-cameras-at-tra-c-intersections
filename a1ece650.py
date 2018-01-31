import re
import sys

#class Point(object):
    #def __init__ (self, x, y):
     #   self.x = float(x)
    #    self.y = float(y)
   # def __str__ (self):
     #   return '(' + str(self.x) + ',' + str(self.y) + ')'


def intersect(sg1,sg2):
    x1, y1 = sg1[0][0], sg1[0][1]
    x2, y2 = sg1[1][0], sg1[1][1]
    x3, y3 = sg2[0][0], sg2[0][1]
    x4, y4 = sg2[1][0], sg2[1][1]

    xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
    xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    xnum = round(xnum,2)
    xden = round(xden,2)
    ynum = round(ynum,2)
    yden = round(yden,2)

    if (xden == 0.0) or (yden == 0.0):
        if x1 - x2 == 0:
            if x3 == x1:
                return (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
            else:
                return ('None', 'None')
        elif x1 - x2 != 0:
            k = (y1 - y2)/(x1 - x2)
            b = y1 - k * x1
            if y3 == k * x3 + b and y4 == k * x4 + b :
               return (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
            else:
                xcoor = ycoor = 'None'
                return ('None', 'None')
                #return (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
                #return ('None', 'None')
    else:
        xcoor = round((xnum / xden),2)
        ycoor = round((ynum / yden),2)
        if (max(min(x1, x2), min(x3, x4)) <= xcoor <= min(max(x1, x2), max(x3, x4))) and (
                        max(min(y1, y2), min(y3, y4)) <= ycoor <= min(max(y1, y2), max(y3, y4))):
            return (xcoor, ycoor), (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,1), round(y3,2)), (round(x4,2), round(y4,2))
        else:
            return ('None', 'None')


def vertex(sg1, sg2):
    x1, y1 = sg1[0][0], sg1[0][1]
    x2, y2 = sg1[1][0], sg1[1][1]
    x3, y3 = sg2[0][0], sg2[0][1]
    x4, y4 = sg2[1][0], sg2[1][1]

    xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
    xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    xnum = round(xnum,2)
    xden = round(xden,2)
    ynum = round(ynum,2)
    yden = round(yden,2)

    if (xden == 0.0) or (yden == 0.0):
        if x1 - x2 == 0:
            if x3 == x1:
                return (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
            else:
                return ('None', 'None')
        elif x1 - x2 != 0:
            k = (y1 - y2)/(x1 - x2)
            b = y1 - k * x1
            if y3 == k * x3 + b and y4 == k * x4 + b :
               return (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
            else:
                xcoor = ycoor = 'None'
                return ('None', 'None')
                        #return (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
                        #return ('None', 'None')
    else:
        xcoor = round(xnum / xden,2)
        ycoor = round(ynum / yden,2)
        if (max(min(x1, x2), min(x3, x4)) <= xcoor <= min(max(x1, x2), max(x3, x4))) and (
                max(min(y1, y2), min(y3, y4)) <= ycoor <= min(max(y1, y2), max(y3, y4))):
            #if ((xcoor - x1) * (y2-y1) == (x2 - x1) * (ycoor - y1)):
                return (xcoor, ycoor), (round(x1,2), round(y1,2)), (round(x2,2), round(y2,2)), (round(x3,2), round(y3,2)), (round(x4,2), round(y4,2))
            #else:
                #return (xcoor, ycoor)
        else:
            return ('None', 'None')



streetnumber = 0
dict1 = {}
dict2 = {}
while (raw_input!= 'eof'):
    entry = raw_input()
    entry = entry.lower()

    if entry != 'g':
        try:
            line = entry.split('\n')
            part = entry.strip().split('"')
            num = None
            command = part[0][0]
            streetname = part[1]
            coordinate = part[2]
                #raise Exception('Error: the format of the command is wrong. Please try again')
        #except Exception as ex:
                #sys.stderr.write(str(ex) + '\n')
                #dict1[streetname] = coordinate """must not be here"""
                # #print dict1
            if command == "a":
                if coordinate[-1] != ')':
                    raise Exception('wrong coordinate input')
                else:
                    try:
                        if streetname in dict1.keys():
                            raise Exception('Error : street currently exists')
                        else:
                            dict1[streetname] = coordinate
                            allstreetlist = []
                            d = dict1.values()
                            for v in d:
                                v = v.replace('(', '')
                                v = v.strip().split(')')
                                onestreetlist = []
                                for numPair in v:
                                    if not numPair == '':
                                        Pair = numPair.split(',')
                                        x = int(Pair[0])
                                        y = int(Pair[1])
                                        intNumPair = x, y
                                        onestreetlist.append(intNumPair)
                                allstreetlist.append(onestreetlist)
                    except Exception as ex:
                        sys.stderr.write(str(ex) + '\n')

            if command == "r":
                try:
                    if streetname in dict1.keys():
                        del dict1[streetname]
                        allstreetlist = []
                        d = dict1.values()
                        for v in d:
                            v = v.replace('(', '')
                            v = v.strip().split(')')
                            onestreetlist = []
                            for numPair in v:
                                if not numPair == '':
                                    Pair = numPair.split(',')
                                    x = int(Pair[0])
                                    y = int(Pair[1])
                                    intNumPair = x, y
                                    onestreetlist.append(intNumPair)
                            allstreetlist.append(onestreetlist)
                        #print allstreetlist
                    else:
                        raise Exception('Error : wrong street input')
                except Exception as ex:
                    sys.stderr.write(str(ex) + '\n')

            if command == "c":
                try:
                    if streetname in dict1.keys():
                        dict1[streetname] = coordinate
                        allstreetlist = []
                        d = dict1.values()
                        for v in d:
                            v = v.replace('(', '')
                            v = v.strip().split(')')
                            onestreetlist = []
                            for numPair in v:
                                if not numPair == '':
                                    Pair = numPair.split(',')
                                    x = int(Pair[0])
                                    y = int(Pair[1])
                                    intNumPair = x, y
                                    onestreetlist.append(intNumPair)
                            allstreetlist.append(onestreetlist)
                        #print allstreetlist
                    else:
                        raise Exception('Error: the street does not exist')
                except Exception as ex:
                    sys.stderr.write(str(ex) + '\n')

            if command != "a" and command != "r" and command != "c":
                try:
                    raise Exception('Error: wrong command')
                except Exception as ex:
                    sys.stderr.write(str(ex) + '\n')
        except Exception as ex:
                sys.stderr.write("Error: Incorrect input format or " + str(ex) + '\n')

    elif entry == 'g':
        numofstreets = len(dict1.values())
        #print dict1
        list_v = []
        list_v1 = []
        dict_v = {}
        sg1 = [()] * 2
        sg2 = [()] * 2
        for i in range(numofstreets):
            for j in range(i + 1, numofstreets):
                for sg1_index in range(len(allstreetlist[i]) - 1):
                    for sg2_index in range(len(allstreetlist[j]) - 1):
                        sg1[0] = allstreetlist[i][sg1_index]
                        sg1[1] = allstreetlist[i][sg1_index + 1]
                        sg2[0] = allstreetlist[j][sg2_index]
                        sg2[1] = allstreetlist[j][sg2_index + 1]
                        list_v.append(vertex(sg1, sg2))
                       # print list_v
                        for s in range(len(list_v)-1, -1, -1):
                            if list_v[s] == ('None', 'None'):
                                del list_v[s]
        for m in range(len(list_v)):
            for n in range(len(list_v[m])):
                list_v1.append(list_v[m][n])
        #print list_v1
        list_v2 = []
        for i in list_v1:
            if not i in list_v2:
                list_v2.append(i)                                                #vertex
       # print list_v2
        for t in range(len(list_v2)):
            dict_v[t] = list_v2[t]
        print "V = {"
        for key, value in dict_v.items():
            print str(key) + ': ' + str(value)
        print '}'

        list_v3 = []
        for i in range(numofstreets):
            for j in range(i + 1, numofstreets):
                for sg1_index in range(len(allstreetlist[i]) - 1):
                    for sg2_index in range(len(allstreetlist[j]) - 1):
                        sg1[0] = allstreetlist[i][sg1_index]
                        sg1[1] = allstreetlist[i][sg1_index + 1]
                        sg2[0] = allstreetlist[j][sg2_index]
                        sg2[1] = allstreetlist[j][sg2_index + 1]
                        list_v3.append(intersect(sg1, sg2))
                        for s in range(len(list_v3)-1, -1, -1):
                            if list_v3[s] == ('None', 'None'):
                                del list_v3[s]
        list_v4 = []
        list_v5 = []
        for i in range(len(list_v3)):
            list_v5.append(list_v3[i][0])
            for j in range(1, len(list_v3[i])):
                list_v4.append((list_v3[i][0], list_v3[i][j]))
        list_v6 = []
        for i in list_v5:
            if not i in list_v6:
                list_v6.append(i)

        list_eagle = []
        for k in list_v4:
            if not k in list_eagle:
                list_eagle.append(k)
        for w in range(len(list_eagle)-1,-1,-1):
            for z in range(len(list_v6)-1,-1,-1):
                if (min(list_eagle[w][0][0], list_eagle[w][1][0]) < list_v6[z][0] < max(list_eagle[w][0][0], list_eagle[w][1][0])) or (
                            min(list_eagle[w][0][1], list_eagle[w][1][1]) < list_v6[z][1] < max(list_eagle[w][0][1], list_eagle[w][1][1])):
                    del list_eagle[w]
        for i in range(len(list_v6)):
            for j in range(i+1, len(list_v6)):
                for v in range(len(list_v2)):
                    if (min(list_v6[i][0], list_v6[j][0]) < list_v2[v][0] < max(list_v6[i][0], list_v6[j][0])) or (
                            min(list_v6[i][1], list_v6[j][1]) < list_v2[v][1] < max(list_v6[i][1], list_v6[j][1])) == 0:
                        a = (list_v6[i], list_v6[j])
                        list_eagle.append(a)
        #print list_v6

        list_efinal = []
        for k in list_eagle:
            if not k in list_efinal:
                list_efinal.append(k)

        list_eagle1 = []
        for i in range(len(list_efinal)):
            for j in range(len(list_v2)):
                if (list_v2[j] == list_efinal[i][0]) or (list_v2[j] == list_efinal[i][1]):
                    list_eagle1.append((j))
        print 'E = {'
        i = 0
        while i < len(list_eagle1):
            print "<" + str(list_eagle1[i]) + "," + str(list_eagle1[i + 1]) + ">"
            i = i + 2
        print '}'
        #print list_eagle1
        #print list_efinal
        #print list_eagle
