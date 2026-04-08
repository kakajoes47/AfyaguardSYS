from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def fetch_logs(index="filebeat-*", size=50):
    query = {
        "size": size,
        "query": {
            "match_all": {}
        }
    }

    response = es.search(index=index, body=query)

    logs = []
    for hit in response["hits"]["hits"]:
        logs.append(hit["_source"])

    return logs
