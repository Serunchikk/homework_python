m = [1,3,6,3,23,3,45,54,56,67,34,233,13,1]
for k in range(len(m)-1):
    for l in range(k+1,len(m)):
        if m[k] > m[l]:
            m[k],m[l] = m[l],m[k]
print(m)