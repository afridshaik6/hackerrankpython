def birthdayCakeCandles(candles):
    # Write your code here
    sample = 0
    p = max(candles)
    for i in candles:
        if p == i:
            sample += 1
    print(sample)


birthdayCakeCandles([3 ,2,1,3])
