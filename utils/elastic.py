from elasticsearch import Elasticsearch
import pandas as pd

def connect_elasticsearch():
    return Elasticsearch("http://localhost:9200")

def fetch_logs(es, size=300):
    indices=["logs","suricata-*","filebeat-*","zeek-*"]

    res=es.search(index=",".join(indices),
                  body={"query":{"match_all":{}}},
                  size=size)

    data=[hit["_source"] for hit in res["hits"]["hits"]]
    df=pd.DataFrame(data) if data else pd.DataFrame()

    return normalize(df)

def normalize(df):
    if "id.orig_h" in df.columns:
        df["src_ip"]=df["id.orig_h"]
    if "id.resp_h" in df.columns:
        df["dest_ip"]=df["id.resp_h"]
    if "@timestamp" in df.columns:
        df["timestamp"]=df["@timestamp"]
    return df
