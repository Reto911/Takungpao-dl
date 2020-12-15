import wget
import arrow
import datetime
d1 = arrow.get(input("输入起始日期(yyyymmdd): "))
d2 = arrow.get(input("输入终止日期(yyyymmdd): "))
day = d2 - d1
if day.days < 0:
    print("终止日期早于起始日期。")
    exit(1)
for i in range(int(day.days)+1):
    date = d1.shift(days=i)
    url = 'http://paper.takungpao.com/resfile/PDF/'+date.format('YYYYMMDD')+'/ZIP/'+date.format('YYYYMMDD')+'_pdf.zip'
    file_name = wget.download(url,out='./pdf')
    print('\n' + file_name + ' is downloaded')
