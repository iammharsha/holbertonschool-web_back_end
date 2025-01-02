#!/usr/bin/env python3
"""Module to get nginx logs stat"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs_collection = client.logs.nginx
    log_count = nginx_logs_collection.count_documents({})

    method_counts = {
        method: nginx_logs_collection.count_documents({
            "method": method
        }) for method in methods
    }

    status_logs = nginx_logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{log_count} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_logs} status check")
        