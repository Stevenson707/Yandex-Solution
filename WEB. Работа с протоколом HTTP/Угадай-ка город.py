import pygame
import requests
import sys
import os
import random


# Переключение слайдов реализовано на "S"


def show_map(ll_spn=None, map_type="map", add_params=None):
    if ll_spn:
        map_request = f"http://static-maps.yandex.ru/1.x/?{ll_spn}&l={map_type}"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}"

    if add_params:
        map_request += "&" + add_params
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    return response


def show_maps():
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    lst = ["map", "sat"]

    map_locations = {
        "Екатеринбург": "ll=60.603742,56.838207&spn=0.04,0.04",
        "Москва": "ll=37.618290,55.753434&spn=0.04,0.04",
        "Краснодар": "ll=38.976217,45.040723&spn=0.05,0.05"
    }

    loc = ["ll=60.603742,56.838207&spn=0.04,0.04",
           "ll=37.618290,55.753434&spn=0.04,0.04",
           "ll=38.976217,45.040723&spn=0.05,0.05"]

    while pygame.event.wait().type != pygame.QUIT:
        map_location = random.choice(loc)
        type_map = random.choice(lst)
        response = show_map(map_location, type_map)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        # Запишем полученное изображение в файл.
                        map_file = "map.png"
                        try:
                            with open(map_file, "wb") as file:
                                file.write(response.content)
                        except IOError as ex:
                            print("Ошибка записи временного файла:", ex)
                            sys.exit(2)

                        # Рисуем картинку, загружаемую из только что созданного файла.
                        screen.blit(pygame.image.load(map_file), (0, 0))

                        # Переключаем экран и ждем закрытия окна.
                        pygame.display.flip()

                        # Удаляем за собой файл с изображением.
                        os.remove(map_file)
                        running = False


def main():
    show_maps()


if __name__ == "__main__":
    main()
