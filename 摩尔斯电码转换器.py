
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','X','Y','Z']
morse=['·-','-···','-·-·','-··','·','··-·','--·','····','··','·---','-·-','·-··','--','-·','---','·--·','--·-','·-·','···','-','··-','···-','·--','-··-','-·--','--··']
q=input('你想干什么（1=w-m,2=m-w，3=关于此软件)：')
if q=='1':
    t=input('请输入明文（仅英文，不分大小写）：').upper()
    temp=''
    for i in t:
        if i in letter:
            temp+=morse[letter.index(i)]+''
        else:
            t+=''
    print('摩斯电码：',temp)

elif q=='2':
    t2=input('请输入暗文（用空格分割）：')
    temp2=t2.split(' ')
    temp3=''
    for i in temp2:
        if i in morse:
            temp3+=letter[morse.index(i)]
        else:
            temp3+=''
    print('明文：',temp3)

elif q=='3':
    print('''         关于此软件
                此软件是为了让用户在使用摩
                斯电码传输信息时，更好的进
                行编译而编写。

                软件版本：1.0.1（正式版）
                编译语言：python 3.10.2
                发布时间：2022.10.7 6：50 p.m.
                持有人保留所有权利             ''')


