# https://contest.yandex.ru/contest/22781/run-report/134989979/
#
# -- ПРИНЦИП РАБОТЫ --
# Дек реализован на статическом массиве. Соблюдение границ массива обеспечено принципом кольцевого буфера.
# Держим указатели на первый и последний непустые элементы Дека.
# При записи элемента в Дек смещаем указатель на один индекс вправо (для головы Дека) или влево (для хвоста Дека)
# и записываем по новому указателю новое значение.
# При удалении элемента из Дека делаем обратную операцию - записываем по соответствующему указателю "нулевое" значение
# и смещаем указатели влево (для головы Дека) и вправо (для хвоста Дека).
# При попытке записать элемент в заполненный Дек или удалить элемент из пустого Дека возвращаем ошибку (буквально
# строку "error"), согласно условию задачи.
#
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Реализация Дека требует интерфейса для добавления и удаления элементов в конец и начало очереди.
# Корректная работа интерфейса гарантирована записью и удалением по соответствующим указателям на элементы нижележащего массивa.
# Корректное смещение индексов реализовано с помощью техники получения остатка
# от деления нового значения индекса на размер массива - принцип кольцевого буфера.
# От переполнения очереди защищает отслеживание текущего количества элементов в очереди при всех манипуляциях с Деком.
#
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Добавление в начало и конец Дека стоит O(1), потому что запись элемента в массив по индексу стоит O(1).
# По этой же причине извлечение из начала и конца Дека стоит O(1) - эти операции фактически являются
# присваиваением значения элементу массива по индексу. Массив статический, поэтому нет добавочной амортизированной
# сложности по времени, необходимой для копирования данных в новую область памяти - в обоих случаях строго O(1).
#
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Выделение памяти происходит под статический массив, в котором хранятся элементы Дека.
# Т.о. пространственная сложность составляет О(n), где n - размер очереди.


class Deque:
    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.items = [None] * cap
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.cap

    def push_front(self, value: int) -> None:
        if self.is_full():
            raise ValueError("stack is full")
        self.head = (self.head + 1) % self.cap
        self.items[self.head] = value
        self.size += 1
        return None

    def pop_front(self) -> int:
        if self.is_empty():
            raise ValueError("stack is empty")
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head - 1) % self.cap
        self.size -= 1
        return value

    def push_back(self, value: int) -> None:
        if self.is_full():
            raise ValueError("stack is full")
        self.items[self.tail] = value
        self.tail = (self.tail - 1) % self.cap
        self.size += 1
        return None

    def pop_back(self) -> int:
        if self.is_empty():
            raise ValueError("stack is empty")
        self.tail = (self.tail + 1) % self.cap
        value = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        return value


def read_input() -> tuple[int, list[tuple[str, int | None]]]:
    ops_num = input()
    cap = input()
    ops = []
    for _ in range(int(ops_num)):
        op_raw = input()
        op_split = op_raw.split()
        if len(op_split) > 1:
            ops.append((op_split[0], int(op_split[1])))
        else:
            ops.append((op_split[0], None))
    return int(cap), ops


if __name__ == "__main__":
    cap, ops = read_input()
    dq = Deque(cap)
    for op in ops:
        method_arg = op[1]
        try:
            if method_arg is None:
                print(getattr(dq, op[0])())
            else:
                res = getattr(dq, op[0])(op[1])
                if res is not None:
                    print(res)
        except ValueError:
            print("error")
