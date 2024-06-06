#자판기 만들기

#자판기 생성시 필요한 물건들 모두 객체화(상품, 돈, 메뉴 등) -> 그 대상의 연산이 쉬워짐.
class production: #자판기에 진열되는 상품
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getAmout(self):
        return self.amounts #객체 변수에 대한 get 함수 필수!

    def purchase(self, num): # 돈 객체가 생김에 따라 변경 필요!
        if(money >= self.price * num):
            money -= self.price * num
            self.amount -= num

class money: #투입, 반환, 저장되는 돈
    def __init__(self):
        self.total = 0

    def getTotal(self):
        return self.total

    def Input(self, amount):
        self.total += amount

    def Output(self, amount):
        self.total -= amount

class menu: #상품을 모아놓고 보여주는 메뉴(상품의 리스트)
    def __init__(self):
        self.list = []
        
    def getList(self):
        return self.list
    
    def getName(self, i): #리스트 속 상품의 변수 얻기 쉽도록 오버로딩
        self.list[i].getName()
        
    def getPrice(self, i):
        self.list[i].getPrice()
        
    def getAmount(self, i):
        self.list[i].getAmount()
    
    def add(self, production): #메뉴에 상품 추가, 삭제
        self.list.append(production)

    def remove(self, production):
        self.list.remove(production)
        
    def showList(self): #객체인 상품 속 변수들을 get함수로 출력
        for i in range(len(self.list)):
            print("{} : 가격 : {}원, 재고, {}개\n".format(self.getName(i), self.getPrice(i), self.getAmount(i)))

income = money()
payment = money()
frontmenu = {}
menu = menu()

def menucorrection(name, price, amount):
    menu[name] = production(price, amount)
    frontmenu[name] = [menu[name].getPrice(), menu[name].getAmout()]

while(True):
    mod = True # mod가 True면 관리자 모드, False면 판매 모드
    #편집 모드
    while(mod):
        print("관리자 모드.\n")
        choice = int(input("원하시는 메뉴를 선택해 주세요. 1. 수입 회수, 2. 메뉴 편집, 3. 판매 모드\n"))
        
        if(choice == 1):
            income.Input(money.getTotal())
            payment.Output(money.getTotal())
            print("잔액이 회수되었습니다.")
        
        elif(choice == 2):
            print("현재 메뉴 : {}\n".format(frontmenu))
            print("1. 상품 추가, 2. 상품 삭제, 3. 상품 정보 변경")
            choice = int(input())
            
            if(choice == 1):
                prod1 = input("추가하고 싶은 상품의 이름, 가격, 수량을 차례대로 입력해주세요.")
                menu.add(prod1) #깊은 복사 얕은 복사 고민 필요!
                print("상품이 추가되었습니다.\n")
                menu.showList()
                
            elif(choice == 2):
                name = input("삭제하고 싶은 상품의 이름을 입력해주세요.")
                if(name in menu):
                    del menu[name]
                    del frontmenu[name]
                del name
                print("상품이 삭제되었습니다.\n")
                print("현재 메뉴 : {}".format(frontmenu))
                
            elif(choice == 3):
                name = input("변경하고 싶은 상품의 이름을 입력해주세요.")
                if(name in menu):
                    print("변경한 가격과 수량을 차례대로 입력해주세요.")
                    price = int(input())
                    amount = int(input())
                    menucorrection(name, price, amount)
                    del price
                    del amount
                del name
                print("상품 정보가 변경되었습니다.")
                print("현재 메뉴 : {}".format(frontmenu))
                
        elif(choice == 3):
            mod = False
            

#판매 모드
    while(not mod):
        Input = input(int("구입을 원하시면 아래의 구멍에 돈을 넣어주세요.\n"))
        