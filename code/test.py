def transponate(chord: str, distance: int) -> str:
    chord_list = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb','E', 'F', 'F#', 'G', 'G#' ]
    i = 0
    while chord_list[i] != chord:
        i += 1

    i = (i + distance) % 12
    return chord_list[i]

def main():
    print("транспонатор аккордов")
    print(transponate('B', -3))


if __name__ == '__main__':
    main()