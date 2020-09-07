import settings
import tools
def addOffice(obj):
    for F in settings.OFFICES:
        if obj['office'] == F['id']:
            obj['office'] = F

def addDepartment(obj,tile):
    for o in obj:        
        for D in settings.DEPARTAMETS:                        
            if o['department'] == D['id']:
                o['department'] = D                
                if len(tile) > 0:
                    expand(tile,o['department'],None) #(recursive)


def addSuperDepartment(obj,tile):    
    for D in settings.DEPARTAMETS:    
        if obj['superdepartment'] == D['id']:
            obj['superdepartment'] = D
            if len(tile) > 0:
                    expand(tile,obj['superdepartment'],None) #(recursive)


def addManager(obj,tile,actualKey,pdData):
    for o in obj:
        manager = o.get('manager')
        findedItem = pdData.query(f'id == {manager}')
        if not findedItem.empty:
            findedItem = findedItem.to_dict()
            o['manager']  = tools.formatedItem(findedItem)
             
            if len(tile) > 0: 
                expand(tile,[o['manager']],pdData) # (recursive)
        
# While there exists pending expansions it will be called recursively
def expand(keys,obj,template):
    actualKey = keys[0]
    tile = keys[1:]

    if (actualKey == "manager"):
        addManager(obj,tile,actualKey,template)
    
    elif(actualKey == "department"):
        addDepartment(obj,tile)

    elif (actualKey == "superdepartment"):
        addSuperDepartment(obj,tile)
    
    elif (actualKey == "office"):
        addOffice(obj[0])

# Launch all the given expanders 
def startExpanders(expanders,response,pdData):
    for exp in expanders:
        expand(exp.split("."),response,pdData)

