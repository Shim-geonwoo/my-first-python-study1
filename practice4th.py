######클래스
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank1 = Unit("시저탱크", 150, 35)        

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#외부에서도 쓸 수 있음

#마인드 컨트롤
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 외부에서 클로킹이라는 변수를 추가 할당 후 True값 넣음
# 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있음(확장)
# 차이점: 레이스 1에는 변수 3개, 레이스 2에만 추가했음


######메소드


# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name #여기서 name은 위에서 전달받은 name을 씀
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
# # self는 자기자신 의미. 클래스에서 self 무조건 써줌
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


######상속


# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
# Unit에서 정의한 것 상속하여 사용
# AttackUnit에서 damage만 따로 정의가능

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


######다중상속


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


######매소드 오버라이딩


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#               .format(self.name, location, self.speed))
            
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
    

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")


######Pass and Super
# Unit을 통해서 초기화 할때는 self
# Super를 통해서 초기화는 self 노필요

# class BulidingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location


# supply_depot = BulidingUnit("서플라이 디폿", 500, "7시")


# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         # super().__init__()
#         # super는 맨처음에 상속받는 클래스가 호출
#         Unit.__init__(self)
#         Flyable.__init__(self)

#드랍쉽
# dropship = FlyableUnit()


######스타 전반전


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(self.name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
#               .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다."\
#               .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed,damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#         .format(self.name, location, self.damage))

# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족해 스팀팩 사용이 불가능합니다.".format(self.name))

#탱크
# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150 ,1 ,35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다".format(self.name))  
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# class Wratih(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__("레이스, 80, 20, 5")
#         self.clocked = False
    
#     def cloking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 생성합니다.")        

# def game_over():
#     print("Player : GG")
#     print("[Player]가 퇴장했습니다.")


# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wratih()

# Units = []
# Units.append(m1)
# Units.append(m2)
# Units.append(m3)
# Units.append(t1)
# Units.append(t2)
# Units.append(w1)

# #전군이동
# for unit in Units:
#     unit.move("1시")

# #탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# #공격모드 준비(탱크 시즈, 레이스 클로킹, 마린 스팀팩)
# for unit in Units:
#     if isinstance(unit, Marine):
#     #지금 만들어진 객체가 어떤 클래스의 인스턴스인지
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wratih):
#         unit.cloking()

# #전군공격
# for unit in Units:
#     unit.attack("1시")
    