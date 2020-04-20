import os
import os.path as osp
import numpy as np
import pandas as pd 
from utilities import append_csv

def delete_file(fpath):
    ''' 
    Deletes fpath if it exists 
    '''
    if osp.exists(fpath):
        os.remove(fpath)


def form_list_of_dates(start_date, end_date):
    '''
    Prepare a list of dates including the start and end date.
    '''
    dates = pd.date_range(start=pd.to_datetime(start_date,  dayfirst=True), 
                    end=pd.to_datetime(end_date,  dayfirst=True), freq = 'D')
    dates = list(dates.strftime('%d-%m-%Y'))
    
    return dates


def get_raw_dataframe(date):
    '''
    Reads the raw excel for the specified date and returns a pandas df
    '''
    raw_xlsx_dname = 'raw_xlsx'
    cwd = os.getcwd()
    dir_name = osp.dirname(cwd)
    raw_xlsx_dpath = osp.join(dir_name, raw_xlsx_dname)
    fname = date + '.xlsx'
    fpath = osp.join(raw_xlsx_dpath, fname)
    df = pd.read_excel(fpath)
        
    return df


def get_positive_case_dataframe():
    
    processed_data_dname = 'processed_data'
    cwd = os.getcwd()
    dir_name = osp.dirname(cwd)
    processed_data_dpath = osp.join(dir_name, processed_data_dname)
    
    positive_case_fpath = osp.join(processed_data_dpath, 
                                   'positive_case_information.xlsx')
    
    df = pd.read_excel(positive_case_fpath, parse_dates=True)
    
    df['Positive Date'] = df['Positive Date'].dt.strftime('%d-%m-%Y')
    df['Negative Date'] = df['Negative Date'].dt.strftime('%d-%m-%Y').replace('NaT', '')
    df['Death Date'] = df['Death Date'].dt.strftime('%d-%m-%Y').replace('NaT', '')
    
    return df


def form_state_summary_header():
    '''
    Define the header for state summary file
    '''
    
    header = ['Date', 'State', 'State_Code', 'Confirmed', 'Active', 'Recovered',
              'Deceased', 'Under_Observation', 'Home_Isolation',
              'Symptomatic_Hospitalized','Symptomatic_Hospitalized_Today', 
              'Samples_Sent_For_Testing', 'Samples_Tested_Negative']
    return header 


def form_district_summary_header():
    '''
    Define the header for district summary file
    '''
    
    header = ['Date', 'State', 'State_Code', 'District', 'District_Code', 
              'Confirmed', 'Active', 
              'Recovered', 'Deceased', 'Under_Observation', 'Home_Isolation', 
              'Symptomatic_Hospitalized', 'Symptomatic_Hospitalized_Today']
    return header 


def tidy_list(ip):
    
    op = list() 
    for elem in ip:
        if np.isnan(elem):
            op += ['NA']
        else:
            op += [int(elem)]
            
    return op


def read_district_code_excel():
    
    # read district codes from district_code.xlsx
    processed_data_dname = 'processed_data'
    cwd = os.getcwd()
    dir_name = osp.dirname(cwd)
    processed_data_dpath = osp.join(dir_name, processed_data_dname)
    ip_fpath = osp.join(processed_data_dpath, 'district_code.xlsx')
    ip_df = pd.read_excel(ip_fpath)
    
    ip_df['District Code'] = ip_df['District Code'].astype(np.int)
    
    return ip_df


def add_district_code_col(district_df):
    
    ip_df = read_district_code_excel()
    num_district = 14
    for i in range(0, num_district):
        mask = district_df['District'] == ip_df['District'][i]
        district_df.loc[mask, 'District Code'] = np.int(ip_df['District Code'][i])
    
    district_df['District Code'] = district_df['District Code'].astype(int)

    return district_df # contains a new column 'District Code'


def kerala_state_summary(dates_list, fpath):
    
    state = 'Kerala'
    state_code = 32
    
    delete_file(fpath) # delete fpath if it exists 
    
    # form and write header to output file
    state_header = form_state_summary_header()
    append_csv(state_header, fpath)
    
    # initialize variables to calculate cumulative sum
    tot_crd = np.zeros(shape=(3), dtype=np.int) # confirmed, recovered, deaths
    
    # loop through the dates 
    for date in dates_list:
        op_row = [date, state, state_code]
        
        raw_df = get_raw_dataframe(date)
        raw_df_last_row = list(raw_df.iloc[-1])
        
        # today's confirmed, recovered, deaths
        today_crd = np.array(raw_df_last_row[7:], dtype=np.int)
        tot_crd += today_crd
        
        # tot_active = tot_crd[0] - tot_crd[1] - tot_crd[2]
        tot_active = np.matmul(tot_crd, np.array([1, -1, -1])) 
        
        temp_list = list(tot_crd)
        temp_list.insert(1, tot_active)
        
        op_row += temp_list
        
        UO_HI_SH_SHT_SSFT_STN = tidy_list(raw_df_last_row[1:7])
        op_row += UO_HI_SH_SHT_SSFT_STN
        
        append_csv(op_row, fpath)
    

def kerala_district_summary(dates_list, op_fpath):
    
    state = 'Kerala'
    state_code = 32
    num_district = 14
    
    dist_code_df = read_district_code_excel() # read district code
    
    delete_file(op_fpath) # delete fpath if it exists 
    
    # form and write header to output file
    state_header = form_district_summary_header()
    append_csv(state_header, op_fpath)
    
    # initialize variables to calculate cumulative sum of confirmed, recovered,
    # deaths
    tot_crd = np.zeros(shape=(num_district, 3), dtype=np.int) 

    # loop through the dates 
    for date in dates_list:
        
        raw_df = get_raw_dataframe(date)
        # loop through the districts 
        for i in range(0, num_district):
            op_row = [date, state, state_code, dist_code_df['District'][i], 
                      dist_code_df['District Code'][i]]
            
            district_row = list(raw_df.iloc[i])
        
            # today's confirmed, recovered, deaths
            today_crd = np.array(district_row[7:], dtype=np.int)
            tot_crd[i,:] += today_crd
        
            # tot_active = tot_crd[0] - tot_crd[1] - tot_crd[2]
            tot_active = np.matmul(tot_crd[i,:], np.array([1, -1, -1])) 
        
            temp_list = list(tot_crd[i,:])
            temp_list.insert(1, tot_active)
        
            op_row += temp_list
        
            UO_HI_SH_SHT = tidy_list(district_row[1:5])
            op_row += UO_HI_SH_SHT
        
            append_csv(op_row, op_fpath)

def kerala_positive_case_summary(op_fpath):
    
    delete_file(op_fpath) # delete fpath if it exists 
    
    pos_df = get_positive_case_dataframe() # positive cases df
    # extract first 5 cols: Patient ID, Positive Date, District, Negative Date,
    # Death Date
    op_df = pos_df.iloc[:,0:5]
    op_df = add_district_code_col(op_df)
    op_df = op_df[['Patient ID', 'District', 'District Code', 'Positive Date', 
             'Negative Date', 'Death Date']]
    op_df.columns = op_df.columns.str.replace(' ', '_')
    
    op_df.to_csv(op_fpath, index=False)


if __name__ == "__main__":
    
    start_date = "31-01-2020"
    end_date = "18-04-2020"
    dates_list = form_list_of_dates(start_date, end_date)
    
    kerala_state_summary(dates_list, 'kerala_state_summary.csv')
    kerala_positive_case_summary('kerala_positive_case_summary.csv')
    kerala_district_summary(dates_list, 'kerala_district_summary.csv')



