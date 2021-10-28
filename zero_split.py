def zero_split(s):
    i = 0
    j = 0
    s_list = []
    for c in s:
        if c == '0':
            if i+1 < len(s):
                if s[i+1] != '0':
                    s_list.append(s[j:i+1])
                    j = i+1
        if i+1 == len(s):
            s_list.append(s[j:i+1])      
        i+=1
    return s_list