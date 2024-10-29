import PySimpleGUI as psg
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234567',
    port='3306',
    database='tour'
)

mycursor = mydb.cursor()


class InfSystem:
    def __init__(self):
        self.mydb = mydb
        self.mycursor = mycursor

    def add_cities(self, city_id, city_name):
        self.mycursor.execute(
            "INSERT INTO city (id, name) VALUES (%s, %s)",
            (city_id, city_name))
        self.mydb.commit()

    def delete_cities(self, city_id):
        self.mycursor.execute("DELETE FROM city WHERE id=%s", (city_id,))
        self.mydb.commit()

    def view_cities(self):
        self.mycursor.execute("SELECT * FROM city")
        cities = self.mycursor.fetchall()
        return cities

    def add_trips(self, trips_id, Start_date, End_date):
        self.mycursor.execute(
            "INSERT INTO trips (trips_id, date_start, date_end) VALUES (%s, %s, %s)",
            (trips_id, Start_date, End_date)
        )
        self.mydb.commit()

    def delete_trips(self, trips_id):
        self.mycursor.execute("DELETE FROM trips WHERE trips_id=%s", (trips_id,))
        self.mydb.commit()

    def view_trips(self):
        self.mycursor.execute("SELECT * FROM trips")
        trips = self.mycursor.fetchall()
        return trips

    def add_hotel(self, hotel_id, name, address, rate, price, city_id):
        self.mycursor.execute(
            "INSERT INTO hotels (hotels_id, hotels_name, hotels_address, hotels_rate, hotels_price, id_city) VALUES (%s, %s, %s, %s, %s, %s)",
            (hotel_id, name, address, rate, price, city_id)
        )
        self.mydb.commit()

    def delete_hotel(self, hotel_id):
        self.mycursor.execute("DELETE FROM hotels WHERE hotels_id=%s", (hotel_id,))
        self.mydb.commit()

    def view_hotels(self):
        self.mycursor.execute("SELECT * FROM hotels")
        hotels = self.mycursor.fetchall()
        return hotels

    def add_entertainment(self, entertain_id, theatre_name, time, show_name, rate, price, trips_id):
        self.mycursor.execute(
            "INSERT INTO entertainment (entertain_id, theatre_name, time, show_name, show_rate, price, trips_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (entertain_id, theatre_name, time, show_name, rate, price, trips_id)
        )
        self.mydb.commit()

    def delete_entertainment(self, entertain_id):
        self.mycursor.execute("DELETE FROM entertainment WHERE entertain_id=%s", (entertain_id,))
        self.mydb.commit()

    def view_entertainment(self):
        self.mycursor.execute("SELECT * FROM entertainment")
        entertainment = self.mycursor.fetchall()
        return entertainment

    def view_table(self, table_name, table_data):
        output = ""
        for row in table_data:
            output += str(row) + "\n"
        psg.popup(table_name, output)


def login():
    layout = [
        [psg.Text("Авторизация")],
        [psg.Text("Логин"), psg.Input(key="login")],
        [psg.Text("Пароль"), psg.Input(key="password", password_char="*")],
        [psg.Button("Войти")]
    ]

    window = psg.Window("Авторизация", layout)

    while True:
        event, values = window.read()

        if event == psg.WINDOW_CLOSED:
            break
        elif event == "Войти":
            login_input = values["login"]
            password_input = values["password"]

            if login_input == "meow" and password_input == "11111":
                window.close()
                main()
            else:
                psg.popup("Неправильный логин или пароль")

    window.close()


def main():
    system = InfSystem()

    layout = [
        [psg.Text("Меню")],
        [psg.Button("Города"), psg.Button("Поездки")],
        [psg.Button("Отели"), psg.Button("Развлечения")],
        [psg.Button("Выход")]
    ]

    window = psg.Window("Меню", layout)

    while True:
        event, values = window.read()

        if event == psg.WINDOW_CLOSED or event == "Выход":
            break
        elif event == "Города":
            cities_menu(system)
        elif event == "Поездки":
            trips_menu(system)
        elif event == "Отели":
            hotels_menu(system)
        elif event == "Развлечения":
            entertainment_menu(system)

    window.close()


