import nltk
import string
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import locale

pdf_using = "/Users/alexanderadams/hiddenfees/preprocess_model/ADP_MacFarlane.txt"

with open(pdf_using) as f:
    texts = f.readlines()

text = ''
for i in range(len(texts)):
    text = text + texts[i]

words = word_tokenize(text)
sentences = sent_tokenize(text)
text = text.lower()

def find_each_variable(name_of_variable):
    index = text.find(name_of_variable)
    start = index + len(name_of_variable)
    string_number = ''
    f = 0
    while f != 1:
        if text[start] == "$":
            start = start + 1
        elif text[start] == ",":
            start = start + 1
        elif text[start] == "0":
            string_number = string_number + text[start]
            start = start + 1 
        elif text[start] == "1": 
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "2":
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "3":
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "4":
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "5":
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "6": 
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "7": 
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "8": 
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == "9":
            string_number = string_number + text[start]
            start = start + 1
        elif text[start] == ".":
            string_number = string_number + text[start]
            start = start + 1
        else:
            f = f + 1
    number = float(string_number)
    return number

plan_asset = find_each_variable("plan assets: ")
total_plan_asset = float("2953655.05") #find_each_variable("total plan assets (minus loans) as of 07/31/18 ")
average_compensation = float(".0050") #find_each_variable("total asset weighted average compensation to adp for services to investment funds ")
weighted_average = float(".0078") #find_each_variable("total asset weighted average net expense ratio ")
monthly_fee = find_each_variable("total monthly plan-level processing fees: ") + find_each_variable("total monthly plan-level optional service fees: ")
annual_rk = monthly_fee * 12
total_investment = total_plan_asset + average_compensation
net_investment = total_plan_asset * weighted_average
revenue_share = total_plan_asset * average_compensation
total_investment = net_investment + revenue_share
total = annual_rk + total_investment
print(total)
name_index = text.find("401(k)")
name_string = text[0:name_index - 1]
locale.setlocale( locale.LC_ALL, '' )
print("The toal cost of 401(k) fees for " + name_string.upper() + "  is: " + str(locale.currency(total, grouping = True)))









