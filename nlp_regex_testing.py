import re

def test_regex(pattern, msg):
    x=re.search(pattern,msg)
    try:
        print("match: %s"%x.group())
    except AttributeError:
        print("not matched: %s"%msg)

###############################################################################
# birthday
pattern_old = "^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)([1-9]|1[0-2])(.|-|)(20|19)[0-9][0-9]$"
pattern = "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-|/)([1-9]|0[1-9]|1[0-2])(.|-|)(20|19|)[0-9][0-9]"

birthdates = [ "13-11-1917", "13.11.1917", "13.10.2007", "1.11.2027", "1.1.1977", "01.1.1977"
               , "01.01.1977", "4.5.1999", "4.5.99", "4.5.1899", "3/4/56", "4-5-86"
]
for datestring in birthdates:
    test_regex(pattern, msg = datestring)
###############################################################################
# policy no
pattern = "[0-9]{4,6}"

list_no = ["30000", "42459 ", "453922"]

for _str in list_no:
    test_regex(pattern = pattern, msg = _str)
###############################################################################
pattern = "[fF]ahrrad"  #trailing whitespace: Distinguish from Fahrradversicherung?


list_rad = ["Fahrrad ", "Fahrrades ", "fahrrads ", "Fahrrads "]

for _str in list_rad:
    test_regex(pattern, msg = _str )


pattern = "[fF]ahrradversicherung(..|)"

list_versicherung = ["Fahrradversicherung", "fahrradversicherungen", "Fahrrad", "Fahrraddiebstahl"]

for _str in list_versicherung:
    test_regex(pattern, msg = _str )

pattern = "[Dd]iebstahl"

list_versicherung = ["diebstahl", "Diebstahl", "Diebstahl", "Fahrraddiebstahl"]

for _str in list_versicherung:
    test_regex(pattern, msg = _str )


