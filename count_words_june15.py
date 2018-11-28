
# coding: utf-8

# In[2]:


import os
import csv

total_dic = {}
doc_dic = {}
private_dic = {}
local_dic = {}

measure_dic = {}
tech_dic = {}
monitor_dic = {}
eval_dic = {}
evaluate_dic ={}
technology_dic = {}
quantify_dic = {}
monitoring_dic = {}
business_dic = {}

# NOV25 new stem words: company, companies, corporate, corporation, data, right, evaluation, civil society; 
company_dic = {}
companies_dic = {}
corporate_dic = {}
corporation_dic = {}
data_dic = {}
right_dic = {}
evaluation_dic = {}
civil_society_dic = {}


total_counts = {}
total_words_doc = 0

# This is the directory that has all the text files you want to count words in
indir = "/Users/xingsgalaxy/Desktop/Michelle/materials/Input/texts/2003"

outdir = "/Users/xingsgalaxy/Desktop/Michelle/materials/Output/2003/"

# Loop through all the files
for root, dirs, filenames in os.walk(indir):
    
#   For each file in folder
    for f in filenames:

# This is parsing the file name so you can save the counts with dame name
        if f == ".DS_Store":
            continue
        filename = indir + "/" + f
        print("working on " + f)
        for w in open(filename).read().split():
            total_words_doc += 1
            w = w.lower().rstrip('?:!.,);"').lstrip('(')
            if w in total_dic:
                total_dic[w] += 1
            else:
                total_dic[w] = 1
            
            if w in doc_dic:
                doc_dic[w] += 1
            else:
                doc_dic[w] = 1  
        name = f.split(".")
        name = name[0]
        name = name + '.csv'
        
#       Add filename and count to count file
        total_counts[name] = total_words_doc

#       Add local count to total file
        if "local" in doc_dic.keys():
            local_dic[name] = doc_dic['local']

#       Add private count to total file        
        if "private" in doc_dic.keys():
            private_dic[name] = doc_dic['private']
        
#       Add measure count to total file        
        if "measure" in doc_dic.keys():
            measure_dic[name] = doc_dic['measure']

#       Add tech count to total file        
        if "tech" in doc_dic.keys():
            tech_dic[name] = doc_dic['tech']

#       Add monitor count to total file        
        if "monitor" in doc_dic.keys():
            monitor_dic[name] = doc_dic['monitor']

#       Add eval count to total file        
        if "eval" in doc_dic.keys():
            eval_dic[name] = doc_dic['eval']

#       Add evaluate count to total file        
        if "evaluate" in doc_dic.keys():
            evaluate_dic[name] = doc_dic['evaluate']

#       Add technology count to total file        
        if "technology" in doc_dic.keys():
            technology_dic[name] = doc_dic['technology']            

#       Add qualify count to total file        
        if "quantify" in doc_dic.keys():
            quantify_dic[name] = doc_dic['quantify']

#       Add monitoring count to total file        
        if "monitoring" in doc_dic.keys():
            monitoring_dic[name] = doc_dic['monitoring']

#       Add business count to total file        
        if "business" in doc_dic.keys():
            business_dic[name] = doc_dic['business']

# NOV25 add new dictionaries: company, companies, corporate, corporation, data, right, evaluation, civil society;

#       Add company count to total file        
        if "company" in doc_dic.keys():
            company_dic[name] = doc_dic['company']

#       Add companies count to total file        
        if "companies" in doc_dic.keys():
            companies_dic[name] = doc_dic['companies']

#       Add corporate count to total file        
        if "corporate" in doc_dic.keys():
            corporate_dic[name] = doc_dic['corporate']

#       Add corporation count to total file        
        if "corporation" in doc_dic.keys():
            corporation_dic[name] = doc_dic['corporation']

#       Add data count to total file        
        if "data" in doc_dic.keys():
            data_dic[name] = doc_dic['data']

#       Add right count to total file        
        if "right" in doc_dic.keys():
            right_dic[name] = doc_dic['right']

#       Add evaluation count to total file        
        if "evaluation" in doc_dic.keys():
            evaluation_dic[name] = doc_dic['evaluation']

#       Add civil society count to total file        
        if "civil_society" in doc_dic.keys():
            civil_society_dic[name] = doc_dic['civil_society']

# # This will save the individual counts to a csv
#         with open(name, 'wb') as csv_file:
#             writer = csv.writer(csv_file)
#             for key, value in doc_dic.items():
#                writer.writerow([key, value])
        doc_dic.clear()
        total_words_doc = 0

# # This saves the total dictionary    
#     with open('total_counts.csv', 'wb') as csv_file:
#         writer = csv.writer(csv_file)
#         for key, value in total_dic.items():
#             writer.writerow([key, value])

# This saves the doc word counts to one file    
    with open(outdir+'total_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

        print("line 75" + str(total_counts))
        for key, value in total_counts.items():
            print(key + ": " + str( value))
            writer.writerow( [key, value] )  

# This saves the local counts to one file    
    with open(outdir+'local_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in local_dic.items():
            writer.writerow([key, value])

# This saves the private counts to one file    
    with open(outdir+'private_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in private_dic.items():
            writer.writerow([key, value])

# This saves the measure counts to one file    
    with open(outdir+'measure_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in measure_dic.items():
            writer.writerow([key, value])

# This saves the tech counts to one file    
    with open(outdir+'tech_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in tech_dic.items():
            writer.writerow([key, value])

# This saves the monitor counts to one file    
    with open(outdir+'monitor_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in monitor_dic.items():
            writer.writerow([key, value])

# This saves the eval counts to one file    
    with open(outdir+'eval_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in eval_dic.items():
            writer.writerow([key, value])  

# This saves the evaluate counts to one file    
    with open(outdir+'evaluate_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in evaluate_dic.items():
            writer.writerow([key, value]) 

# This saves the technology counts to one file    
    with open(outdir+'technology_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in technology_dic.items():
            writer.writerow([key, value])   

# This saves the quantify counts to one file    
    with open(outdir+'quantify_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in quantify_dic.items():
            writer.writerow([key, value])   

# This saves the monitoring counts to one file    
    with open(outdir+'monitoring_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in monitoring_dic.items():
            writer.writerow([key, value])   

# This saves the business counts to one file    
    with open(outdir+'business_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in business_dic.items():
            writer.writerow([key, value])  

# NOV25 create new files on: company, companies, corporate, corporation, data, right, evaluation, civil society;

# This saves the company counts to one file    
    with open(outdir+'company_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in company_dic.items():
            writer.writerow([key, value]) 

# This saves the companies counts to one file    
    with open(outdir+'companies_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in companies_dic.items():
            writer.writerow([key, value]) 

# This saves the corporate counts to one file    
    with open(outdir+'corporate_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in corporate_dic.items():
            writer.writerow([key, value]) 

# This saves the corporation counts to one file    
    with open(outdir+'corporation_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in corporation_dic.items():
            writer.writerow([key, value]) 

# This saves the data counts to one file    
    with open(outdir+'data_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in data_dic.items():
            writer.writerow([key, value]) 

# This saves the right counts to one file    
    with open(outdir+'right_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in right_dic.items():
            writer.writerow([key, value])

# This saves the evaluation counts to one file    
    with open(outdir+'evaluation_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in evaluation_dic.items():
            writer.writerow([key, value]) 

# This saves the civil society counts to one file    
    with open(outdir+'civil_society_word_counts.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in civil_society_dic.items():
            writer.writerow([key, value]) 