## Ответы на контрольные вопросы:
1.  В чем основная идея __полиморфизма__? Как он реализуется в Python.
    Основная идея полиморфизма заключается в том, что объект может принимать разные формы в зависимости от контекста,
    то есть один и тот же код может работать с объектами разных типов, не требуя явного указания типа
    Как он реализуется?
    В python полиморфизм реализуется с помощью наследования и динамической типизации
    1. Наследование
        Классы могут наследовать от других классов, переопределяя методы родительского класса. Это позволяет одному и тому же методу иметь разную реализацию в разных классах\
    2. Динамическая типизация
    Тип переменной определяется во время выполнения программы, а не во время компиляции

2. Зачем переопределять метод `__radd__()` наравне с __add__()`?
    Переопределение __add__() и __radd__() в Python делает сложение с объектами класса коммутативным. 
    __add__() используется, когда объект класса стоит слева от оператора +
    __radd__() используется, когда объект класса стоит справа от оператора +
    Это позволяет складывать объекты класса как с другими объектами этого же класса, так и с другими типами данных

3. Как можно описать взаимоотношения родительского и дочернего классов?
    Родительский класс – это общий шаблон, а дочерний класс – это его более специализированная версия, которая наследует его свойства и поведение
    Дочерний класс может добавлять свои уникальные особенности и переопределять поведение родительского класса

4. Для чего используется ключевое слово super()?
    super() в Python используется для доступа к методам родительского класса из дочернего класса
    Инициализация: super().__init__() вызывается для инициализации родительских свойств
    Переопределение: super().method_name() позволяет расширить поведение метода, унаследованного от родительского класса
    C3 MRO - это алгоритм поиска методов, который используется в питоне 
    super() использует C3 MRO, чтобы определить, какой класс-предок нужно использовать для вызова метода

5. Какую роль играет порядок классов предков при множественном наследовании?
    Порядок классов предков при множественном наследовании определяет, какой из методов будет вызван, если у нескольких предков есть одинаковый метод
    Python использует алгоритм C3 MRO (Method Resolution Order) для определения порядка поиска методов.
    Правильный порядок линейный поиск, помогает избежать проблем с многократным наследованием

6. Зачем нужна __обработка исключений__? В каких случаях ее использование некорректно?
    Обработка исключений - это механизм, который позволяет программе продолжать работу, даже если во время выполнения возникает ошибка (исключение). 
    Вместо того, чтобы завершаться, программа перехватывает исключение и выполняет код, прописанный в блоке except
    Использование обработки исключений не всегда является оптимальным решением.
    В некоторых случаях  более  подходящим  будет  проверить  возможные  ошибки  с помощью  условных  операторов  и  предложить  пользователю  ввести  корректное  значение,  вместо  того  чтобы  перехватывать  исключение

7. Зачем в блоке `try` использовать раздел `finally`?
    Код в блоке finally выполняется всегда, даже если в блоке try возникло исключение, которое не было перехвачено в except, или если в блоке try произошло прерывание выполнения

8. Что нужно сделать, чтобы реализовать свое собственное __исключение__?
    Создать новый класс, наследующий от базового класса исключений (или его подкласса)

9. Чем итератор отличается от генератора?
    Итератор - это объект, который позволяет перебирать последовательность элементов по одному
    Генератор - это специальный тип итератора, который создает значения по факту, а не хранит их все в памяти

10. В чем минусы декорирования функций?
    Декораторы могут неожиданно изменять поведение функции
    Может происходить частичная потеря информации, так как декоратор получает только функцию, а не ее аргументы
