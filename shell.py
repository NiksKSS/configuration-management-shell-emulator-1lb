## first step
import os

def expand_variables(command):#замена команды на итоговый путь ($HOME(key) → заменяет на /Users/veronika(value))
    for key, value in os.environ.items(): #проход по всем переменным окружения
        command = command.replace(f"${key}", value)
        command = command.replace(f"${{{key}}}", value)
    return command

def parse_command(line):#разбитие строки на команды и аргументы
    if not line.strip(): #если только пробелы или строка пустая
        return None, []
    expanded = expand_variables(line.strip())#Убираем пробелы по краям и заменяем $HOME, ${USER} и т.п.
    parts = expanded.split() #разделяем
    if not parts:
        return None, []
    cmd = parts[0]
    args = parts[1:]
    return cmd, args

def main():
    vfs_name = "VFS"
    prompt = f"{vfs_name}$ "

    while True:
        try:
            user_input = input(prompt)
            cmd, args = parse_command(user_input)

            if cmd is None:
                continue 

            if cmd == "exit":
                break

            elif cmd in ["ls", "cd"]:
                print(f"[заглушка] команда: {cmd}, аргументы: {args}")

            else:
                print(f"ошибка: неизвестная команда: {cmd}")

        except KeyboardInterrupt:
            print("\nПрервано пользователем")
            break
        except EOFError:
            print("\nВыход")
            break

if __name__ == "__main__":
    main()