bitcoin = int(input())
china = float(input())
commission = float(input())

total_bitcoin = bitcoin * 1168
total_china = china * 0.15
dolars = total_china * 1.76
euros = (total_bitcoin + dolars) / 1.95
commissions = (commission / 100) * euros
result = euros - commissions


print(f"{result:.2f}")