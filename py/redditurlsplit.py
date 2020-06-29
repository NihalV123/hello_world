i=1;
count = 0
for each_line in open("redditurl.txt", "r"):
    each_line = each_line.replace(',', '')
    count = count + 1
    print(each_line)
    f= open(str(i)+".txt","a+")
    f.write(each_line) 
    if (count == 100):
         count = 0
         i =i+1;
f.close()