# detects calendar date

import re


def dateDetection(inputDate):
    dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    mo = dateRegex.search(inputDate)

    day = mo.group(2)
    month = mo.group(1)
    year = mo.group(3)

    month_30 = ['04', '06', '09', '11']
    month_31 = ['01', '03', '05', '07', '08', '10', '12']

    # checks date and current month
    if month in month_31:
        if day <= '31':
            pass
        else:
            print("Invalid Date")
            return False
    elif month in month_30:
        if day <= '30':
            pass
        else:
            print("Invalid Date")
            return False
    elif month == '02':
        if int(year) % 4 == 0:
            if day <= '29':
                pass
            else:
                print("Invalid Date")
                return False
        elif int(year) % 4 != 0:
            if day <= '28':
                pass
            else:
                print("Invalid Date")
                return False
    else:
        print('incorrect Month .....')
        return False
    print("Valid")

# checks year and feb
