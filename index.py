#자판기 만들기
#관리자 모드 -> 
#판매 모드 -> 돈 투입 - 돈 액수 확인 - 출력 가능한 물건 선별, 제시 - 물건 선택 - 물건 출력
#물건 -> 가격, 재고, 구입시 금액 지불과 재고 하나 소진,
class production:
    def __init__(self, price, amount):
        self.price = price
        self.amount = amount
        
    def getPrice(self):
        return self.price
    
    def getAmout(self):
        return self.amount

    #클래스에서는 객체 변수의 변화에만 집중. 전역 변수나 다른 과정은 구현 과정에서 따로 제작
    #다른 변수나 시스템과의 관계는 메모해서 구현에 이용.
    def purchase(self, num):
        if(money >= self.price * num):
            money -= self.price * num
            self.amount -= num


income = 0
money = 0
frontmenu = {}
menu = {}

def menucorrection(name, price, amount):
    menu[name] = production(price, amount)
    frontmenu[name] = [menu[name].getPrice(), menu[name].getAmout()]

while(True):
    #편집 모드
    while(True):
        print("관리자 모드.\n")
        choice = int(input("원하시는 메뉴를 선택해 주세요. 1. 잔액 회수, 2. 메뉴 편집, 3. 판매 모드\n"))
        
        if(choice == 1):
            income += money
            money = 0
            print("잔액이 회수되었습니다.")
        
        elif(choice == 2):
            print("현재 메뉴 : {}\n".format(frontmenu))
            print("1. 상품 추가, 2. 상품 삭제, 3. 상품 정보 변경")
            choice = int(input())
            
            if(choice == 1):
                print("추가하고 싶은 상품의 이름, 가격, 수량을 차례대로 입력해주세요.")
                name = input()
                price = int(input())
                amount = int(input())
                menucorrection(name, price, amount)
                print("상품이 추가되었습니다.\n")
                print("현재 메뉴 : {}".format(frontmenu))
                del name
                del price
                del amount
                
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
            break
            

#판매 모드
    while(True):
        Input = input(int("구입을 원하시면 아래의 구멍에 돈을 넣어주세요.\n"))