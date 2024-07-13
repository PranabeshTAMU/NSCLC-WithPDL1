mport numpy as np
import pandas as pd
import itertools
from itertools import combinations
from NSCLC_PDL1_one_fault import NSCLC_PDL1_one_fault
from NSCLC_PDL1_two_faults import NSCLC_PDL1_two_faults
from NSCLC_PDL1_three_faults import NSCLC_PDL1_three_faults
#import matplotlib.pyplot as plt

drugs = ['Osimertinib', 'Selpercatinib', 'Trastuzumab_deruxtecan', 'Savolitinib', 'Dabrafenib', 'Durvalumab', 'Trametinib', 'Alpelisib', 'Enzastaurin', 'Lumakras', 'RG7388', 'Ribociclib', 'STAT_Inhibitor', 'Everolimus', 'Lorlatinib', 'MK2206']

num_drugs = n = 4 #number of drugs

A = np.zeros((43, 65536))

# "i" iterates over faults
for i in range (43): # goes from fault 0 to 41
    for d1 in range(2):
        for d2 in range(2):
            for d3 in range(2):
                for d4 in range(2):
                    for d5 in range(2):
                        for d6 in range(2):
                            for d7 in range(2):
                                for d8 in range(2):
                                    for d9 in range(2):
                                        for d10 in range(2):
                                            for d11 in range(2):
                                                for d12 in range(2):
                                                    for d13 in range(2):
                                                        for d14 in range(2):
                                                            for d15 in range(2):
                                                                for d16 in range(2):
                                                                   m = 32768 * d1 + 16384 * d2 + 8192 * d3 + 4096 * d4 + 2048 *  d5 + 1024 * d6 + 512 * d7 + 256 *  d8 + 128 * d9 + 64 * d10 + 32 * d11 + 16 *  d12 + 8 *d13 + 4 *  d14 + 2 *d15 + d16+ 1
                                                                   if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 + d15 + d16<= n:
                                                                       A[i,m] = NSCLC_PDL1_one_fault(i, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16)
                                                            

A = np.sum(A, axis=0)  # Summing the measures across all faults
mask = (A !=0)
A = A[mask] # Removing the zero columns
A = A / np.max(A) # Normalising the measure
A = A.reshape(-1,1) # Calculating Transpose of that matrix


# Overall measure for two fault network

B = np.zeros((43, 43, 65536))

# Generate all possible combinations of drugs
#drug_combinations = list(itertools.product([0, 1], repeat=12))

# "i" and "j" iterate over faults
for i in range(43):
    for j in range(43):
        for d1 in range(2):
            for d2 in range(2):
                for d3 in range(2):
                    for d4 in range(2):
                        for d5 in range(2):
                            for d6 in range(2):
                                for d7 in range(2):
                                    for d8 in range(2):
                                        for d9 in range(2):
                                            for d10 in range(2):
                                                for d11 in range(2):
                                                    for d12 in range(2):
                                                        for d13 in range(2):
                                                            for d14 in range(2):
                                                                for d15 in range(2):
                                                                    for d16 in range(2):
                                                                        m = 32768 * d1 + 16384 * d2 + 8192 * d3 + 4096 * d4 + 2048 *  d5 + 1024 * d6 + 512 * d7 + 256 *  d8 + 128 * d9 + 64 * d10 + 32 * d11 + 16 *  d12 + 8 *d13 + 4 *  d14 + 2 *d15 + d16+ 1
                                                                        if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 + d15+ d16<= n:                                                        
                                                                            B[i, j, m] = NSCLC_PDL1_two_faults(i, j, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16)


B = np.sum(np.sum(B, axis=0), axis=0)  # Summing the measures across all faults
mask = (B !=0)
B = B[mask] # Removing the zero columns
B = B / np.max(B) # Normalising the measure
B = B.reshape(-1,1) # Calculating Transpose of that matrix


C = np.zeros((43, 43, 43, 65536))
# Generate all possible combinations of drugs
#drug_combinations = list(itertools.product([0, 1], repeat=12))

