from fpdf import FPDF

# Create a PDF object
# pdf = FPDF()

# # Set font
# pdf.set_font("Arial", size=12)

def find_value(text, index):
    if index != -1:
        substring = text[index:]

        # Split the substring by whitespace and look for a numerical value
        for word in substring.split():
            if '$' in word or '%' in word or word.replace(',', '').replace('.', '').isdigit():
                number = word
                # print(f"Number associated with key: {number}")
                number = number.replace('$', '').replace('%', '').replace(',', '')
                return number
    else:
        return 0

def parse_adp(text):
    plan_assets = float(find_value(text, text.find('Plan Assets')))
    print(plan_assets)
    participants = float(find_value(text, text.find('Number of Participants')))
    print(participants)
    assets_minus_loans = float(find_value(text, text.find('Total Plan Assets (minus loans)')))
    print(assets_minus_loans)
    rev_share_percent = float(find_value(text, text.find('Services to Investment Funds')))/100
    print(rev_share_percent)
    net_investments_percent = float(find_value(text, text.find('Net Expense Ratio')))/100
    print(net_investments_percent)
    
    monthly_rk = float(find_value(text, text.find('Administrative Services Fees:')))
    print(monthly_rk)
    
    #Long Fence and Home - net investments percent is 0.0084 but in the model it is being calculated as 0.0081
    #Stedman West Interests - adding a nonexistent monthly rk value
    
    #PDF CODE
    # pdf = FPDF()
# Set font
    # pdf.set_font("Arial", size=12)
    # # Add a page
    # pdf.add_page()

# Set font
    
    # pdf.set_font("Arial", size=12)
    
    # text = "Fee Calculation"
    # pdf.cell(200, 10, txt=text, border= 'B', ln = 1, align = 'C')
    
    # text = "Participants: " + str(participants)
    # pdf.cell(200, 10, txt=text, ln=1)
    
    # text = "Total Plan Assets(minus loans): " + str(assets_minus_loans)
    # pdf.cell(200, 10, txt=text, ln=1)
    
    # text = "Revenue Share Percentage: " +  str(rev_share_percent)
    # pdf.cell(200, 10, txt=text, ln=1)
    
    # text = "Net Investments Percentage: " + str(net_investments_percent)
    # pdf.cell(200, 10, txt=text, ln=1)
    
    # pdf.output("new.pdf")
    # print('Pdf should be finished')
    annual_rk = monthly_rk * 12 
    print('Annual RK: ' + str(annual_rk))
    # print(annual_rk)
    net_investments = net_investments_percent * assets_minus_loans
    print(net_investments)
    
    # print(net_investments)
    rev_share =  rev_share_percent * assets_minus_loans
    print(rev_share)
    total_investments = net_investments + rev_share
    print(total_investments)
    
    total_cost = annual_rk + total_investments
    print(total_cost)
    rounded_number = round(total_cost, 2)
    print(rounded_number)
    return rounded_number
    # Save the PDF
    
    
# index = text.find('Plan Assets')
# if index != -1:
#     # Extract a substring starting from the index of "Plan Assets"
#     substring = text[index:]

#     # Split the substring by whitespace and look for a numerical value
#     for word in substring.split():
#         if word.replace(',', '').replace('.', '').isdigit():
#             number = word
#             print(f"Number found after 'Plan Assets': {number}")
#             break
        
# index = text.find('Number of Participants')

# if index != -1:
#     # Extract a substring starting from the index of "Plan Assets"
#     substring = text[index:]

#     # Split the substring by whitespace and look for a numerical value
#     for word in substring.split():
#         if word.replace(',', '').replace('.', '').isdigit():
#             number = word
#             print(f"Number found after 'Plan Participants': {number}")
#             break

# index = text.find('Administrative Services Fees:')

# if index != -1:
#     # Extract a substring starting from the index of "Plan Assets"
#     substring = text[index:]

#     # Split the substring by whitespace and look for a numerical value
#     for word in substring.split():
#         print(word)
#         if '$' in word or '%' in word or word.replace(',', '').replace('.', '').isdigit():
#             number = word
#             print(f"Number found after 'without loans': {number}")
#             break