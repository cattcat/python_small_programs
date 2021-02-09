level = [0.05, 0.12, 0.2, 0.3, 0.4, 0.45]

sal = float(input("請輸入年薪："))

if sal > 0 and sal <= 540000:

    print("使用税率：",level[0])

    print("所得稅為：%.0f元" % ((sal - 88000 - 90000 - 128000 ) * level[0] ))

elif sal > 540001 and sal <= 1210000:

    print("使用税率：", level[1])

    print("所得稅為：%.0f元" % ((sal - 88000 - 90000 - 128000 ) * level[1] ))

elif sal > 1210001 and sal <= 2420000:

    print("使用税率：", level[2])

    print("所得稅為：%.0f元" % ((sal - 88000 - 90000 - 128000 ) * level[2] ))

elif sal > 2420001 and sal <= 4530000:

    print("使用税率：", level[3])

    print("所得稅為：%.0f元" % ((sal - 88000 - 90000 - 128000 ) * level[3] ))

elif sal > 4530001 and sal <= 10310000:

    print("使用税率：", level[4])

    print("所得稅為：%.0f元" % ((sal - 88000 - 90000 - 128000 ) * level[4] ))

elif sal > 10310001 :

    print("使用税率：", level[5])

    print("所得稅為：%.0f元" % ((sal - 88000 - 90000 - 128000 ) * level[5] ))