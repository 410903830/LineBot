class size:

    #身高
    try:
        height= int(input("請輸入身高："))
    except:
        height= 0

    #體重
    try:
        weight= int(input("請輸入體重"))
    except:
        weight= 0

    #尺寸
    size_measure= ""

    def size(height,weight):

        if 150<=height<=160 or (150<=height<=160 and 48<=weight<=52):
            
            size_measure= "S"
            return size_measure
    
        elif 161<=height<=170 or (161<=height<=170 and 56<=weight<=60):
            
            size_measure= "M"
            return size_measure

        elif 171<=height<=175 or (171<=height<=175 and 65<=weight<=70):
            
            size_measure= "L"
            return size_measure
        
        elif 176<=height<=180 or (176<=height<=180 and 75<=weight<=80):
            
            size_measure= "XL"
            return size_measure 

        elif 181<=height<=185 or (181<=height<=185 and 85<=weight<=90):
            
            size_measure= "XXL"
            return size_measure   

        elif 186<=height<=190 or (186<=height<=190 and 90<=weight):
            
            size_measure= "3XL"
            return size_measure
        
        elif height==0 or weight==0:
            size_measure= "請輸入正確身高體重"
            return size_measure
                          
        else:
            size_measure= "4XL 特體"
            return size_measure

            
    print(size(height, weight))
