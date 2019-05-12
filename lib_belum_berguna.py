#---------------------- Add Function To Queue probably/ masih belum berguna
#menambahkan fungsi ke queue
def addToQueue(function=None,args=[]):
    dict = {}
    dict['function']=function
    for i in range(len(args)):
        dict[i]=args[i]
    orderQueue(dict)
#run fungsi dari queue
def run(order):
    if 'function' in str(order[0]):
        function = order[0]
        args = order[0]
        function(*args)
    else :
        return order