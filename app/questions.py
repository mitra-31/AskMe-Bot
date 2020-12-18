import csv

def link(query):
  try:
    from googlesearch import search 
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
     if "geeksforgeeks"  in j:
        return (j)
  except ImportError: 
	  print("No module named 'google' found") 






with open('app/q.csv',mode='r') as f:
    csvReader = csv.reader(f,delimiter="\n")
    lineCount = 0
    totalLines = 0
    lst = []
    for row in csvReader:
        lst.append(row)
        totalLines += 1