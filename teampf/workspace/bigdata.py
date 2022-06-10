from faker import Faker
import sys

fake=Faker("ko_KR")

sys.stdout=open("삼청각.txt","w")

print("식당 / 연령 / 성별")
for i in range(150):
    print("삼청각", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))
sys.stdout.close()



# sys.stdout=open("지화자.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("지화자", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("수담.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("수담", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("인량훠궈.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("인량훠궈", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("암소서울.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("암소서울", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("울프강 스테이크 하우스.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("울프강 스테이크 하우스", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("백리향.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("백리향", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("아카사카.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("아카사카", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("버드나무집.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("버드나무집", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("도우룸.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("도우룸", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("보름쇠.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("보름쇠", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("곰바위.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("곰바위", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("가온.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("가온", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("볼트 스테이크 하우스.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("볼트 스테이크 하우스", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("정식당.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("정식당", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("텅앤그루브.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("텅앤그루브", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("모수서울.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("모수서울", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)

# sys.stdout=open("크리스탈 제이드.txt","w")

# print("식당 / 연령 / 성별")

# for i in range(150):
#     print("크리스탈 제이드", "/", fake.random_int(min=20, max=59), "/", fake.random_element(elements=("남자","여자")))

# sys.stdout.close()

# print("-"*25)