# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]
def show_movies(movie_list):
    for movie in movies:
        print(f"{movie["movie_name"]}")

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง'
def check_age(user_age, age_restriction):
    age = int(input("What is your age? "))
    if movies['age_restriction'] == 'G':
        pass
    else:
        if age >= movies['age_restriction']:
            pass
        else:
            print("You are too young to buy watch this movie.")
            return
    
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    if movies['genre'] == 'Horror':
        base_price += 50
    else:
        base_price += 0
    # TODO: ถ้า genre เป็น 'Horror' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    show_movies()
    ask = input("Select movie: ")
    if ask == 1:
        check_age()
        st = input("Select dub\n1. Thai dub\n2. Soundtrack\nsound: ")
        if st == 1:
            print(f"Ticket result: Avengers Endgame Thai dub 300")
        elif st == 2:
            print(f"Ticket result: Avengers Endgame Soundtrack 300")
    elif ask == 2:
        check_age()
        st = input("Select dub\n1. Thai dub\n2. Soundtrack\nsound: ")
        if st == 1:
            print(f"Ticket result: Inception Thai dub 280")
        elif st == 2:
            print(f"Ticket result: Inception Soundtrack 280")
    elif ask == 3:
        check_age()
        st = input("Select dub\n1. Thai dub\n2. Soundtrack\nsound: ")
        if st == 1:
            print(f"Ticket result: It Thai dub 180")
        elif st == 2:
            print(f"Ticket result: It Soundtrack 180")
    elif ask == 4:
        check_age()
        st = input("Select dub\n1. Thai dub\n2. Soundtrack\nsound: ")
        if st == 1:
            print(f"Ticket result: The Notebook Thai dub 250")
        elif st == 2:
            print(f"Ticket result: The Notebook Soundtrack 250")
    elif ask == 5:
        check_age()
        st = input("Select dub\n1. Thai dub\n2. Soundtrack\nsound: ")
        if st == 1:
            print(f"Ticket result: Harry Potter and the Sorcerer\'s Stone Thai dub 260")
        elif st == 2:
            print(f"Ticket result: Harry Potter and the Sorcerer\'s Stone Soundtrack 260")
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    # 3. รับอายุผู้ใช้
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    show_movies()
    buy_ticket()

    
    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = input("Select menu: ")
    for i in menu:
        if menu == 1:
            show_movies()
            
        elif menu == 2:
            show_movies()
            buy_ticket()


    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# เรียก main เพื่อเริ่มโปรแกรม
main()

#not done