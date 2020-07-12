import wolframalpha

def Wolframalpha(key):
    try:
        client = wolframalpha.Client('G45HAX-H76XQ2WVVA')
        res = client.query('solution of ' + key);resultlist = []
        
        resultlist.append(res['pod'][1]['subpod']['img']['@alt'])
        a = '/'.join(resultlist)
        return a
    
    except Exception as ex:
        return "Error! : " + str(ex)

