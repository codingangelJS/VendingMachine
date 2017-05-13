import VendingMachine

'''
자판기 프로그램 

1. 돈 입력 - 천원짜리, 오백원, 백원 만 입력 가능. 입력할때 한번에 돈 하나씩만 입력가능

2. 번호입력
2. 1~10 까지만 입력가능

3. 물건 나오기 
'''

vm = VendingMachine.Machine()


def first_step():
    while True:
        print('현재 가진 돈 : ', vm.cosMoney)
        money = int(input("돈 투입 : "))
        result = vm.check_money(int(money))
        if result is True:
            continue
        elif result is False:
            second_step()
            break


def second_step():
    while True:
        number = int(input("번호 : "))
        result = vm.check_product(number)
        if result == 1:
            continue
        elif result == 2:
            first_step()
            break
        elif result == 0:
            break

print('저는 자판기 입니다.\n이것은 메뉴판 입니다.\n')

while True:
    for idx, val in enumerate(vm.menu):
        print((idx + 1), '.', val[0], val[1], '원')

    print("\n급액을 입력해주세요.\n입력하시고 원하는 금액을 넣으셨으면 숫자 0을 입력해주세요")
    first_step()
    print('자판기에서 뽑은 물건 :', vm.cosProduct, ', 남은 돈 : ', vm.cosMoney)
    out = int(input("사용을 중지하고 싶으면 0 을 입력해주시고 계속 사용하고싶으면 0 이외의 숫자를 눌러주세요: "))

    if out == 0:
        break
