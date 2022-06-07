str = 'X-DSPAM-Confidence:0.8475'
col_index = str.find(":")
extracted_num = float(str[col_index+1:])
print(extracted_num)
