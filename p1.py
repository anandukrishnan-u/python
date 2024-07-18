#!/bin/python3


# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    m=max(candles)
    c=0
    for i in candles:
        if m==i:
            c+=1
    return c

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input())

    candles = list(map(int, input().split()))

    result = birthdayCakeCandles(candles)
    print(result)

  #  fptr.write(str(result) + '\n')

   # fptr.close()
