import csv
import re
from datetime import datetime

def loader_func(pth):
    tmp_lst = []
    with open(pth, 'r') as f_obj:
        rdr = csv.DictReader(f_obj)
        for r in rdr:
            tmp_lst.append(r)
    return tmp_lst

def func_alpha_9(v_list):
    """Scrubs the applicant data for the metrics engine."""
    res_arr = []
    for idx in range(len(v_list)):
        cur_r = v_list[idx]
        
        # --- Email Validation ---
        eml = cur_r['Email']
        eml_regex = r"^[a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        if not re.match(eml_regex, eml):
            continue 
            
        # --- Date Formatting ---
        dt_str = cur_r['Date_of_Birth']
        try:
            dt_obj = datetime.strptime(dt_str, "%Y-%m-%d")
            cur_r['Date_of_Birth'] = dt_obj.strftime("%Y-%m-%d")
        except:
            pass
        try:
            dt_obj = datetime.strptime(dt_str, "%d-%m-%Y")
            cur_r['Date_of_Birth'] = dt_obj.strftime("%d-%m-%Y")
        except:
            pass
        # --- Score Cleanup ---
        scr = cur_r['AI_Score']
        if scr=='' or scr=='null':
            continue
            
        res_arr.append(cur_r)
        
    return res_arr
