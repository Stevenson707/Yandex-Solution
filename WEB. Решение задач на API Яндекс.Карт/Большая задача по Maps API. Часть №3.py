import pygame
import requests
import sys
import os


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
    spn1 = 1
    spn2 = 1
    ll1 = 60.603742
    ll2 = 56.838207
    while pygame.event.wait().type != pygame.QUIT:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_PAGEUP:
                        try:
                            spn1 -= 0.1
                            spn2 -= 0.1
                            map_location = f"ll={str(ll1)},{str(ll2)}&spn={str(spn1)},{str(spn2)}"
                            type_map = "map"
                            response = show_map(map_location, type_map)
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
                        except:
                            pass

                    elif event.key == pygame.K_PAGEDOWN:
                        try:
                            spn1 += 0.1
                            spn2 += 0.1
                            map_location = f"ll={str(ll1)},{str(ll2)}&spn={str(spn1)},{str(spn2)}"
                            type_map = "map"
                            response = show_map(map_location, type_map)
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
                        except:
                            pass

                    elif event.key == pygame.K_UP:
                        try:
                            ll2 += 0.1
                            map_location = f"ll={str(ll1)},{str(ll2)}&spn={str(spn1)},{str(spn2)}"
                            type_map = "map"
                            response = show_map(map_location, type_map)
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
                        except:
                            pass

                    elif event.key == pygame.K_DOWN:
                        try:
                            ll2 -= 0.1
                            map_location = f"ll={str(ll1)},{str(ll2)}&spn={str(spn1)},{str(spn2)}"
                            type_map = "map"
                            response = show_map(map_location, type_map)
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
                        except:
                            pass

                    elif event.key == pygame.K_LEFT:
                        try:
                            ll1 -= 0.1
                            map_location = f"ll={str(ll1)},{str(ll2)}&spn={str(spn1)},{str(spn2)}"
                            type_map = "map"
                            response = show_map(map_location, type_map)
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
                        except:
                            pass

                    elif event.key == pygame.K_RIGHT:
                        try:
                            ll1 += 0.1
                            map_location = f"ll={str(ll1)},{str(ll2)}&spn={str(spn1)},{str(spn2)}"
                            type_map = "map"
                            response = show_map(map_location, type_map)
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
                        except:
                            pass


def main():
    show_maps()


if __name__ == "__main__":
    main()
