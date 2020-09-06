def formatedItem(item):
    ret = {}
    for i in item:   
        key = None

        for values in item[i]:
            key = values
            break
        
        value = item[i].get(key)
        if i == "department" or i == "office" or i == "manager":
            try:
                value = int(value)
            except Exception:
                value = None
        
        ret[i] = value
    return ret


def formatLS(ls):
    cp = []
    for l in ls:
        try:
            cp.append(int(l))
        except Exception:
            pass
    return cp