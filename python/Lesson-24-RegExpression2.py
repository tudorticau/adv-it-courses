# import bibliography for regex
import re
# ---- Text where python will looking for ----------
mytext = " Quon Phillips, tempor.diam.dictum@icloud.edu Hope Carey, facilisis@yahoo.net Norman Griffin,vulputate.lacus@outlook.org," \
         " Germane Vaughan,sagittis@hotmail.org Yael Fleming,magna.tellus.faucibus@google.org" \
         " Quon Phillips,(723) 464-1191,Jan 1, 2022 Hope Carey,1-312-473-9945,Nov 18, 2022" \
         " Norman Griffin,1-728-660-1642, Aug 13, 2023 Germane Vaughan,(686) 883-9870,Jan 29, 2022" \
         " Yael Fleming,1-281-625-7142,Dec 21, 2022"
"""
\d = Any Digit 0-9
\D = Any non DIGIT
\w = Any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\. = .
\s = breakspace
\S = non breakspace
"""

# ---- program to find all emails ----
textlookfor = r"\w+@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)
print("-------------------------------------------")