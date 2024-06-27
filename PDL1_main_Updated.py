import numpy as np
import pandas as pd
import itertools
from itertools import combinations
from NSCLC_PDL1_one_fault import NSCLC_PDL1_one_fault
from NSCLC_PDL1_two_faults import NSCLC_PDL1_two_faults
from NSCLC_PDL1_three_faults import NSCLC_PDL1_three_faults
#import matplotlib.pyplot as plt

drugs = ['Osimertinib', 'Selpercatinib', 'Trastuzumab_deruxtecan', 'Savolitinib', 'Dabrafenib_Trametinib', 'Durvalumab', 'Alpelisib', 'Enzastaurin', 'Lumakras', 'RG7388', 'Ribociclib', 'STAT_Inhibitor', 'Everolimus', 'Lorlatinib']

#num_drugs = int(input("Enter the number of drugs in each combination (0-13): "))
num_drugs = n = 1 #number of drugs

A = np.zeros((49, 16384))

# "i" iterates over faults
for i in range (49): # goes from fault 0 to 41
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
                                                            m = 8192 * d1 + 4096 * d2 + 2048 * d3 + 1024 * d4 + 512 * d5 + 256 * d6 + 128 * d7 + 64 * d8 + 32 * d9 + 16 * d10 + 8 * d11 + 4 * d12 + 2 * d13 + d14 + 1
                                                            if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 <= n:
                                                                A[i,m] = NSCLC_PDL1_one_fault(i, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14)
                                                            

A = np.sum(A, axis=0)  # Summing the measures across all faults
mask = (A !=0)
A = A[mask] # Removing the zero columns
A = A / np.max(A) # Normalising the measure
A = A.reshape(-1,1) # Calculating Transpose of that matrix


# Overall measure for two fault network

#B = np.zeros((38, 38, 8193))

B = np.zeros((49, 49, 16384))

# Generate all possible combinations of drugs
#drug_combinations = list(itertools.product([0, 1], repeat=12))

# "i" and "j" iterate over faults
for i in range(49):
    for j in range(49):
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
                                                                m = 8192 * d1 + 4096 * d2 + 2048 * d3 + 1024 * d4 + 512 * d5 + 256 * d6 + 128 * d7 + 64 * d8 + 32 * d9 + 16 * d10 + 8 * d11 + 4 * d12 + 2 * d13 + d14 + 1
                                                                if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 <= n:
                                                                    B[i,j,m] = NSCLC_PDL1_two_faults(i, j, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14)
                                                            

#B = np.sum(np.sum(B, axis=0), axis=0)  # Summing the measures across all faults
#B = B[:, np.any(B, axis=1)]  # Removing the zero columns
#B = B / np.max(np.abs(B))  # Normalizing the measure
#B = np.transpose(B)

B = np.sum(np.sum(B, axis=0), axis=0)  # Summing the measures across all faults
mask = (B !=0)
B = B[mask] # Removing the zero columns
B = B / np.max(B) # Normalising the measure
B = B.reshape(-1,1) # Calculating Transpose of that matrix


'''
B = B[np.newaxis, :]  # Adding a new axis to make it 
B = B[:, np.any(B, axis=0)]  # Removing the zero columns 
B = B / np.max(np.abs(B))  # Normalizing the measure
B = np.transpose(B)  # Transposing to 
'''
#C = np.zeros((38, 38, 38, 8193))

C = np.zeros((49, 49, 49, 16384))
# Generate all possible combinations of drugs
#drug_combinations = list(itertools.product([0, 1], repeat=12))

# "i", "j", "k" iterate over faults
for i in range(49):
    for j in range(49):
        for k in range(49):
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
                                                                    m = 8192 * d1 + 4096 * d2 + 2048 * d3 + 1024 * d4 + 512 * d5 + 256 * d6 + 128 * d7 + 64 * d8 + 32 * d9 + 16 * d10 + 8 * d11 + 4 * d12 + 2 * d13 + d14 + 1
                                                                    if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 <= n:
                                                                        C[i,j,k,m] = NSCLC_PDL1_three_faults(i, j, k, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14)
                                                            

C = np.sum(np.sum(np.sum(C, axis=0), axis=0), axis=0)  # Summing the measures across different faults 
mask = (C !=0)
C = C[mask] # Removing the zero columns
C = C / np.max(C) # Normalising the measure
C = C.reshape(-1,1) # Calculating Transpose of that matrix

'''
C = C[np.newaxis, :]  # Adding a new axis to make it 
C = C[:, np.any(C, axis=0)]  # Removing the zero columns 
C = C / np.max(np.abs(C))  # Normalizing the measure
C = np.transpose(C)  # Transposing 
'''


if num_drugs < 0 or num_drugs > 14:
    print("Invalid input. Please enter a number between 0 and 14.")
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
    
    
    
    
    
    
''' 
    # Generate combinations of drugs
    combinations_list = []
    total_drugs = len(drugs)
    for n_value in range(n, -1, -1):
        temp_list = []
        for i in range(total_drugs):
            for j in range(total_drugs - 1, i - 1, -1):
                if j - i + 1 == n_value:
                    combination = ",".join(drugs[i:j + 1])
                    temp_list.append(combination)
        combinations_list.extend(reversed(temp_list))      
    print(combinations_list)
    # Create a DataFrame for each combination
    dfs = []
    for i, combination in enumerate(combinations_list):
        if i == 0:
            combination = ('Untreated',)
        df = pd.DataFrame({'Drugs': combination})
        dfs.append(df)
        #print(combination)
        output_one_fault = np.column_stack((combinations_list, A))
        output_two_faults = np.column_stack((combinations_list, B))
        output_three_faults = np.column_stack((combinations_list, C))
        #print(output_one_fault)
        #print(output_two_faults)
        #print(output_three_faults)

    #result_df = pd.concat(dfs, ignore_index=True)
    #print(result_df)
'''
