resultlst = [[3,0],[0,3],[3,1],[1,3],[3,2],[2,3]]
#用积分乘以100加净胜分，为各队有效积分
real = [[103,-3,0.125],[-3,103,0.125],[102,-2,0.1875],[-2,102,0.1875],[101,-1,0.1875],[-1,101,0.1875]]
destiny = {'s':0,'a':0,'b':0}
sresult = []
bresult = []
k = 0
#剩余比赛：1vs5，2vs4，2vs5，3vs4
for onefive in real:
    for twofour in real:
        twofive = real[1]
        for threefour in real:
            result = [[1, 304], [2, 204], [3, 201], [4, 200], [5, 99], [6, 92]]
            result[0][1] += onefive[0]
            result[4][1] += onefive[1]
            result[1][1] += twofour[0]
            result[3][1] += twofour[1]
            result[1][1] += twofive[0]
            result[4][1] += twofive[1]
            result[2][1] += threefour[0]
            result[3][1] += threefour[1]
            final = sorted(result, key=lambda x: x[1])
            k += 1
            for i in range(0, 6):
                if final[i][0] == 5:
                    if i == 4 or i == 5:
                        destiny["s"] = destiny["s"] + onefive[2] * twofour[2] * threefour[2]
                        sresult.append(resultlst[real.index(onefive)])
                    if i == 2 or i == 3:
                        destiny["a"] = destiny["a"] + onefive[2] * twofour[2]* threefour[2]


                    if i == 0 or i == 1:
                            destiny["b"] = destiny["b"] + onefive[2] * twofour[2] * twofive[2] * threefour[2]
                            bresult.append(resultlst[real.index(onefive)])


print(destiny)
print(bresult)
dic = {}
for it in sresult:
    ok = it[0]*10 + it[1]
    if ok not in dic.keys():
        dic[ok] = 0
    dic[ok] += 1

print(dic)
print(k)




