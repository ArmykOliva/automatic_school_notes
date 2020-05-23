line = "i hate fucking nig<span class='ga'>shit</span>gers"
#res = '<font gay>'.join(test_str[i:i + 1] for i in range(0, len(test_str), 1))
res = ""
i = 0
while i < len(line):
    if (line[i:i + 1] == " "):
        res += line[i:i + 1]
    elif (line[i:i + 5] == "<span" or line[i:i + 6] == "</span"):
        while line[i:i + 1] != ">":
            res += line[i:i + 1]
            i += 1
        res += ">"
    else:
        res += ".." + line[i:i + 1] + ".."
        
    i += 1

print(res)