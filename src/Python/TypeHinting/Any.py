from typing import Any, Mapping


class Employee:
    ...


class Manager(Employee):
    ...


worker: Employee = Employee()
worker = Manager()

boss: Manager = Manager()
boss = Employee()


# Сравните поведение `Any` с поведением `object`. Похожий на `Any`, каждый тип является подтипом `object`. Однако, в
# отличие от `Any`, обратное неверно: объект не является подтипом любого другого типа.

# `object` может быть приведен к более конкретному типу, в то время как `Any` на самом деле означает, что все допустимо,
# и средство проверки типов отключается от любого использования объекта (даже если вы позже присвоите такому объекту
# имя, которое проверено на тип).

# Если вы написали функцию в нетипизированном случае, приняв list, что сводится к тому же, что и List[Any].
# Проверка типов там отключена и возвращаемое значение больше не имеет значения, но так как ваша функция принимает
# список, содержащий `Any` объекты, правильное возвращаемое значение будет `Any` здесь.

def some_func() -> Any: ...


somthing = some_func()

worker = some_func()
somthing = worker
worker = somthing

# `Any` можно считать типом который имеет все значения и все методы. В сочетании с определением подтип выше, это места

# `Any` частично вверху (имеет все значения) и нижний (у него есть все методы) иерархии типов. Сравните это
# с `object` - это не соответствует большинство типов (например, вы не можете использовать object() случай, когда `int`
# ожидается). оба `Any` и `object` иметь в виду «любой тип разрешен» при использовании для аннотации аргумента, но
# только `Any` может быть передан независимо от ожидаемого типа (по сути, `Any`объявляет откат к динамической типизации
# и закрывает жалобы из статической проверки).

# Или проще говоря

# Особым типом является `Any`. Статическая программа проверки типов будет рассматривать каждый тип как совместимый с
# `Any`, а `Any` как совместимость с любым типом.
# Это означает, что можно выполнить любую операцию или вызов метода над значением типа `Any` и присвоить его любой
# переменной:

a = None    # type: Any
a = []      # OK
a = 2       # OK

s = ''      # type: str
s = a       # OK


def foo(item: Any) -> int:

    # Typechecks; 'item' could be any type,
    # and that type might have a 'bar' method

    item.bar()
    return 0

# Итог: любой тип может быть Any, но Any не может быть любым типом. Any является подмножетсвом всех типов.
# object - класс, а не тип, но при этом производные от object - классы/типы, следственно object != Any.

# Отличие класса от типа:
# Класс - фабрика экземпляров этиго класса, тип это - Union[int, str], от него нельзя создавать экземпляров.
# Так же от Union[int, str] нельзя наследоваться.
# Смотрите - Union.py

# Когда тип значения object, средство проверки типов отклонит почти все операции над ним, и присвоение его переменной
# (или использование это как возвращаемое значение) более специализированного типа является ошибкой типа. На с другой
# стороны, когда значение имеет тип Any, средство проверки типов разрешить все операции над ним, а значение типа Any
# может быть назначен в переменную (или используемую в качестве возвращаемого значения) более ограниченного типа.
#
# Предполагается, что параметр функции без аннотации аннотирован с помощью Any. Если универсальный тип используется
# без указания параметров типа, предполагается, что они Any:


def use_map(m: Mapping) -> None:  # Тоже самое, что и Mapping[Any, Any]
    ...

# Это правило распространяется и на Tuple, в контексте аннотации это эквивалентно к Tuple[Any, ...]и, в свою очередь,
# к tuple. К тому же голый Callableв аннотации эквивалентно Callable[..., Any]

# Резюме:
#
# C `Any` объектом можно делать всё что угодно, для него статический анализатор отключается.
# С `object` можно делать не всё: обращаться с ним можно только как с экземпляром ojbect. Статический анализатор
# проверяет тип.
