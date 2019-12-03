import pandas as pd
import re
from Bio.Seq import Seq

def NGG_list_up_internal(sequence, strand):
    
    pattern="(?=([ATCG]{21}GG))"
    
    result_list = []
    for m in re.finditer(pattern, sequence):
        sgRNA = m.group(1)[:20]
        pam = m.group(1)[20:]
        position = m.start()
        
        result_list.append([strand, sgRNA, pam, position])
        
    return result_list


def NGG_list_up(sequence, name):

    positive_seq = sequence
    negative_seq = str(Seq(sequence).complement())[::-1]
    
    ngg_list = NGG_list_up_internal(positive_seq, '+') + NGG_list_up_internal(negative_seq, '-')
    
    result_df = pd.DataFrame(ngg_list, columns=['strand', 'sgRNA', 'pam', 'position'])
    result_df.to_csv(name + '_ngg_list.csv', index=False)
    
    return result_df
    
  