# "i", "j", "k" iterate over faults
for i in range(43):
    for j in range(43):
        for k in range(43):
            for d1 in range(2):
                for d2 in range(2):
                    for d3 in range(2):
                        for d4 in range(2):
                            for d5 in range(2):
                                for d6 in range(2):
                                    for d7 in range(2):
                                        for d8 in range(2):
                                            for d9 in range(2):
                                                for d10 in range(2):
                                                    for d11 in range(2):
                                                        for d12 in range(2):
                                                            for d13 in range(2):
                                                                for d14 in range(2):
                                                                    for d15 in range(2):
                                                                        for d16 in range(2):
                                                                            m = 32768 * d1 + 16384 * d2 + 8192 * d3 + 4096 * d4 + 2048 *  d5 + 1024 * d6 + 512 * d7 + 256 *  d8 + 128 * d9 + 64 * d10 + 32 * d11 + 16 *  d12 + 8 *d13 + 4 *  d14 + 2 *d15 + d16+ 1
                                                                            if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 + d15+ d16<= n:                                                            
                                                                                C[i,j,k,m] = NSCLC_PDL1_three_faults(i, j, k, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16)

C = np.sum(np.sum(np.sum(C, axis=0), axis=0), axis=0)  # Summing the measures across different faults 
mask = (C !=0)
C = C[mask] # Removing the zero columns
C = C / np.max(C) # Normalising the measure
C = C.reshape(-1,1) # Calculating Transpose of that matrix

if num_drugs < 0 or num_drugs > 16:
    print("Invalid input. Please enter a number between 0 and 15.")
else:
    # Define the drug names
# Initialize the output list with 'Untreated'
    output_list = ["Untreated"]

# Iterate through the nested loops to generate drug combinations
    for d1 in range(2):
        for d2 in range(2):
            for d3 in range(2):
                for d4 in range(2):
                    for d5 in range(2):
                        for d6 in range(2):
                            for d7 in range(2):
                                for d8 in range(2):
                                    for d9 in range(2):
                                        for d10 in range(2):
                                            for d11 in range(2):
                                                for d12 in range(2):
                                                    for d13 in range(2):
                                                        for d14 in range(2):
                                                            for d15 in range(2):
                                                                for d16 in range(2):
                                                        # Create an empty combination
                                                                    combination = []

                                                        # Append individual drugs if the corresponding variable is 1
                                                                    if d1:
                                                                        combination.append(drugs[0])
                                                                    if d2:
                                                                        combination.append(drugs[1])
                                                                    if d3:
                                                                        combination.append(drugs[2])
                                                                    if d4:
                                                                        combination.append(drugs[3])
                                                                    if d5:
                                                                        combination.append(drugs[4])
                                                                    if d6:
                                                                        combination.append(drugs[5])
                                                                    if d7:
                                                                        combination.append(drugs[6])
                                                                    if d8:
                                                                        combination.append(drugs[7])
                                                                    if d9:
                                                                        combination.append(drugs[8])
                                                                    if d10:
                                                                        combination.append(drugs[9])
                                                                    if d11:
                                                                        combination.append(drugs[10])
                                                                    if d12:
                                                                        combination.append(drugs[11])
                                                                    if d13:
                                                                        combination.append(drugs[12])
                                                                    if d14:
                                                                        combination.append(drugs[13])                                                                     
                                                                    if d15:
                                                                        combination.append(drugs[14])
                                                                    if d16:
                                                                        combination.append(drugs[15])                                                                                         
                                                        # Add the combination to the output list with formatting
                                                                    if combination and len(combination) <= n:
                                                                        output_list.append("{}".format(' + '.join(combination)))
    combo_array = np.array(output_list)
# Print the output list
    #for combo in output_list:
        #print(combo)
    #output_one_fault = np.column_stack((combo_array, A))
    #output_two_faults = np.column_stack((combo_array, B))
    #output_three_faults = np.column_stack((combo_array, C))
    output = np.column_stack((combo_array, A, B, C))  
