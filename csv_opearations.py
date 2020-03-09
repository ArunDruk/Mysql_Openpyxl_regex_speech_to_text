import csv

### reading the CSV file #####
# with open("SQL_data_values.csv",'r') as fr:
#     thereader=csv.reader(fr)
#     data=list(thereader)

###### Writing to the CSV file ########
## Below is the list of tupples
L=[('John', 'Highway 21'),
('Simran', 'caley'),
('Rock', 'California'),
('Kane', 'Africa'),
('StoneCold', 'New Zealand'),
('Jenillia', 'France'),
('Kathy', 'Sweden'),
('Joseph', 'Dubai')
]

with open ("CSV_write_values.csv",'w',newline="") as fw:
    thewriter=csv.writer(fw)
    thewriter.writerow(["name","address"])
    for i in range(len(L)):
        thewriter.writerow([L[i][0],L[i][1]])





