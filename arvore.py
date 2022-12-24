def draw_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

def main():
    height = int(input("Insira a altura da árvore de Natal: "))
    draw_tree(height)

main()
