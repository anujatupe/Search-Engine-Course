#creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hastable=[]
    for i in range (0,nbuckets):
        hastable.append([])
    return hastable

print make_hastable(2)

print make_hashtable(5)
