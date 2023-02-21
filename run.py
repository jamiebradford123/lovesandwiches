import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    get sales data figures input form user
    """
    print("Please enter sales data from todays sales")
    print("Data should be six numbers and seperated by commas")
    print("Example: 1,2,3,4,5,6\n")

    data_str = input("Enter your data here: ")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    convert all string values to integers, raise error if strings cannot be converted, 
    or there isnt exaxtly six values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you entered {len(values)}"
            )

    except ValueError as e:
        print(f"invalid data: {e}, please try again")

get_sales_data()