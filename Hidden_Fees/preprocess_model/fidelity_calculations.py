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

def parse_fidelity(text):
    plan_assets = float(find_value(text, text.find('Total Plan Assets')))
    print(plan_assets)
    participants = float(find_value(text, text.find('Total Plan Participants')))
    print(participants)
    #Dont know these values yet
    # assets_minus_loans = float(find_value(text, text.find('Total Plan Assets (minus loans)')))
    # print(assets_minus_loans)
    # rev_share_percent = float(find_value(text, text.find('Services to Investment Funds')))/100
    # print(rev_share_percent)
    # net_investments_percent = float(find_value(text, text.find('Net Expense Ratio')))/100
    # print(net_investments_percent)
    
    monthly_rk = float(find_value(text, text.find('Administrative Services Fees:')))
    print(monthly_rk)