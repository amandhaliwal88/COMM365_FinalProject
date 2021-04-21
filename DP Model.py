options = [0,1,2,3,4]
values =  [[23600,6540,1828,526,167],   #reward function
           [30419,8007,2124,579,174],
           [20085,5666,1612,473,153],
           [26513,7000,1862,510,154],
           [30293,8128,2198,612,188]]




def iterate ():
    comp = []
    for i in range(5):                  #recurssive iterations
        avail1 = pbv(options)
        currentops = []
        currentops.append(i)
        avail1.remove(i)
        for j in avail1:
            avail2 = pbv(avail1)
            currentops.append(j)
            avail2.remove(j)
            for k in avail2:
                avail3 = pbv(avail2)
                currentops.append(k)
                avail3.remove(k)
                for l in avail3:
                    avail4 = pbv(avail3)
                    currentops.append(l)
                    avail4.remove(l)
                    for m in avail4:
                        currentops.append(m)
                        comp.append(pbv(currentops))
                        currentops.remove(m)
                    currentops.remove(l)
                currentops.remove(k)
            currentops.remove(j)
        currentops.remove(i)
    return comp

def value (list):                   #calculated culmulative value of choices
    result = []
    for i in list:
        total = 0
        for k in range (len(i)):
            total  += values[i[k]][4-k]
        result.append(total)
    return result

        

def pbv (thelist):                  #pass by value
    newlist = []
    for i in thelist:
        newlist.append(i)
    return newlist

def main():
    sequence = iterate()
    print(sequence)
    thisvalue = value(sequence) 
    print (thisvalue)
    maximum = max(thisvalue)
    position = thisvalue.index(maximum)
    print (sequence[position])
    print (maximum)
    

if __name__ == "__main__":
    main()

        
