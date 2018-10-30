---
layout: post
title:  "Python Type Hint 类型系统提示"
subtitle: "programming language"
date:   2018-10-25 18:00:05 -0400
background: '/img/posts/type/type.jpg'
categories: Programming
---
# Python Type Hint 类型系统提示
## 目的
用类型提示来写出让人更容易理解的代码，也防止自己写过之后几个月忘了。

## 基本语法
```
def greeting(name: str) -> str:
    return 'Hello ' + name
```
类似静态语言的写法
## 内容
#### None
用None来替代type(None)

#### Type 别名
```
Url = str

def retry(url: Url, retry_count: int) -> None:
    pass
```
一般将别名的第一个字母大写来区别。一般用```TypeVar```来定义类型，
```
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def dilate(v: Vector[T], scale: T) -> Vector[T]:
    return ((x * scale, y * scale) for x, y in v)
```

#### Callable 函数参数
用```Callble[[Arg1Type.7 type check,Arg2Type], ReturnType]```来定义函数签名中的回调函数
```
from typing import Callable

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    # Body

def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    # Body
    # ...可以替代list
```

#### Generics 泛型
一个函数，能处理多种类型，如果我们一样样类型去定义，会很繁琐，可以用一种通用类型，即泛型来替代函数签名类型
```
from typing import Sequence, TypeVar

T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]
```
其中，用T来替代泛型

#### 用户自定义泛型
可以来自定义自己的泛型类型，
```
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('{}: {}'.format(self.name, message))
```
这样```LoggedVar```就是用户自定义的泛型了，具有```set``` ```get``` ```log```等方法

#### 类型变量的范围规则

```
from typing import TypeVar, Generic

T = TypeVar('T')

class MyClass(Generic[T]):
    def meth_1(self, x: T) -> T: ... # T here
    def meth_2(self, x: T) -> T: ... # and here are always the same

a = MyClass() # type: MyClass[int]
a.meth_1(1)   # OK
a.meth_2('a') # This is an error! 
```
需要用**注释**来确认```a```的类型
```
T = TypeVar('T')
S = TypeVar('S')

class Outer(Generic[T]):
    class Bad(Iterable[T]):      # Error
        ...
    class AlsoBad:
        x = None # type: List[T] # Also an error

    class Inner(Iterable[S]):    # OK
        ...
    attr = None # type: Inner[T] # Also OK
```
在通用类里不能用相同的类

#### 在运行时确认泛型类的类型
```
from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    x = None  # type: T  # Instance attribute (see below)
    def __init__(self, label: T = None) -> None:
        ...

x = Node('')  # Inferred type is Node[str]
y = Node(0)   # Inferred type is Node[int]
z = Node()    # Inferred type is Node[Any]
```
与上面不同的是，在运行时才能确认泛型的类型

#### 类型擦除
```
p = Node[int]()
q = Node[str]()
```
这两个实际还是同一类型，因为类型擦除的缘故，他俩还是Node类型，泛型必须要有运行时间后才能确认

#### 类型bound
```
from typing import TypeVar

class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
    ... # __gt__ etc. as well

CT = TypeVar('CT', bound=Comparable)

def min(x: CT, y: CT) -> CT:
    if x < y:
        return x
    else:
        return y

min(1, 2) # ok, return type int 
min('x', 'y') # ok, return type str
```
只有实现了```__lt__```方法的类型，才能进行比较，这个我觉得可以用于接口的检测，比如只有实现了特定接口的类型，才能作为特定函数的参数

#### 类型的变异
默认情况下，默认一类通过的函数，此类的父类或子类不能通过。通过改变继承的参数```covariant=True```可以将父类或子类也通过检查，`_co`常作为此种泛型的后缀。

#### 类型自身函数的参数是类型本身
```
class Tree:
    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right
```
目前会报错，所以用str来替代
```
class Tree:
    def __init__(self, left: 'Tree', right: 'Tree'):
        self.left = left
        self.right = right
```

#### Union
Union[T1,T2,..] 可以是T1,T2...的子集(即可以是其中的任何一个)。
```
def handle_employee(e: Union[Employee, None]) -> None: ...
```
可以用```Union```来替代```Optional ```

#### Any
用```Any``` type 来代替所有的类型

#### NoReturn

用```NoReturn```确保不会返回任何值

#### 只传递类型到参数，而不是类型的实例

```
def new_user(user_class):
    user = user_class()
    # (Here we could write the user object to a database)
    return user
```
类似工厂函数，只是传递类型，用```Type```关键字
```
U = TypeVar('U', bound=User)
def new_user(user_class: Type[U]) -> U:
    ...
```

## 检查
1. ```pip install mypy``` 安装```mypy```模块
2. ```mypy your_func.py``` 用```mypy``` 去检查写的程序