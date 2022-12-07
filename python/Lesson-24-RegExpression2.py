# import bibliography for regex
import re
# ---- File where python will looking for ----------
input_filename = "random_data.txt"
result_filename = "results_data.txt"
inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()

# ---- program to find all emails ----
lookfor = r"[\w.-]+@[\w.-]+"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)



print("-------------------------------------------")