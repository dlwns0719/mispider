import pandas as pd

def mismatch(target_DataFrame, source_DataFrame, target_name, source_name):

    result_list = []
    for target in target_DataFrame.values:
        
        target_strand = target[0]
        target_seq = target[1]
        target_pam = target[2]
        target_position = target[3]
        
        for source in source_DataFrame.values:
            
            source_strand = source[0]
            source_seq = source[1]
            source_pam = source[2]
            source_position = source[3]

            count = 0
            for k in range(20):
                if ord(target_seq[k]) ^ ord(source_seq[k]) != 0: 
                    count = count + 1

            if count == 1:
                result_list.append([target_name, target_strand, target_seq, target_pam, target_position])
                result_list.append([source_name, source_strand, source_seq, source_pam, source_position, "1 mismatch"])
                
            elif count == 2:
                result_list.append([target_name, target_strand, target_seq, target_pam, target_position])
                result_list.append([source_name, source_strand, source_seq, source_pam, source_position, "2 mismatch"])
                
    
    result_df = pd.DataFrame(result_list, columns=['', 'strand', 'sequence', 'pam', 'position', 'mismatch'])
    result_df.to_csv(target_name + "_" + source_name + "_mismatch_list.csv", index=False)
    