"""
    Output using print() function

    - The simplest way to produce output is using the print() function where you can pass zero or more expressions
    separated by commas. This function converts the expressions you pass into a string before writing to the screen.

    Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

    Parameters:
        - value(s) : Any value, and as many as you like. Will be converted to string before printed
        - sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
        - end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
        - file : (Optional) An object with a write method. Default :sys.stdout
        - flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

    Returns: It returns output to the screen.

    Should Learn:
    https://realpython.com/python-print/
"""

# Example:
text = f"Hello"
language = f"Python 3"

print(f"This is base print(): ", text, language)
print(f"This is print() with sep parameter: ", text, language, sep='')
print(f"This is print() with sep parameter: ", text, language, sep='\n')
print(f"This is print() with end parameter: ", text, language, sep='\n')

with open('write_with_print.txt', mode='w') as write_with_print:
    print('Hello Python 3 !', file=write_with_print)

print(
    '==============================================================================================================='
    '==============================================================================================================='
)

"""
    Biến và Kiểu Dữ Liệu - Variables and Types

    - Python is completely object oriented, and not "statically typed". You do not need to declare variables
    before using them, or declare their type.
    - Every variable in Python is an "object".
    This tutorial will go over a few basic types of variables.

    (Google Translate)

    - Python hoàn toàn là hướng đối tượng và không được "statically typed" (statically typed - gõ tĩnh). Bạn không cần
    khai báo biến trước khi sử dụng hoặc khai báo kiểu của chúng.
    - Mọi biến trong Python là một "đối tượng".

    Source:
    https://www.learnpython.org/en/Variables_and_Types
"""

"""
    Kiểu None - None

    The sole value of the type NoneType. None is frequently used to represent the absence of a value,
    as when default arguments are not passed to a function. Assignments to None are illegal and raise a SyntaxError.

    (Google Translate)

    Giá trị duy nhất của kiểu NoneType. Không có giá trị nào thường được sử dụng để biểu thị sự vắng mặt
    của một giá trị, như khi các đối số mặc định không được truyền cho một hàm. Việc chuyển nhượng cho Không là
    bất hợp pháp và gây ra lỗi SyntaxError.

    More Information:
    https://docs.python.org/3.2/library/constants.html#:~:text=The%20sole%20value%20of%20the,illegal%20and%20raise%20a%20SyntaxError.
"""

# None

none_variable = None

print(f"This is None Type: {type(None)} - {type(none_variable)} - None Value: {none_variable}")

print(
    '==============================================================================================================='
    '==============================================================================================================='
)

"""
    Kiểu Số - Numbers

    - Python supports two types of numbers - integers and floating point numbers.
    (It also supports complex numbers, which will not be explained in this tutorial).

    (Google Translate)

    Python hỗ trợ hai loại số - số nguyên và số dấu phẩy động (Số thập phân).
    (Nó cũng hỗ trợ số phức, điều này sẽ không được giải thích trong hướng dẫn này).

"""

# Number

first_int = 1           # first_int là biến - 1 là số, loại "số nguyên" (first_init is Variable - 1 is number. Type is Integer)
second_int = 3          # second_int là biến - 3 là số, loại "số nguyên" (second_int is Variable - 3 is number. Type is Integer)
third_int = 4.3         # third_int là biến - 4.3 là số, loại số thập phân (third_int is Variable, 4.3 is number. Type is Float)
fourth_int = 10 + 1j    # fourth_int là biến - 10 + 1j là số, loại số phức (fourth_int is Variable, 10 + 1j is number. Type is Complex)

print(
    f"Using Function type() To check Type of Variable - Sử dụng hàm type() để kiểm tra kiểu dữ liệu của biến \n",
    f"This is type of first_init variable: {type(first_int)} - ({first_int}) \n",
    f"This is type of second_int variable: {type(second_int)} - ({second_int}) \n",
    f"This is type of third_int variable: {type(third_int)} - ({third_int}) \n",
    f"This is type of fourth_int variable: {type(fourth_int)} - ({fourth_int}) \n",
    sep='',
    end='\n'
)

print(
    '==============================================================================================================='
    '==============================================================================================================='
)

# Note \n is a escape sequence in Python 3 (Mean: New Line) - More Information: http://www.python-ds.com/python-3-escape-sequences


"""
    Kiểu Chuỗi - Strings
    - Strings are defined either with a single quote or a double quotes.

    (Google Translate)

    - Các chuỗi được định nghĩa bằng một dấu nháy đơn hoặc dấu nháy kép.
"""

# Strings

greeting = 'Hello'
language = 'Python 3'

"""
    The difference between the two is that using double quotes makes it easy to include apostrophes
    (whereas these would terminate the string if using single quotes)
"""

apostrophes = "Don't worry about apostrophes"

print(
    f"This is Strings: ",
    greeting,
    language,
    apostrophes,
    end='\n'
)

print(
    '==============================================================================================================='
    '==============================================================================================================='
)

