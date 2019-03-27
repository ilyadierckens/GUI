import write
import time

c1V = 20
c1A = 10
psV = 1
psA = 2
luV = 6
luA = 7
ldV = 2
ldA = 3
tuV = 3
tuA = 5
tdV = 7
tdA = 2


while 1:
    write.updatemetingen(c1V,c1A,psV,psA,luV,luA,tuV,tuA,ldV,ldA,tdV,tdA)
    time.sleep(1)
