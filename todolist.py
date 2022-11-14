import os
try:
    import tkinter as tk
except ImportError:
    os.system('pip install tkinter')
    import tkinter as tk
try:
    import regex as re
except ImportError:
    os.system('pip install regex')
    import regex as re
from tkinter import filedialog
import datetime
import time


class makeCal:

    def readPath():
        path = tk.Tk()
        path.withdraw()
        f_path = filedialog.askopenfilename()
        return f_path

    def readText(path):
        file = open(path, 'r')
        text = file.read()
        file.close()
        return text

    def listOperate(text):
        issue = '{{(.*?)}}'
        list = re.findall(issue, text)
        return list

    def issueOperate(list):
        issueList = []
        for issue in list:
            key = ':(.*?);'
            keyList = re.findall(key, issue)
            issueList.append(keyList)
        return issueList

    def fTrans(begin, end):
        date = datetime.date.today()
        year = date.year
        month = date.month
        day = date.day
        isNatural = False
        if '明天' in begin:
            isNatural = True
            begin = begin[2:]
            day += 1
        elif '后天' in begin:
            isNatural = True
            begin = begin[2:]
            day += 2
        value = str(year) + str(month) + str(day) + 'T'
        if not isNatural:
            value = begin[:8] + 'T'
            begin = begin[8:]
        beginTime = float(begin)
        if beginTime < 8:
            beginTime = 24 - beginTime
            swag = value[:7]
            value = swag + str(int(value[7])+1) + value[8:] + 'T'
        beginValue = str(int(100*(beginTime - 8)))
        if beginTime < 18:
            beginValue = '0' + beginValue
        if beginTime >= 8 and beginTime < 9:
            beginValue = '0' + beginValue
        endTime = float(end)
        if endTime < 8:
            enTime = 24 - endTime
        endValue = str(int(100*(endTime - 8)))
        if endTime < 18:
            endValue = '0' + endValue
        if endTime >= 8 and endTime < 9:
            endValue = '0' + endValue
        list = [value+beginValue+'00Z', value+endValue+'00Z']
        return list


    def timeFormat(list):
        Dic = {'UID': '', 'DESCRIPTION': '', 'DTSTART': '', 'DTEND': '', 'SUMMARY': ''}
        begin = ''
        end = ''
        Dic['UID'] = list[0]
        Dic['SUMMARY'] = list[0]
        Dic['DESCRIPTION'] = list[2]
        time = list[1]
        if '~' in time or '-' in time:
            isBegin = True
            for ch in time:
                if ch == '~' or ch == '-':
                    isBegin = False
                    continue
                if(isBegin):
                    begin += ch
                else:
                    end += ch
        else:
            begin = time
        time = makeCal.fTrans(begin, end)
        Dic['DTSTART'] = time[0]    
        Dic['DTEND'] = time[1]
        return Dic

    def listDrop(path, finaList):
        now = time.localtime()
        file = open(path, 'w')
        file.write('BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:\n')
        for issue in finaList:
            file.write('BEGIN:VEVENT\n')
            for key in issue.keys():
                file.write(str(key)+':'+str(issue[key])+'\n')
            file.write('END:VEVENT\n')
        file.write('END:VCALENDAR\n')
        file.close()
        return

    def makeFormat(name, path):
        new = './' + name + '.ics'
        if new in os.listdir('./'):
            os.remove(new)
        os.rename(path, new)
        return



    def main():
        path = makeCal.readPath()
        text = makeCal.readText(path)
        list = makeCal.listOperate(text)
        issueList = makeCal.issueOperate(list)
        finaList = []
        for list in issueList:
            finaList.append(makeCal.timeFormat(list))
        name = 'newSchedule'
        path = './' + name + '.txt'
        makeCal.listDrop(path, finaList)
        makeCal.makeFormat(name, path)
        os.system('open '+'./'+name+'.ics')
        return


print("请选择txt格式的日程文件")
input()
makeCal.main()

if __name__ == '__main__':
    print('Thanks for using!')