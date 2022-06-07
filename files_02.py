fname = input("enter file name: \n")
try:
    fhandle = open(fname, "r")
except:
    print("File cannot be opened:", fname)
    exit()
count = 0
spam_confidence = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence"):
        col_pos = line.find(" ")
        extracted_num = line[col_pos+1:]
        spam_confidence += float(extracted_num)
        count += 1
average_spam_confidence = spam_confidence / count
print(f"Average spam confidence: {average_spam_confidence:.3f}")
