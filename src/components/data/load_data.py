import pandas as pd


#########  data ########

class COLNAMES:
    l_col_id = ['Cleaned Parent Customer']

    # data1 features for clustering
    l_col_firm = ['Primary Gnostic', 'Primary End Mkt Segment', 'Primary End Market Sub Segment' , 'Primary End Mkt Group' , 'Industry (3P)'  , 'Sub Industry (3P)']
    A = 'A'
    A_count=['A_count']
    SF_indx='Strong_firm_neighbs_indx'
    SP_indx='Strong_prod_neighbs_indx'
    GF_indx='Good_firm_neighbs_indx'
    GP_indx='Good_prod_neighbs_indx'
    AF_indx='Average_firm_neighbs_indx'
    AP_indx='Average_prod_neighbs_indx'
    WF_indx='Weak_firm_neighbs_indx'
    WP_indx='Weak_prod_neighbs_indx'
    l_col_firm_indx = [SF_indx,GF_indx, AF_indx, WF_indx]
    l_col_portf_indx = [ SP_indx,  GP_indx,  AP_indx,  WP_indx]

    S_recom='Strong_recom_All'
    S_recom_count='S.All_no'
    G_recom='Good_recom_All'
    G_recom_count='G.All_no'
    A_recom='Average_recom_All'
    A_recom_count='A.All_no'
    W_recom='Weak_recom_All'
    W_recom_count='W.All_no'
    l_col_recom=[S_recom,S_recom_count,G_recom,G_recom_count,A_recom,A_recom_count,W_recom,W_recom_count]



# def TFC_output() -> pd.DataFrame:
#     path='C:/Users/jrizk/OneDrive - Analog Devices, Inc/Documents/My AD Folder/01.TFC Model/Recommendation_Engine_Code/Output/'
#     data = pd.read_csv(path +'TFC_output_Allinfo.csv')
#     # path = "./components/data/TFC_output_Allinfo.csv"
#     # data = pd.read_csv(path)
#     return data







