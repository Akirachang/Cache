import os
filelist = os.listdir("trace") 
num = 2
os.system("mkdir "+str(num)) 
for file in filelist:
    print('hi')
    print('hiiii')
    try:
        command = "time ./bin/CMPsim.gentrace.32 -threads 1 -t "+"./trace/"+file+" -o ./"+str(num) +"/"+file[:-13]+".stats -cache UL3:1024:64:16 -LLCrepl "+str(num)
        print '\n'
        print command
        print '\n' 
        os.system(command)
    except: 
        pass