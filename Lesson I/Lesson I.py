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
"""