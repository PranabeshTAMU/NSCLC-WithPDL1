import numpy as np
def NSCLC_PDL1_one_fault(fault1, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16):
#inputs 
    K_Ras = 0
    EGF = 0
    TGFalpha = 0
    HGF = 0
    KIF5B_RET = 0
    EML4ALK = 0
    DNA_Damage = 0
    P16 = 1
    PTEN = 1
    PAMP = 0

# Drugs
    Osimertinib=x1#Targets EGFR
    Selpercatinib=x2#=1 #Targets KIF5BRET
    Trastuzumab_deruxtecan=x3#Targets ERBB2
    Savolitinib=x4#Targets MET
    Dabrafenib=x5#=1 #Targets RAF
    Durvalumab=x6#Targets PD_L1
    Trametinib=x7#=1 #Targets MEK
    Alpelisib=x8#=1 #Targets PI3K
    Enzastaurin=x9#=1 #Targets PKC
    Lumakras=x10#=1 #Targets KRAS
    RG7388=x11#=1 #Targets MDM2
    Ribociclib=x12#=1 #Targets CDK4/6
    STAT_Inhibitor=x13#=1 #Targets STAT3/5
    Everolimus=x14#=1 #Targets mTOR
    Lorlatinib=x15#=1 #Targets EM4ALK
    MK2206 =x16#=1 #Targets AKT
    
    

    if fault1 == 1:
        EGFR = 1
    else:
        EGFR = int( EGF or TGFalpha)
    
    if fault1 == 2:
        ERBB2 = 1
    else:
        ERBB2 = int(EGF or TGFalpha)
    
    if fault1 == 3:
        MET = 1
    else:
        MET = int(HGF)
    
    if fault1 == 4:
        EML4ALK1 = 1
    else:
        EML4ALK1 = int(EML4ALK)
        
    if fault1 == 5:
        PTEN1 = 1
    else:
        PTEN1 = int(not PTEN)
    
    if fault1 == 6:
        KIF5BRET = 1
    else:
        KIF5BRET = int(KIF5B_RET)
        
    if fault1 == 7:
        PLCgamma = 1
    else:
        PLCgamma = int((EGFR and (not Osimertinib)) or (ERBB2 and (not Trastuzumab_deruxtecan)) or (MET and (not Savolitinib)) or (EML4ALK1 and (not Lorlatinib)))
       
    if fault1 == 8:
        GrB2 = 1
    else:
        GrB2 = int((EGFR and (not Osimertinib)) or (ERBB2 and (not(Trastuzumab_deruxtecan))) or (MET and (not Savolitinib)))
    
    if fault1 == 9:
        KRAS = 1
    else:
        KRAS = int(K_Ras)
        
    if fault1 == 10:
        PI3K = 1
    else:
        PI3K = int((ERBB2 and (not Trastuzumab_deruxtecan)) or (EGFR and (not Osimertinib)) or (MET and (not Savolitinib)) or (EML4ALK1 and (not Lorlatinib)) or (KRAS and (not Lumakras)))

    if fault1 == 11:
        SOS = 1
    else:
        SOS = int(GrB2)
    
    if fault1 == 12:
        DNA = 1
    else:
        DNA = int(DNA_Damage) 
    
    if fault1 == 13:
        PIP3 = 1
    else:
        PIP3 = int(PTEN1 or (PI3K and (not Alpelisib)))        

    if fault1 == 14:
        JAK3 = 1
    else:
        JAK3 = int((EML4ALK1 and (not Lorlatinib)) or (KIF5BRET and (not Selpercatinib)))      
    
    if fault1 == 15:
        
        PKC = 1
    else:
        PKC = int(PLCgamma)

    if fault1 == 16:
        PDK1 = 1
    else:
        PDK1 = int(PIP3)
        
    if fault1 == 17:
        RAS = 1
    else:
        RAS = int(SOS or (KIF5BRET and (not Selpercatinib)) or (EML4ALK1 and (not Lorlatinib)))
                 
    if fault1 == 18:        
        NORE1 = 0
    else:
        NORE1 = int(not ((KRAS or RAS) and (not Lumakras)))

    if fault1 == 19:
        RASSF1 = 0
    else:
        RASSF1 = int(not ((KRAS or RAS) and (not Lumakras)))
        
    if fault1 == 20:
        MST1 = 0
    else:
        MST1 = int(RASSF1 and NORE1)   
    
    if fault1 == 21:
        RAF = 1
    else:
        RAF = int((KRAS and (not Lumakras)) or (RAS and (not Lumakras)) or (PKC and (not Enzastaurin)))
        
    if fault1 == 22:
        TLR = 1
    else:
        TLR = int(PAMP)

    if fault1 == 23:
        TIRAP = 1
    else:
        TIRAP = int(TLR)

    if fault1 == 24:
        TRAF6 = 1
    else:
        TRAF6 = int(TIRAP)        
        
    if fault1 == 25:
        TRIF = 1
    else:
        TRIF = int(TLR)

    if fault1 == 26:
        STAT3by5 = 1
    else:
        STAT3by5 = int(JAK3 or (EGFR and (not Osimertinib)) or (ERBB2 and (not Trastuzumab_deruxtecan)) or (MET and (not Savolitinib)) or (KRAS and (not Lumakras)))
  
    if fault1 == 27:
        PKB_Akt = 1
    else:
        PKB_Akt = int(PIP3 or PDK1)

    if fault1 == 28:
        MEK = 1
    else:
        MEK = int(TRAF6 or (RAF and (not Dabrafenib))) 

    if fault1 == 29:
        ERK = 1
    else:
        ERK = int(MEK and (not Trametinib)) 
             
    if fault1 == 30:
        IKK = 1
    else:
        IKK = int(TRIF or (PKB_Akt and (not MK2206)))
        
    if fault1 == 31:
        NFAT = 1
    else:
        NFAT = int(ERK)  
        
    if fault1 == 32:         
        AP1 = 1
    else:
        AP1 = int(ERK)          
      
    if fault1 == 33:        
        NFKB = 1
    else:
        NFKB = int((PKB_Akt and (not MK2206)) or IKK) 
        
    if fault1 == 34:        
        PD_L1 = 1
    else:
        PD_L1 = int(AP1 or NFAT or (STAT3by5 and (not STAT_Inhibitor)) or NFKB or DNA)        
        
    if fault1 == 35:        
        RetinoicAcid = 1
    else:
        RetinoicAcid = int(DNA)        

    if fault1 == 36:        
        mTOR = 1
    else:
        mTOR = int(PKB_Akt and (not MK2206))                   

    if fault1 == 37:        
        MDM2 = 1
    else:
        MDM2 = int(DNA  or (PKB_Akt and (not MK2206)))                   

    if fault1 == 38:        
        P53 = 0
    else:
        P53 = int(not(MDM2 and (not RG7388)))       
        
    if fault1 == 39:
        FHIT = 0
    else:
        FHIT = int(P53 and (not AP1))       
             
    if fault1 == 40:
        P21 = 0
    else:
        P21 = int(P53)      

    if fault1 == 41:
        CyclinD1 = 1
    else:
        CyclinD1 = int((not RASSF1) or ERK or (STAT3by5 and (not STAT_Inhibitor)) or (not P16) or (not FHIT))   

    if fault1 == 42:
        CDK4by6 = 1
    else:
        CDK4by6 = int(CyclinD1 or (not P21) or (not P16))
        
    

        #return NSCLC_one_fault(fault1,x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)

    
    RARbeta =  int(RetinoicAcid)
    CD1 = int(CyclinD1)
    Rb = int(CDK4by6 and (not Ribociclib)) 
    S6K =  int(mTOR and (not Everolimus))
    BAD = int(not(PKB_Akt and (not MK2206)))
    CASP9 = int(not(PKB_Akt and (not MK2206)))
    Forkhead = int((not(PKB_Akt and (not MK2206))) and MST1)
    FHIT1 = int(FHIT)
    T_Cell = int(not(PD_L1 and (not Durvalumab)))


    output1 = [RARbeta, CD1, Rb, S6K, BAD, CASP9, Forkhead, FHIT1, T_Cell]
    #print(output1)
    output2 = [0,0,0,0,1,1,1,1,1]  # Ideal Output

    a = 0
    b = 0
    c = 0
    d = 0

    for i in range(9):
        if output1[i] == 1 and output2[i] == 1:
            a += 1
        elif output1[i] == 0 and output2[i] == 1:
            b += 1
        elif output1[i] == 1 and output2[i] == 0:
            c += 1
        elif output1[i] == 0 and output2[i] == 0:
            d += 1

    output = ((b + c) ** 2) / ((a + b + c + d) ** 2)
    return(output)
