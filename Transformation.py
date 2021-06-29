flag = "whatever you want to encrypt"
L = []
for i in range(0, len(flag), 2):
    L.append(chr((ord(flag[i]) << 8) + ord(flag[i + 1])))
    
''.join(L)

#This code basically takes two characters and stores them alongside each other in binary. To give an decimal eqivalent exaple of this, 111<<3 becomes 111000.
#111000+108=111108, as you can see no data is actually lost. if you do 111108>>3, you get 111. The 108 is dropped. 
#So basically all you have to do is to to write that 111 down, and subtract 111000 from 111108, and write that result down. Rinse and Repeat.
#Please consider to write down your own code with the new information above.






#SPOILERS AGEAD!!!











enc = "椧洠湯琠杯湮愠摯\u2061汬⁴桥⁷潲欠景爠祯甮⸮"
D = list(enc)
d = []
for i in D:
    d.append(chr(ord(i)>>8))
    d.append(chr((ord(i))-((ord(i)>>8)<<8)))
''.join(d)
