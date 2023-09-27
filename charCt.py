# Write your code here :-)
import pprint

message='It was a bright cold day in April, and the clocks were striking thirteen.'
count={}

        for c in message:
            count.setdefault(c,0)
            count[c]+=1

        print(pprint.pformat(count))
