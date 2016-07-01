import xlwt
 
 
"""
{           "1":[3],
            "2":[4,5],
            "3":[5,5,6],
            "4":[6,1,2,3,4],
            "5":[7,4],
            "6":[8],
            "7":[9,1,2,3,4,5,6],
            "307":[5, 7, 8, 9, 11, 12]
}
字典里的数据写到Execel中
"""
if __name__ == '__main__':
    
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("tips") #Excel单元格名字
     
     
    obj = open("tips.txt", "r") #字典数据放在一个 txt文件
    all_txt = obj.read()
    new_txt = eval(all_txt)
     
    keys = []
    for key in new_txt.keys() :
        keys.append(int(key));
    keys.sort()
     
    i = 0
     
    for k in keys:
        dickkey = str(k)
        sheet.write(i, 0, dickkey)
        j = 1
        print "dickkey===",dickkey
        vals = new_txt.get(dickkey, None) #k or dickkey
        if vals is None:
            vals = new_txt.get(k, None) #k or dickkey
        print "vals==========",vals
        for item in vals :
            import types
            if type(item) is types.StringType :
                item = item.decode('utf8') 
     
    #        if type(item) is types.IntType:
    #            continue
            sheet.write(i,j ,item )
            j +=1
        i += 1
    wbk.save('tips.xls') #保存为 tips.xls文件

