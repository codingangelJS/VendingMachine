class Machine:
    cosNumber = 1
    cosMoney = 0
    cosProduct = ''

    menu = [('초코에몽', 1000), ('쿠크다스', 1500), ('이건뭘까요', 3000), ('사과', 1000), ('랜덤', 2300)]

    def check_money(self, money):
        if money == 1000 or money == 500 or money == 100:
            self.cosMoney += money
            return True
        elif money == 0:
            return False
        else:
            print("천원, 오백원, 백원 단위의 금액만 입력해주세요\n")
            return True

    def check_product(self, number):
        number = number - 1
        self.cosNumber = number
        if number >= 0 & number < len(self.menu):
            if self.menu[number][1] <= self.cosMoney:
                self.cosMoney -= self.menu[number][1]
                self.cosProduct = self.menu[number][0]
                return 0
            elif self.menu[number][1] > self.cosMoney:
                return 2
        else:
            print("자판기에 있는 숫자만 누르세요\n")
            return 1
