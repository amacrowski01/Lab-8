def remove_substring(string,sub):
    output=[]
    index=0
    while index<len(string):
        if string[index:index+len(sub)]==sub:
            index+=len(sub)#advances index so is skips over spam substring
        else:
            output.append(string[index])
            index+=1
    print("".join(output))#puts spam-free string together

string='SPAM!?HelloSPAM!? worldSPAM!?!'
remove='SPAM!?'

remove_substring(string,remove)


