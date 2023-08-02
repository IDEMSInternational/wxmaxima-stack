# Importing required libraries
import pygsheets

gss_name = "PRO-RUWA missing_values_1_data"

# <---------- SET UP ------------->

# Open the question bank
client = pygsheets.authorize(service_account_file="C:/Users/James/OneDrive/Documents/008_VisualStudio/IDEMS/Quesiton-Bank-manager/service_account.json")
gss_question_bank = client.open(gss_name)
gws_question_bank = gss_question_bank.worksheet("title", "Sheet1")

# Download question headers, question codes and data
question_bank_data = gws_question_bank.get_values(start="A1", end="I101")

with open("missing_values_1_database.wxm", "w") as database:
    database.write("[")
    for line in question_bank_data:
        database.write(str(line) + ",\n")
    database.write("];")
