from Samples.mapapi_PG import show_map


def show_maps():
    spn = input("Введите масштаб без пробелов в формате spn: ")
    ll_spn = f"ll=135.746181,-27.483765&spn={spn}"
    show_map(ll_spn)


def main():
    show_maps()


if __name__ == "__main__":
    main()