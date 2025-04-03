def spaceMessage(string):
    while '[' in string:
        open_idx = string.rfind('[', 0, string.find(']'))
        close_idx = string.find(']', open_idx)
        bracket_content = string[open_idx+1:close_idx]
        
        i = 0
        num_str = ""
        while i < len(bracket_content) and bracket_content[i].isdigit():
            num_str += bracket_content[i]
            i += 1
        
        repeat_count = int(num_str)
        repeat_content = bracket_content[i:]
        
        string = string[:open_idx] + repeat_content * repeat_count + string[close_idx+1:]
    
    return string
