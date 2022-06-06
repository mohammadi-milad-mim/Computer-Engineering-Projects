#MEX function
def MEX(li):
    mex = 0
    while mex in li:
        mex += 1
    return mex


kalyes = [-1]*10001
#Base Cases
kalyes[0] = 0
kalyes[1] = 1
kalyes[2] = 2

for i in range(3, 10001):
    states_SGs = []
    
    #One Shot Begining
    states_SGs.append(kalyes[i-1])
    
    #One Shot End
    states_SGs.append(kalyes[i-2])

    #One Shot Middle
    for j in range(1, i//2+1):
        start = j
        end = i - (j+1)
        if end <= 0:
            break
        sg_val = kalyes[start] ^ kalyes[end]
        states_SGs.append(sg_val)
        
    #Two Shot Middle
    for j in range(1, i//2+1):
        start = j
        end = i - (j+2)
        if end <= 0:
            break
        sg_val = kalyes[start] ^ kalyes[end]
        states_SGs.append(sg_val)
        
    kalyes[i] = MEX(set(states_SGs))

#Print first 100s
print(kalyes[:100])
