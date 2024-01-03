import re
import json

def Re(text):
    rplydata = text

    #將rplydata = replace "" 

    pattern = r"rplydata = "

    rplydata = re.sub(pattern, "", rplydata)

    #將 } replace }]

    rplydata = re.sub(r'}', '}]', rplydata)

    #將第一個出現 ] 後全部移除

    index_to_remove = rplydata.find(']')
    
    rplydata = rplydata[:index_to_remove +1]

    #將rplydata 變成 json

    rplydata = json.loads(rplydata)
    print(type(rplydata))

    gender = rplydata[0].get("gender")
    style = rplydata[0].get("style")
    color = rplydata[0].get("color")

    text = f"這是件{gender},風格是{style},顏色是{color}"

    return gender, style, color, text


