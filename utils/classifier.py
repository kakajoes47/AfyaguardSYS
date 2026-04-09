def classify_attack(row):
    if "alert.signature" in row and isinstance(row["alert.signature"],str):
        s=row["alert.signature"].lower()

        if "scan" in s or "nmap" in s:
            return "SCAN"
        elif "dos" in s or "flood" in s:
            return "DoS"
        elif "bruteforce" in s:
            return "Brute Force"
        elif "malware" in s:
            return "Malware"
        else:
            return "Other"

    return "Normal"

def apply_classification(df):
    df["attack_type"]=df.apply(classify_attack,axis=1)
    return df