"""
    - Các toán tử đơn giản có thể thực hiện trên "Số" và "Chuỗi"
    - Simple operators can be executed on numbers and strings
"""

x = 1
y = 3
z = x + y  # Tương đương với z = 1 + 2. (This is like z = 1 + 2)
print(f"Value z: {z}", end='\n')

hello = 'Hello'
person_name = 'Nguyen Duc Hoang'
greeting = hello + ' ' + person_name # Tương đương với greeting = Hello Nguyen Duc Hoang. (This is like greeting = Hello Nguyen Duc Hoang)
same_greeting = f"{hello} {person_name}"

print(
    f"This is greeting: {greeting}",
    f"This is same_greeting: {same_greeting}",
    sep='\n',
    end='\n'
)

print(
    '==============================================================================================================='
    '==============================================================================================================='
)

# Assignments can be done on more than one variable "simultaneously" on the same line like this
# Bài tập có thể được thực hiện trên nhiều biến "đồng thời" trên cùng một dòng như thế này

a, b = 1, 3
print(f"This is Value a: {a}", f"This is Value b: {b}")

print(
    '==============================================================================================================='
    '==============================================================================================================='
)
# Note Can't Plus "String" With "Number" - Không Thể Cộng Hai Kiểu Dữ Liệu Khác Nhau


"""
    Toán tử số học - Arithmetic Operators.

    What are operators in python?
    - Operators are special symbols in Python that carry out arithmetic or logical computation.
    - The value that the operator operates on is called the operand.

    (Google Translate)

    Toán tử trong python là gì?
    - Toán tử là các ký hiệu đặc biệt trong Python thực hiện tính toán số học hoặc logic.
    - Giá trị mà toán tử hoạt động được gọi là toán hạng.

    - Source:
    https://www.programiz.com/python-programming/operators
"""

# For example:
2 + 3

print(2 + 3)

print(
    '==============================================================================================================='
    '==============================================================================================================='
)

# Arithmetic Operators
"""
    Operator                        Meaning                                                   Example
        +               Add two operands or unary plus                                        x + y+ 2
                        (Thêm hai toán hạng hoặc cộng một bậc - Google Translate)

    Note:
    - Unary plus (+) trả về giá trị của chính toán hạng đó, bạn sẽ không cần phải 
    sử dụng toán tử này vì nó không cần thiết.
    - Unary minus (-) trả về số đối của toán hạng đó.
    Source :
    https://www.howkteam.vn/course/khoa-hoc-lap-trinh-c-can-ban/toan-tu-so-hoc-toan-tu-tang-giam-toan-tu-gan-so-hoc-trong-c-operators-1145

        -               Subtract right operand from the left or unary minus                   x - y- 2

        *               Multiply two operands                                                 x * y

        /               Divide left operand by the right one (always results into float)
                        (Toán tử phép chia, (Luôn trả về kiểu dữ liệu Float) - Vd: 2/2 = 1.0)

        %               Modulus - remainder of the division of left operand by the right      x % y (remainder of x/y)
                        (Toán tử chia lấy phần dư)

        //              Floor division - division that results into whole number              x // y
                        adjusted to the left in the number line
                        (Toán tử chia làm tròn xuống)

        **              Exponent - left operand raised to the power of right                  x**y (x to the power y)

"""

# Arithmetic Operators Example - Ví dụ
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)


print(
    '==============================================================================================================='
    '==============================================================================================================='
)


"""
    Toán tử so sánh - Comparison operators

    Comparison operators are used to compare values. It returns either True or False according to the condition.

    (Google Translate)

    Toán tử so sánh được sử dụng để so sánh các giá trị. Nó trả về True hoặc False tùy theo điều kiện.
"""

# Comparison operators

"""
    Operator                    Meaning                                                                     Example
        >           Greater than - True if left operand is greater than the right                           x > y

        <           Less than - True if left operand is less than the right                                 x < y

        ==          Equal to - True if both operands are equal                                              x == y

        !=          Not equal to - True if operands are not equal                                           x != y

        >=          Greater than or equal to - True if left operand is greater than or equal to the right   x >= y

        <=          Less than or equal to - True if left operand is less than or equal to the right         x <= y
"""

# Comparison operators Example

x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)


print(
    '==============================================================================================================='
    '==============================================================================================================='
)


"""
    Toán tử Logic - Logical operators

    Logical operators are the and, or, not operators.
"""

# Logical operators

"""
    Operator                    Meaning                                                     Example
        and             True if both the operands are true                                  x and y

        or              True if either of the operands is true                              x or y

        not             True if operand is false (complements the operand)                  not x
"""

# Logical operators Example

x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

"""
    Out Put
    - x and y is False
    - x or y is True
    - not x is False
"""

print(
    '==============================================================================================================='
    '==============================================================================================================='
)


