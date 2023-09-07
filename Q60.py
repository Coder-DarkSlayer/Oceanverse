with open("sherlock.txt", "r",encoding="utf-8") as f: # open file in read mode with encoding utf-8
    data = f.read() # read file
    f.close() # close file

res = "" # empty string

for i in data: # iterate through data
    if i.isalpha(): # if i is alphabet
        res += i # add i to res

print(res) # print res