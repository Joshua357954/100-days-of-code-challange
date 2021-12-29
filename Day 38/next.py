import gspread
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials

#scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
scope=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("g-json.json",scope)
client = gspread.authorize(creds)
sheet= client.open("myworkout").sheet1

data=sheet.get_all_records()

sheet.append_row(["Joshua","benita","daddy"])


