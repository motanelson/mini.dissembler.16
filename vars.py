a=10
b=11
v=vars

v=vars()
a=list(v)
for b in a:
    if len(b)>0:
        if b[0:1]!="_":
            print(b)