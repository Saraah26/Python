import re
text = "Items Processed : TX123, AB456, za789"
pattern = r"[A-Z]{2}\d{3}"
matches = re.findall(pattern,text)
print(matches)

import re
text = "The order number is TX902 and the shipping code is NY087"
pattern  = r"[A-Z]{2}\d(3)"
matches = re.findall(pattern,text)
print(matches)

import re
filename1= "report.csv"
pattern =r"^(.+)\.([a-z]+)$"

match = re.search(pattern , filename1)

if match:
    print("Full match:",match.group(0))
    print("File name:", match.group(1))
    print("Extension:", match.group(2))
