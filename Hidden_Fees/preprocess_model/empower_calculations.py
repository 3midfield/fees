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

def find_percent(text, index):
    if index != -1:
        substring = text[index:]

        # Split the substring by whitespace and look for a numerical value
        for word in substring.split():
            if  '%' in word:
                number = word
                # print(f"Number associated with key: {number}")
                number = number.replace('%', '').replace(',', '')
                return number
    else:
        return 0

def parse_empower(text):
    plan_assets = float(find_value(text, text.find('Total Assets')))
    print(plan_assets)
    participants = float(find_value(text, text.find('Number of Participants')))
    print(participants)
    assets_minus_loans = float(find_value(text, text.find('Participant Assets')))
    print(assets_minus_loans)
    rev_share_percent = float(0)
    print(rev_share_percent)
    net_investments_percent = float(find_percent(text, text.find('Payments to Investment Providers (IP) (Q)')))/100 #How to make it look up and get the percent value after
    print(net_investments_percent)

    # print(annual_rk)
    net_investments = net_investments_percent * plan_assets
    print(net_investments)
    
    # print(net_investments)
    rev_share =  rev_share_percent * plan_assets
    print(rev_share)
    total_investments = net_investments + rev_share
    print(total_investments)
    
    total_cost = total_investments
    print(total_cost)
    rounded_number = round(total_cost, 2)
    print(rounded_number)
    return rounded_number
    
    # monthly_rk = float(find_value(text, text.find('Administrative Services Fees:')))
    # print(monthly_rk)