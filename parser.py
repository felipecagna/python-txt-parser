import re

hand = input('Enter file name: ')
try : file = open(hand,encoding='utf-8')
except : 
    print('File not found')
    quit()

#Regex options for parsing
choices = {
    'email' : '[A-Za-z0-9-_.]+@[a-z0-9.]+',
    'url' : 'http[s]?://[A-Za-z0-9-_/+.?=]*',
    'image' : '.*\.jpg|.*\.jpeg|.*\.png|.*\.gif',
    'audio' : '.*\.mp3|.*\.aac|.*\.wav|.*\.mp3|.*\.mp3|',
    'video' : '.*\.mp4|.*\.avi|.*\.mov|.*\.flv|.*\.wmv|.*\.mkv|.*\.webm',
    'file' : '.*\.txt|.*\.pdf|.*\.doc|.*\.m3u8',
    'src' : 'src[=":A-Za-z0-9-_.?¿+/();]+',
    'href' : 'href[=":A-Za-z0-9-_.?¿+/();]+'
}
print('Choose an option or press Enter and write yours:\n',*choices.keys())
option = str(input())
if option in choices:
    option = choices[option]
else : option = str(input('Write your own pattern(ex: "word","http[s]?://[A-Za-z0-9-_/+.?=]"):\n'))

#Parsing and printing results
found = list()
def parse(choice):
    for line in file:
        search = re.findall(str(choice),line)
        for s in search:
            if len(s) != 0 and s not in found:
                found.append(s)
            else : continue
    found.sort()
    return found

parse(option)
for it in found:
    print(it)

print('---------- File has',len(found),'results for this search ----------')

#Save or close program
save = input('Save results in file? [y/n]: ')
if save == 'y':
    saved = str(input('Save as: '))
    with open(saved,'wb+') as f:
        for x in found:
            byx = x.encode()+'\n'.encode()
            f.write(byx)
        print('File saved as',saved)
else : quit()
file.close()
