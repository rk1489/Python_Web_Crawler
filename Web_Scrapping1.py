import sqlite3
import codecs
import urllib.request
from bs4 import BeautifulSoup

file1 = open("rejectlist.txt","r")
ignore = file1.read().split()
ignoreset = set(ignore)
file1.close()

print("Input the no. of URLs to Scrap:")
N=int(input())
print("Input The URLs:")
URL=[]
for _ in range(N):
    URL=URL+input()
    
for i in range(N):
    req = urllib.request.Request(URL[i])

    f = codecs.open("code.txt", "a+", "utf-8")
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page,"html.parser")
    print(soup.title)
    print(soup.title.string)
    
    for script in soup(["script","style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())

    for line in lines:
        print(line)
        line = line.replace("'"," ")

    f.write(line)
    f.close()

    d = {}
    f = open("code.txt","r")
    words = f.read().split()
    wc = len(words)
    print(wc)

    for word in words:
        if word not in ignoreset:
            if word not in d:
                d[word] = 1
            else:
                d[word]+=1
    f.close()

    for word in sorted(d.keys()):
        print(word,d[word],(d[word])/wc*100)

    conn = sqlite3.connect('project.sqlite3')
    conn.execute("drop table if exists words")
    conn.execute('''create table words(url text,word text,count)''')

    for word in sorted(d.keys()):
        str1 = "insert into words values ('www.python.org','"+ word+"','"+str(d[word])+"')"
        print(str1)

    conn.execute("insert into words values ('www.python.org','"+word+"','"+str(d[word])+"')")
    cursor=conn.execute("select * from words order by count desc")

    count = 1

    for row in cursor:
        print("word",row[1])
        print("count: ",row[2])
        count = count + 1
        if count == 6:
            break
