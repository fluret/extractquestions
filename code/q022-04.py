from pprint import pprint

p = input().split()
pprint({i: p.count(i) for i in p})
