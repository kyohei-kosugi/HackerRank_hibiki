if __name__ == '__main__':
    s = input()
    for i in range(0, len(s)):
        if s[i].isalnum() == True:
            isalnum = 'True'
            break
        else:
            isalnum = 'False'
    for j in range(0, len(s)):
        if s[j].isalpha() == True:
            isalpha = 'True'
            break
        else:
            isalpha = 'False'
    for k in range(0, len(s)):
        if s[k].isdigit() == True:
            isdigit = 'True'
            break
        else:
            isdigit = 'False'
    for l in range(0, len(s)):
        if s[l].islower() == True:
            islower = 'True'
            break
        else:
            islower = 'False'
    for m in range(0, len(s)):
        if s[m].isupper() == True:
            isupper = 'True'
            break
        else:
            isupper = 'False'
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)