def createQueue():
    q = []
    return q
def enqueue(q, data):
    q.insert(0,data)
    return q
def dequeue(q):
    return q.pop()
def size(q):
    return len(q)
def isEmpty(q):
    return q == []

