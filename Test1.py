
def minimalsumofdigits(number):
    digits = splitintegerintodigits(number)
    digitssum = sumofdigits(digits)
    lengthofnumber = len(digits)
    minnumberarray = smallestnumberoflengthandsumandbiggerthan(lengthofnumber,digitssum,digits)
    minnumber = arrayofintstointeger(minnumberarray)
    if int(minnumber)!=number :
        return minnumber
    else:
        return -1

def smallestnumberoflengthandsumandbiggerthan(length,sum,numberarray):
    morenaughts = False
    position = -1
    for count in range(length-1,0,-1): #loops from end to front of digits
        if numberarray[count]==0 : #skip if digit is 0
            continue
        elif numberarray[count-1]==0 and morenaughts==False : #if next number is 0 and 2nd next number is not 0
            numberarray[count-1]=numberarray[count-1]+1 #next number +1
            temp = numberarray[count]
            numberarray[count]=0 #this number becomes 0
            for count2 in range(length-1,0,-1): #finds position of first digit that is not 9 from end to front
                if numberarray[count2]!=9 :
                    position = count2
                    break

            if position!=-1 : #adds value of digit before 0 to first digit which isnt 9
                numberarray[position] = numberarray[position] + temp - 1
                break

            if numberarray[count-2]==0:
                morenaughts = True
            continue
        else:
            if morenaughts==False :
                if numberarray[count-1]!=9 :
                    numberarray[count]=numberarray[count]-1
                    numberarray[count-1]=numberarray[count-1]+1
                    break

            continue
    return numberarray




def splitintegerintodigits(number):
    arrayofdigits =[]
    for digit in str(number):
        arrayofdigits.append(int(digit))
    return arrayofdigits

def sumofdigits(digits):
    sum1 = 0
    for digit in digits:
        sum1 = sum1 + digit
    return sum1

def arrayofintstointeger(arrayofdigits):
    minnumberstring = ""
    for digit in arrayofdigits:
        minnumberstring = minnumberstring + str(digit)
    return int(minnumberstring)


def test():
    assert minimalsumofdigits(123)==132
    assert minimalsumofdigits("0200")==1001
    assert minimalsumofdigits(90) == -1
    assert minimalsumofdigits(9999) == -1
    assert minimalsumofdigits("09999999999999") == 18999999999999
    assert minimalsumofdigits("0508")==517

    print("all tests passed")

if __name__ == '__main__':
    test()