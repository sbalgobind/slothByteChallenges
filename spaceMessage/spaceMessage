def spaceMessage(string):
    answer = ''
    subStrings = string.split('[')
    for i in range(len(subStrings)):
        if subStrings[i].count(']') > 0:
            num = int(subStrings[i][0])
            subStrings[i] = subStrings[i][1:]
            index = subStrings[i].index(']')
            multiple = subStrings[i][0:index]
            answer += multiple * num 
            subStrings[i] = subStrings[i].replace(']', '')
            answer += subStrings[i][index:]
        else:
            answer += subStrings[i]
    return answer
