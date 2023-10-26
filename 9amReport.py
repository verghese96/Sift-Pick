import csv # import csv module
import pandas as pd
import os #File reading module

#user selection interface modules
from tkinter import Tk,messagebox 
from tkinter.filedialog import askopenfilename

#User selects CSV file. Checks if CSV.
ALLOWED_EXTENSTIONS = {".csv"}
while True:
    messagebox.showinfo("Morning!", "Please select a CSV extension file.")
    filename = askopenfilename()
    extension = os.path.splitext(filename)[1]
    if extension in ALLOWED_EXTENSTIONS:
        break
 
#create the dataframe for manipulation with pandas
df = pd.read_csv(filename)
#print(df.columns = df.columns.str.replace(' ', '_')) #replace column name spaces to underscore for the 2 columns

#change spaces in headers to "_"


#delete empty value cell in column "Payment Gateway"

#delete "direct" values in column "Merchant Commission Type"
#print(df.MerchantCommissionType.to_string(index=False))

#Desired output data
