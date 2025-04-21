def build_pyramid(height):
    for i in range(1, height + 1):
        print(''.join(str(x) for x in range(1, i + 1)))

# Пример использования:
height = 5
build_pyramid(height)
