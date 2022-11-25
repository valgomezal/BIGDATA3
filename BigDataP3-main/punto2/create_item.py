def create_item(labels,route):
    item = {}
    item["indice"]=labels[0]["Name"]
    item ["info"]=[labels[i]["Name"] for i in range(1,len(labels))]
    item["route"]=route
    return item