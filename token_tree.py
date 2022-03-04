#coding:utf-8
import time

class treeNode:
    def __init__(self, nameValue):
        self.name = nameValue
        self.children = {}

    def disp(self, ind=1):
        print(' '*(ind), self.name, ' ')
        for child in self.children.values():
            child.disp(ind+1)
        
def updateFPtree(items, inTree):
    if items[0] not in inTree.children:
        inTree.children[items[0]] = treeNode(items[0])
    if len(items) > 1:
        updateFPtree(items[1::], inTree.children[items[0]])

def createFPtree(dataset):
    retTree = treeNode("Null")
    for trans in dataset:
        updateFPtree(trans, retTree)

    return retTree

def LoadData():

    with open("dict_no_space.txt",mode="r",encoding="utf-8") as file:
        test_data = []
        for line in file:
            test_data.append(line.strip().encode('utf-8').decode('utf-8-sig'))

    # test_data = ["扁豆",
    #             "扁平",
    #             "扁擔",
    #             "敵後伏擊",
    #             "敵後作戰",
    #             "敵後",
    #             "敵機",
    #             "敵境",
    #             "底下",
    #             "底下人",
    #             "底下奏樂",
    #             "底限",
    #             "底線",
    #             "扁桃",
    #             "扁桃腺",
    #             "貶低",
    #             "貶低人",
    #             "貶斥",
    #             "貶義",
    #             "貶義詞"]
    data = list(map(list,test_data))
    return data

def mineTree(FPtree, sentence, a):
    # a = 0
    if a <= (len(sentence) - 1):
        if sentence[a] in FPtree.children:
            a = a + 1
            a = mineTree(FPtree.children[sentence[a-1]], sentence, a)
    return a


def tokenize(FPtree,sentence):
    toke=[]
    sentencelen =  len(sentence)
    while sentencelen != 0:
        a = 0
        a = mineTree(FPtree, sentence, a)

        if a == 0 :
            toke.append(sentence[0:1])
            sentence = sentence[1:len(sentence)]
            sentencelen = len(sentence)
        else:
            toke.append(sentence[0:a])
            sentence = sentence[a:len(sentence)]
            sentencelen = len(sentence)
        
    return toke

def Combine(AfterTokenizeList):
    flag = 0
    output = []
    temp = []
    for i in AfterTokenizeList:
        if len(i) != 1:
            if flag == 0:
                output.append(i[::])
            else :
                output.append("".join(temp))
                output.append(i[::])
                temp = []
                flag = 0
                
                
        else :
            if flag == 0:
                temp.append(i)
                flag = 1
            else :
                temp.append(i)
    print(output)
    return 0


#開始計時
if __name__ == '__main__':
    
    now = lambda : time.time()
    
    start = now()
    simDat = LoadData()
    FPtree = createFPtree(simDat)

    print(f"Build Token Tree Time : {now()-start}")
    while True:
        x = input('請輸入文字 (輸入q以結束程式): ')
        if x !='q':
            
            #開始計時
            start = now()
            
            
            sentence = x
            toke = tokenize(FPtree, sentence)
            
            Combine(toke)
            
            
            print("執行時間：%f 秒" % (now() - start))

            print("len : ",len(sentence))

        else: break
    