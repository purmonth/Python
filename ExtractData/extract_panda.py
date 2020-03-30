import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import load_workbook
import openpyxl

testList = [
    "DealNumber",
    "TargetImmediateParentPublicStatus"
]

wordList = [
"TargetIndustrySector",                             	
"HighTechIndustry",                   	
"TargetState",       
"AcquirorIndustrySector",                           
"AcquirorPrimarySICCode",
"HighTechIndustry", 	
"AcquirorState",     	
"Status",   
"%ofSharesAcq.",	  
"%OwnedAfterTransaction",       	  
"%Sought",
"ValueofTransaction($mil)",
"Premium1DaypriortoannouncementData",
"Premium1WeekpriortoannouncementData",
"Premium4WeekspriortoannouncementData"
]

wordList2 = [
"AcquirorCUSIP",                     
"AcquirorBookValueLTM($Mil)",  	
"AcquirorCashLTM($Mil)",     
"AcqClosing1DayPriortoAnn($)",          	
"AcqClosing1WeekPriortoAnn($)", 	
"AcqClosing4WeeksPriortoAnn($)", 	
"AcqCommonSharesLTM(mil)",    	
"AcqCommonEquityLTM($mil)",    	
"AcqCurrAssetsLTM($Mil)",  	
"AcqCurrLiabilitiesLTM($mil)",	
"AcqEarningsPerShareLTM($)",         	 
"AcqEBITLTM($mil)",             	
"AcqEBITDALTM($mil)",        	
"AcqIndustrySectorCode",	
"AcqNAICCode",       	 
"AcqNetAssets($mil)",          	
"Acquiror'spricepershare",	
"AcquirorState",     	
"AcquirorStateRegionCode",   	
"AcquirorClosingPrice1DayAfterAnnDate($)",	
"AcquirorClosingPrice1WeekAfterAnnDate($)",	
"AcquirorClosingPrice4WeeksAfterAnnDate($)",	
"AcquirorClosingPriceatAnn($)",	
"AcqTickerSymbol",	
"AcqZipCode",       	
"Intrastate",  	
"TargetCUSIP",  	
"TargetIndustrySectorCode",                           	
"TargetNAICCode",	
"TargetZipCode",
]


def read_excel(filename, nrows):
    # Parameter `read_only=True` leads to excel rows only being loaded as-needed
    book = openpyxl.load_workbook(filename=filename, read_only=True, data_only=True)
    first_sheet = book.worksheets[0]
    rows_generator = first_sheet.values

    header_row = next(rows_generator)
    data_rows = [row for (_, row) in zip(range(nrows - 1), rows_generator)]
    return pd.DataFrame(data_rows, columns=header_row)



#change NameOfTheSheet with the sheet name that includes the data
for i in range(1997, 2019):
    df = pd.DataFrame()
    print("US"+str(i))
    print("Loading 1")
    data1 = pd.read_excel("/Users/hung-yuehlin/Python/ExtractData/US"+str(i)+"-1.xlsx", sheet_name=0)
    for col in data1.columns:
        if(col.replace(" ","").replace("\n","") in wordList):
            coldata = data1[col]
            df2 = pd.DataFrame(coldata)
            df = pd.concat([df,df2],axis=1)
    print("Loading 2")
    data2 = pd.read_excel("/Users/hung-yuehlin/Python/ExtractData/US"+str(i)+"-2.xlsx", sheet_name=0)
    for col in data2.columns:
        if(col.replace(" ","").replace("\n","") in wordList2):
            coldata = data2[col]
            df2 = pd.DataFrame(coldata)
            df = pd.concat([df,df2],axis=1)
        
    print("Converting")
    #save it to the 'NewSheet' in destfile
    df.to_excel("/Users/hung-yuehlin/Python/ExtractData/US"+str(i)+"_done.xlsx", sheet_name='Sheet1')
    