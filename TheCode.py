def TakeList():
    MonkeyList = []
    x = int(raw_input('How many items in your list?'))
    for item in xrange(x):
        h = int(raw_input('item?'))
        MonkeyList.append(h)
    return MonkeyList
def count(sequence, item):
    g = 0
    result = 0
    List = [1, 2]
    Float = 1.6
    String = 'LeBron James'
    Integer = 1
    InputType = type(item)
    def IfFloat():
        Wot = 0
        for lel in sequence:
            if lel == item:
                Wot += 1
        return Wot
    def IfInt():
        CC = 0
        for numero in sequence:
            if numero == item:
                CC += 1
        return CC
    def IfStr():
        Resu = 0
        itemd = str(item)
        for thing in sequence:
            if thing == itemd:
                Resu += 1
        return Resu
    def IfList():
        Ind = 0
        Indseq = 0
        Res = 0
        CurrentRes = 0
        for thing in range(len(sequence)):
            if Ind == len(item) and CurrentRes == len(item):
                Res += 1
                CurrentRes = 0
                Ind = 0
            elif sequence[Indseq] == item[Ind]:
                if Ind < len(item):
                    Ind += 1
                    Indseq += 1
                    CurrentRes += 1
            elif sequence[Indseq] != item[Ind]:
                Indseq += 1
                Ind = 0
        return Res
    for cosa in sequence:
        if InputType == type(List):
            return IfList()
        elif InputType == type(Float):
            return IfFloat()
        elif InputType == type(String):
            return IfStr()
        elif InputType == type(Integer):
            return IfInt()
def MostNums(List):
    Count = 0
    ResesDict = {}
    CountDict = {}
    for item in List:
        ResesDict[count(List, item)] = item
        Count += 1
    if max(ResesDict) <= 1:
        return List[(len(List) - 1)/2]
    return ResesDict[max(ResesDict)]
def MMMR(List):
    List.sort()
    if ((len(List)-1)/2.0) % 1 != 0:
        Median = (List[(len(List)-1)/2] + List[len(List)/2]) / 2
    else:
        Median = List[(len(List)-1)/2]
    Mode = MostNums(List)
    Mean = (sum(List))/(len(List))
    Range = max(List) - min(List)
    NewDict = {}
    NewDict['Mean'] = Mean
    NewDict['Median'] = Median
    NewDict['Mode'] = Mode
    NewDict['Range'] = Range
    return NewDict
def MMMRX(List, desired, x):
    for tien in range(x):
        List.append(tien)
        TheRes = MMMR(List)
        if TheRes['Mean'] == desired:
            return tien
        else:
            List.remove(tien)
