from .registry import discover_algorithms


def show_algorithms(modules):
    for index, module in enumerate(modules, 1):
        print(f"{index}. {module.NAME}")

    print(f"{len(modules) + 1}. Back")


def run_algorithm(module):
    print(f"\n--- {module.NAME} ---")

    operations = module.OPERATIONS

    for index, operation in enumerate(operations, 1):
        print(f"{index}. {operation.title()}")

    choice = input("Choose operation: ")

    try:
        operation = operations[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    text = input("Enter input: ")

    if operation == "encode":
        print("Output:", module.encode(text))

    elif operation == "decode":
        print("Output:", module.decode(text))

    elif operation == "encrypt":
        key = input("Enter key: ")
        print("Output:", module.encrypt(text, key))

    elif operation == "decrypt":
        key = input("Enter key: ")
        print("Output:", module.decrypt(text, key))

    elif operation == "hash":
        print("Output:", module.hash(text))


def start():
    algorithms = discover_algorithms()

    while True:
        print("\n" + "=" * 45)
        print("           CRYPTOGRAPHY TOOLKIT")
        print("=" * 45)

        categories = list(algorithms.keys())

        for index, category in enumerate(categories, 1):
            print(f"{index}. {category}")

        print(f"{len(categories) + 1}. Exit")

        choice = input("\nChoose category: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == len(categories) + 1:
            print("Goodbye!")
            break

        if not 1 <= choice <= len(categories):
            print("Invalid choice.")
            continue

        category = categories[choice - 1]
        modules = algorithms[category]

        while True:
            print(f"\n--- {category} ---")

            show_algorithms(modules)

            algorithm_choice = input("Choose algorithm: ")

            try:
                algorithm_choice = int(algorithm_choice)
            except ValueError:
                print("Invalid choice.")
                continue

            if algorithm_choice == len(modules) + 1:
                break

            if not 1 <= algorithm_choice <= len(modules):
                print("Invalid choice.")
                continue

            run_algorithm(modules[algorithm_choice - 1])
