def intToRoman(num: int) -> str:
    unit=[["","I","II","III","IV","V","VI","VII","VIII","IX"],
    ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
    ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
    ["","M","MM","MMM"]]
    roman=""
    for i in unit:

        t=num%10
        num=int(num/10)
        roman=i[t]+roman

    return roman

print(intToRoman(1389))