"""
    Bitwise operators

    Note:
    - Toán tử này thực hiện trên các bit của các giá trị. Hãy tưởng tượng mình có 2 biến a = 12 và b = 15 nhưng nếu 
    chúng ta convert chúng sang hệ nhị phân thì 2 biến này sẽ có giá trị như sau: a = 00001100 và b = 00001111.

    Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

    (Google Translate)

    Toán tử bitwise hoạt động trên các toán hạng như thể chúng là các chuỗi chữ số nhị phân. Chúng hoạt động từng chút 
    một, do đó có tên.

    For example, 2 is 10 in binary and 7 is 111.
"""

# Bitwise operators

"""
    Operator                    Meaning                                 Example
        &                       Bitwise AND                             x & y = 0 (0000 0000)

        |                       Bitwise OR                              x | y = 14 (0000 1110)

        ~                       Bitwise NOT                             ~x = -11 (1111 0101)

        ^                       Bitwise XOR                             x ^ y = 14 (0000 1110)

        >>                      Bitwise right shift                     x >> 2 = 2 (0000 0010)

        <<                      Bitwise left shift                      x << 2 = 40 (0010 1000)
"""


"""
    Toán tử gán - Assignment operators

    Assignment operators are used in Python to assign values to variables.

    a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

    There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same.
    It is equivalent to a = a + 5.

    (Google Translate)

    Toán tử gán được sử dụng trong Python để gán giá trị cho các biến.

    a = 5 là một toán tử gán đơn giản để gán giá trị 5 ở bên phải cho biến a ở bên trái.

    Có nhiều toán tử ghép khác nhau trong Python như + = 5 để thêm vào biến và sau đó gán giống nhau.
    Nó tương đương với a = a + 5.
"""

# Assignment operators

"""
    Operator                    Meaning                                 Example
    =                           x = 5                                   x = 5

    +=                          x += 5                                  x = x + 5

    -=                          x -= 5                                  x = x - 5

    *=                          x *= 5                                  x = x * 5

    /=                          x /= 5                                  x = x / 5

    %=                          x %= 5                                  x = x % 5

    //=                         x //= 5                                 x = x // 5

    **=                         x **= 5                                 x = x ** 5

    &=                          x &= 5                                  x = x & 5

    |=                          x |= 5                                  x = x | 5

    ^=                          x ^= 5                                  x = x ^ 5

    >>=                         x >>= 5                                 x = x >> 5

    <<=                         x <<= 5                                 x = x << 5
"""


"""
    Toán tử đặc biệt (Toán tử xác thực) - Special operators

    Note:
    - Dạng Toán tử này dùng để xác thực hai giá trị xem nó có bằng nhau hay không. Và trong Python 
    hỗ trợ chúng ta 2 dạng sau:
        + Giả sử: a = 4, b =5

    Source:
    https://toidicode.com/cac-toan-tu-co-ban-trong-python-349.html

    - Python language offers some special types of operators like the identity operator or the membership operator. 
    - They are described below with examples.

    Identity operators

    - "is" and "is not" are the identity operators in Python. They are used to check if two values (or variables) are 
    located on the same part of the memory.
    - Two variables that are equal does not imply that they are identical.

    (Google Translate)

    - Ngôn ngữ Python cung cấp một số loại toán tử đặc biệt như toán tử nhận dạng hoặc toán tử thành viên. 
    - Chúng được mô tả dưới đây với các ví dụ.

    Toán tử nhận dạng

    - "is" và "is not" là các toán tử nhận dạng trong Python. Chúng được sử dụng để kiểm tra xem hai giá trị (hoặc biến) 
    có nằm trên cùng một phần của bộ nhớ hay không.
    - Hai biến bằng nhau không có nghĩa là chúng giống hệt nhau.
"""

# Special operators

"""
    Operator                    Meaning                                                             Example
    is              True if the operands are identical (refer to the same object)                   x is True

    is not          True if the operands are not identical (do not refer to the same object)        x is not True
"""

# Special operators Example (Identity operators in Python)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


print(
    '==============================================================================================================='
    '==============================================================================================================='
)


"""
    Toán tử khai thác - Membership operators

    - "in" and "not in" are the membership operators in Python. They are used to test whether a value or variable is 
    found in a sequence (string, list, tuple, set and dictionary).

    - In a dictionary we can only test for presence of key, not the value.

    (Google Translate)

    - "in" và "not int" là các toán tử thành viên trong Python. Chúng được sử dụng để kiểm tra xem một giá trị hoặc biến 
    được tìm thấy trong một chuỗi (chuỗi, danh sách, bộ, bộ và từ điển).

    - Trong từ điển, chúng ta chỉ có thể kiểm tra sự hiện diện của khóa chứ không phải giá trị.
"""

# Membership operators

"""
    Operator                    Meaning                                         Example
    in              True if value/variable is found in the sequence             5 in x

    not in          True if value/variable is not found in the sequence         5 not in x
"""

# Membership operators Example (Membership operators in Python)
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
