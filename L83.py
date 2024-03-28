def replace_substring(string,sub,replace):
    output=[]#creates empty list
    index=0
    while index<len(string):
        if string[index:index+len(sub)]==sub:#checks if substring starting at current index position is spam
            index+=len(sub)#skip length of sub
            output.append(replace)#append replacement words
        else:
            output.append(string[index])#appends onto list
            index+=1#moves to next character
    print("".join(output))#puts string together and prints

string='SPAM!?HelloSPAM!? worldSPAM!?!'
sub='SPAM!?'
replace='Why'

replace_substring(string,sub,replace)

