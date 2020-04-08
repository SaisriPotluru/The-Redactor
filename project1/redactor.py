import sys,getopt

import main 

full_com_argmt= sys.argv
print(full_com_argmt)
input=["--input"]
for i in range(len(full_com_argmt)):
    if full_com_argmt[i] == "--input":
        rea =  main.input(full_com_argmt[i+1])
        print(rea)
      
for c in full_com_argmt:      
    if c == "--names":
        namr,c =  main.extractnames(rea)
        print(namr)
        print(c) 
    if c == "--dates":
        date,dc =  main.extractdates(namr)
        print(namr)
        print(dc)
    if c == "--gender":
        gender,gc =  main.extractgender(date)
        print(gender)
        print(gc)     
for i in range(len(full_com_argmt)):
    if full_com_argmt[i] == '--concept':
        concept,cc = main.concept(full_com_argmt[i+1],gender)
        print(concept)
        print(cc)
for i in range(len(full_com_argmt)):
    if full_com_argmt[i] == '--stats':
        counttotal = redactor.stats(c,dc,gc,cc))
        
        def redactor.stats(c,dc,gc,cc):
            countn=c
            countd=dc
            countg=gc
            countc=cc
            return countn,countd,countg,countc

   # if full_com_argmt[i] == "--output":
    #    outr =  main.output(full_com_argmt[i+1])
   # if full_com_argmt[i] == "--stats":
    #    stas =  main.stats(full_com_argmt[i+1])    
#res = [full_com_argmt.index(i) for i in input]
#ires = [ele for ele in full_com_argmt if(ele in input)]
#print(ires)    
#print(res)    
    
   # print(f"Argument {i:>6}: {arg}")
