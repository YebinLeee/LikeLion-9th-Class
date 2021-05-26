class car:
    # 생성자
    # 객체의 특정 필드들을 생성&초기화
    def __init__(self, name, color, license):
        
        # ----- 필드 ----- (클래스 안에 정의된 변수)
        self.name=name
        self.color=color
        self.license=license

    # ----- 메서드 ----- (클래스 안에 정의된 함수)
    def drive(self):
        print(self.name,"앞으로 전진!")
    def getCar(self):
        print(self.color, self.license)

car1=car("테슬라", "빨강", "8756") # car 클래스의 car1 객체 생성
car2=car("모닝", "노랑", "1234")
car3=car("벤츠", "검정", "0000")

car1.drive()
car1.getCar()

car2.drive()
car2.getCar()

car3.drive()
car3.getCar()