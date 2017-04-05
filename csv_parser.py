import csv
from re import search
from collections import Counter

with open('MOCK_DATA.csv') as csv_handler:
    reader = csv.DictReader(csv_handler)
    csv_dict = {}
    domain_count = {}
    for row in reader:
        domain = search('@(\w+)', row['email']).group(1)
        if csv_dict.get(domain):
            csv_dict[domain].append([row['id'], row['first_name'], row['last_name'],
                                     row['email'], row['gender'], row['ip_address']])
            domain_count[domain] += 1
        else:
            csv_dict[domain] = [[row['id'], row['first_name'], row['last_name'],
                                 row['email'], row['gender'], row['ip_address']], ]
            domain_count[domain] = 1

[print(domain, count, sep=': ') for domain, count in domain_count.items()]

counter = Counter(domain_count)
for domain, count in counter.most_common(3):
    with open('{}.csv'.format(domain), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\r')
writer.writerows(csv_dict[domain])
