class size:

    #身高

    """
    try:
        height= int(input("請輸入身高："))
    except:
        height= 0

    #體重
    try:
        weight= int(input("請輸入體重"))
    except:
        weight= 0
    """

    #身高
    height =0

    #體重
    weight =0

    #尺寸
    size_measure= ""

    def size(height,weight):

        if str(150)<=height<=str(160) or (str(150)<=height<=str(160) and str(48)<=weight<=str(52)):
            
            size_measure= "S"
            return size_measure
    
        elif str(161)<=height<= str(170) or (str(161)<=height<=str(170) and str(56)<=weight<= str(60)):
            
            size_measure= "M"
            return size_measure

        elif str(171)<=height<= str(175) or ( str(171)<=height<= str(175) and str(65)<=weight<= str(70)):
            
            size_measure= "L"
            return size_measure
        
        elif str(176)<=height<= str(180) or ( str(176)<=height<= str(180) and str(75)<=weight<= str(80)):
            
            size_measure= "XL"
            return size_measure 

        elif str(181)<=height<=str(185) or (str(181)<=height<= str(185) and str(85)<=weight<= str(90)):
            
            size_measure= "XXL"
            return size_measure   

        elif str(186)<=height<= str(190) or ( str(186)<=height<= str(190) and str(90)<=weight):
            
            size_measure= "3XL"
            return size_measure
        
        elif str(0)==height or str(0)==weight:
            size_measure= "請輸入正確身高體重"
            return size_measure
                          
        else:
            size_measure= "請輸入正確身高體重或聯絡客服"
            return size_measure
            
  
