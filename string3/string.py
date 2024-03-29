s="abcabc"
i=0
while i<len(s)-1:
    if s[i:i+2] in ['ab','ba']:
        s=s.replace(s[i:i+2],'c',1)
        i=0
    elif s[i:i+2] in ['cb','bc']:
        s=s.replace(s[i:i+2],'a',1)
        i=0
    elif s[i:i+2] in ['ac','ca']:
        s=s.replace(s[i:i+2],'b',1)
        i=0
    else:
        i+=1
print(s)