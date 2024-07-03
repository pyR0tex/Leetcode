# random shit

input = ["task: compile","files: foo.txt","deps:","",]
changedFiles = ["foo.txt","README.md"]
ttr = []
for i in input:
    l = i.split()
    if len(l) > 1:
        ttr.append(l[1])
        
print(ttr)
