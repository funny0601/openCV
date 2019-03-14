while 1 : # 무한 루프
    money = int(input('돈을 넣어주세요 ')) # 입력된 값을 정수로 변환
    number = int(input('음료를 넣어주세요 ')) # 선택한 음료의 번호를 정수로 변환

    temp = money

    if number == 1 :  # 음료(number)가 1인 경우
        print('포도주스. 거스름돈은 ', money-100)
        money = temp - 100
        if money <= 0 :
            break  # 반복문을 벗어남
    elif number == 2 :
        print('오렌지주스. 거스름돈은 ', money-200)
        money = temp - 200
        if money <= 0 :
            break
    elif number == 3 :
        print('환타. 거스름돈은 ', money-300)
        money = temp - 300
        if money <= 0 :
            break
    else :          # 음료(number)가 1,2,3이 모두 아닌 경우
        print('없는 번호')

