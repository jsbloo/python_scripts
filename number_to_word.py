def numbers_to_words(number):
    teen_dict = {
        '0' : '',
        '1' :'One',
        '2':'Two',
        '3':'Three',
        '4':'Four',
        '5':'Five',
        '6':'Six',
        '7':'Seven',
        '8':'Eight',
        '9':'Nine',
        '10':'Ten',
        '11':'Eleven',
        '12':'Twelve',
        '13':'Thirteen',
        '14':'Fourteen',
        '15':'Fithteen',
        '16':'Sixteen',
        '17':'Seventeen',
        '18':'Eighteen',
        '19':"Nineteen"
    }

    dec_dict = {
        '2': 'Twenty',
        '3': 'Thirty',
        '4': 'Fourty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety',
    }
    
    cent_dict = {
        '3': 'Hundred',
        '4': 'Thousand',
        '7': 'Million',
        '10': 'Billion',
        '13': 'Trillion'
    }

    digit_str = str(number)
    digit_len =  len(digit_str)

    if digit_len == 1:
        return teen_dict[digit_str[0]]
    
    if digit_len == 2:
        if number < 20:
            return teen_dict[str(number)]
        if(digit_str[1]!='0'):
            return dec_dict[digit_str[0]] + '-' + teen_dict[digit_str[1]]
        return dec_dict[digit_str[0]]
    
    if digit_len == 3:
        builder = teen_dict[digit_str[0]] + '-' + cent_dict[str(digit_len)]
        x = numbers_to_words(int(digit_str[1] + digit_str[2]))#recursion
        if x !='':
            builder = builder + " and " + x 
        return builder

    if digit_len == 4:
        x = teen_dict[digit_str[0]] + "-" + cent_dict['4'] + " " + numbers_to_words(int(digit_str[1:4]))
        return x

    if digit_len > 4 :
        if str(len(digit_str)) in cent_dict:
            builder = numbers_to_words(int(digit_str[:1])) + '-' + cent_dict[str(len(digit_str))]#recursion
            builder = builder + ", " + numbers_to_words(int(digit_str[1:]))#recursion
        elif str(len(digit_str)-1) in cent_dict:
             builder = numbers_to_words(int(digit_str[:2])) + '-' + cent_dict[str(len(digit_str)-1)]#recursion
             builder = builder + ", " + numbers_to_words(int(digit_str[2:]))#recursion
        else:
            builder = numbers_to_words(int(digit_str[:3])) + '-' + cent_dict[str(len(digit_str)-2)]#recursion
            builder = builder + ", " + numbers_to_words(int(digit_str[3:]))#recursion

        return builder










