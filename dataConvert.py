import time
import datetime

dateBefore=1
input="000000_0"
output=input+".out"
table="recsys_kpi_total_copy"
rowName =["gmv","req_users","req_num","orders","clicks","all_orders","all_gmv"]
rowId =[7,2,1,5,3,8,10]

tim = (datetime.datetime.now() - datetime.timedelta(days = dateBefore))
sdate_time = tim.strftime("%Y-%m-%d")
stype=11

slogtype="gmv.click"
search_key=12

file = open(input)
outfile = open(output,'w')
tmp_line="insert into "+table +" (date_time,type,logtype,search_key,action,counts)values('"
#for rn in rowName:
#    tmp_line+=(rn +",")
#tmp_line += " values ("+timFormat+","
    
for line in file:
    la = line.split("\001")
    sqlLine = tmp_line
    i=0
    for ri in rowId:
        if(la[search_key]==""):
            spd="rec.index"
        else:
            spd=la[search_key]
        sqlLine=tmp_line+(sdate_time+"','"+"rec"+"','"+slogtype+"','"+spd.strip()+"','"+rowName[i]+"','")
        if(la[ri]!="\N"):
            sqlLine+=(la[ri]+"');")
        else:
            sqlLine+="');"
        outfile.write(sqlLine+"\r\n")
        i+=1
    
outfile.close

    
    
