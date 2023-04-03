from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)

    
def get_frequent_visit_from_ip(ips):
    a = Counter(ips).most_common(1)
    return a[0]