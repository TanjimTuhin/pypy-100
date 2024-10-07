print('Welcome to the tip calculator!')
bill=float(input('what was the total bill? $'))
tip=int(input('how much tip would you like to give? 10,12 or 15?'))
split=int(input('how many people to split the bill?'))
pay=(bill+(tip/100))/split
xpay=round(pay,2)
print(f"each person should pay: ${xpay}")