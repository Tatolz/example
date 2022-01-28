def zasson(syotoku,songai,sisyutu,hoken):
    try:
        ans = 0
        #1-0.条件
        if(syotoku <= 480000):
            return ans
        #1-1.差し引き損失額
        sub_sum =   songai + sisyutu - hoken
        #1-2.計算
        calc_a = sub_sum - syotoku * 0.1
        calc_b = sisyutu - 50000
        if(calc_a > calc_b):
            ans = calc_a
        else:
            ans = calc_b
        #1-3.マイナスチェック
        if(ans>=0):
            return ans
        else:
            return 0
    #例外処理  
    except Exception as e:
        print(str(e))
        return 'error'
    
def hitorioya(syotoku,child):
    try:
        if syotoku <= 5000000 and child <= 480000:
            return 350000
        else:
            return 0
    except Exception as e:
        return 'error'

def kifukin(syotoku,kifukin):
    try:
        #1-1.所得控除の計算
        calc_a = kifukin
        #1-2.税額控除の計算
        calc_b = syotoku * 0.4
        #比較(有利を選択)
        if(calc_a > calc_b):
            ans = calc_b - 2000
        else:
            ans = calc_a - 2000
        return ans
    except Exception as e:
        return 'error'
    
def haigu_tokubetu(syotoku,haigu):
    try:
        if syotoku <= 9000000:
            if haigu > 480000 and 950000:
                ans = 380000
                return ans
            elif haigu > 950000 and haigu <= 1000000:
                ans = 360000
                return ans
            elif haigu > 1000000 and haigu <= 1050000:
                ans = 310000
                return ans
            elif haigu > 1050000 and haigu <= 1100000:
                ans = 260000
                return ans
            elif haigu > 1100000 and haigu <= 1150000:
                ans = 210000
                return ans
            elif haigu > 1150000 and haigu <= 1200000:
                ans = 160000
                return ans
            elif haigu > 1200000 and haigu <= 1250000:
                ans = 110000
                return ans
            elif haigu > 1250000 and haigu <= 1300000:
                ans = 60000
                return ans
            elif haigu > 1300000 and haigu <= 1330000:
                ans = 30000
                return ans
            else:
                return 0
        elif syotoku > 9000000 and syotoku <= 9500000:
            if haigu > 480000 and 950000:
                ans = 260000
                return ans
            elif haigu > 950000 and haigu <= 1000000:
                ans = 240000
                return ans
            elif haigu > 1000000 and haigu <= 1050000:
                ans = 210000
                return ans
            elif haigu > 1050000 and haigu <= 1100000:
                ans = 180000
                return ans
            elif haigu > 1100000 and haigu <= 1150000:
                ans = 140000
                return ans
            elif haigu > 1150000 and haigu <= 1200000:
                ans = 110000
                return ans
            elif haigu > 1200000 and haigu <= 1250000:
                ans = 80000
                return ans
            elif haigu > 1250000 and haigu <= 1300000:
                ans = 40000
                return ans
            elif haigu > 1300000 and haigu <= 1330000:
                ans = 20000
                return ans
            else: 
                return 0
        elif syotoku > 9500000 and syotoku <= 10000000:
            if haigu > 480000 and 950000:
                ans = 130000
                return ans
            elif haigu > 950000 and haigu <= 1000000:
                ans = 120000
                return ans
            elif haigu > 1000000 and haigu <= 1050000:
                ans = 110000
                return ans
            elif haigu > 1050000 and haigu <= 1100000:
                ans = 90000
                return ans
            elif haigu > 1100000 and haigu <= 1150000:
                ans = 70000
                return ans
            elif haigu > 1150000 and haigu <= 1200000:
                ans = 60000
                return ans
            elif haigu > 1200000 and haigu <= 1250000:
                ans = 40000
                return ans
            elif haigu > 1250000 and haigu <= 1300000:
                ans = 20000
                return ans
            elif haigu > 1300000 and haigu <= 1330000:
                ans = 10000
                return ans
            else:
                return 0
        else:
            return 0
    except Exception as e:
        return 'error'