def cities_menu(system):
    layout = [
        [psg.Text("Меню городов")],
        [psg.Button("Добавить город"), psg.Button("Удалить город")],
        [psg.Button("Просмотреть города"), psg.Button("Назад")]
    ]

    window = psg.Window("Меню городов", layout)

    while True:
        event, values = window.read()

        if event == psg.WINDOW_CLOSED or event == "Назад":
            break
        elif event == "Добавить город":
            city_id = psg.popup_get_text("Введите ID города")
            city_name = psg.popup_get_text("Введите название города")
            system.add_cities(city_id, city_name)
        elif event == "Удалить город":
            city_id = psg.popup_get_text("Введите ID города для удаления")
            system.delete_cities(city_id)
        elif event == "Просмотреть города":
            cities = system.view_cities()
            system.view_table("Города", cities)

    window.close()


def trips_menu(system):
    layout = [
        [psg.Text("Меню поездок")],
        [psg.Button("Добавить поездку"), psg.Button("Удалить поездку")],
        [psg.Button("Просмотреть поездки"), psg.Button("Назад")]
    ]

    window = psg.Window("Меню поездок", layout)

    while True:
        event, values = window.read()

        if event == psg.WINDOW_CLOSED or event == "Назад":
            break
        elif event == "Добавить поездку":
            trips_id = psg.popup_get_text("Введите ID поездки")
            start_date = psg.popup_get_text("Введите дату начала")
            end_date = psg.popup_get_text("Введите дату окончания")
            system.add_trips(trips_id, start_date, end_date)
        elif event == "Удалить поездку":
            trips_id = psg.popup_get_text("Введите ID поездки для удаления")
            system.delete_trips(trips_id)
        elif event == "Просмотреть поездки":
            trips = system.view_trips()
            system.view_table("Поездки", trips)

    window.close()


def hotels_menu(system):
    layout = [
        [psg.Text("Меню отелей")],
        [psg.Button("Добавить отель"), psg.Button("Удалить отель")],
        [psg.Button("Просмотреть отели"), psg.Button("Назад")]
    ]

    window = psg.Window("Меню отелей", layout)

    while True:
        event, values = window.read()

        if event == psg.WINDOW_CLOSED or event == "Назад":
            break
        elif event == "Добавить отель":
            hotel_id = psg.popup_get_text("Введите ID отеля")
            name = psg.popup_get_text("Введите название отеля")
            address = psg.popup_get_text("Введите адрес отеля")
            rate = psg.popup_get_text("Введите рейтинг отеля")
            price = psg.popup_get_text("Введите цену")
            city_id = psg.popup_get_text("Введите ID города")
            system.add_hotel(hotel_id, name, address, rate, price, city_id)
        elif event == "Удалить отель":
            hotel_id = psg.popup_get_text("Введите ID отеля для удаления")
            system.delete_hotel(hotel_id)
        elif event == "Просмотреть отели":
            hotels = system.view_hotels()
            system.view_table("Отели", hotels)

    window.close()


def entertainment_menu(system):
    layout = [
        [psg.Text("Меню развлечений")],
        [psg.Button("Добавить театр"), psg.Button("Удалить театр")],
        [psg.Button("Просмотреть театры"), psg.Button("Назад")]
    ]

    window = psg.Window("Меню развлечений", layout)

    while True:
        event, values = window.read()

        if event == psg.WINDOW_CLOSED or event == "Назад":
            break
        elif event == "Добавить театр":
            entertain_id = psg.popup_get_text("Введите ID театра")
            theatre_name = psg.popup_get_text("Введите название театра")
            time = psg.popup_get_text("Введите время проведения шоу")
            show_name = psg.popup_get_text("Введите название шоу")
            rate = psg.popup_get_text("Введите рейтинг шоу")
            price = psg.popup_get_text("Введите цену")
            trips_id = psg.popup_get_text("Введите ID поездки")
            system.add_entertainment(entertain_id, theatre_name, time, show_name, rate, price, trips_id)
        elif event == "Удалить театр":
            entertain_id = psg.popup_get_text("Введите ID театра для удаления")
            system.delete_entertainment(entertain_id)
        elif event == "Просмотреть театры":
            entertainment = system.view_entertainment()
            system.view_table("Театры", entertainment)

    window.close()


if __name__ == "__main__":
    login()
