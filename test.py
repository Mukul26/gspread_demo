from http import client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("test_sheet")

#selecting a worksheet by  name

worksheet = sheet.worksheet('Mukul')
data = worksheet.get_all_records()
pprint(data)

###############creating a new worksheet
sheet.add_worksheet(title="Aswal", rows='100',cols='20')

###############Deleting a worksheet
aswal = sheet.worksheet('Aswal')
sheet.del_worksheet(aswal)

#########Getting a cell value

first_sheet = sheet.worksheet('Sheet1')
first_sheet.update('B8','kk')
print(first_sheet.acell('B1').value)
