"""
    This is Lesson 2. It was written by Nguyễn Đức Hoàng

    Contents:
    - Comment In Python 3
    - Variable In Python 3                      ** Important
    - Some Operators In Python 3
"""

"""
    Why Need Comment In Python - Tại sao cần Commnet trong Python
    
    - Comments can be used to explain Python code.
    - Comments can be used to make the code more readable.
    - Comments can be used to prevent execution when testing code.
    
    Google Translate
    - Nhận xét có thể được sử dụng để giải thích mã Python.
    - Nhận xét có thể được sử dụng để làm cho mã dễ đọc hơn.
    - Chú thích có thể được sử dụng để ngăn chặn việc thực thi khi kiểm tra mã.
"""

# Comments starts with a #, and Python will ignore them:

# Example

# This is a comment
print("Hello, World!")

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# Comments can be placed at the end of a line, and Python will ignore the rest of the line:

# Example

print("Hello, World!")  # This is a comment

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Multi Line Comments: (Nhận xét nhiều dòng)
    - Python does not really have a syntax for multi line comments.
    - To add a multiline comment you could insert a # for each line:
    
    - Or, not quite as intended, you can use a multiline string.
    - Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string 
    (triple quotes) in your code, and place your comment inside it:
    
    Google Translate
    - Python không thực sự có cú pháp cho nhận xét nhiều dòng.
    - Để thêm nhận xét nhiều dòng, bạn có thể chèn dấu # cho mỗi dòng:
    
    - Hoặc, không hoàn toàn như dự định, bạn có thể sử dụng một chuỗi nhiều dòng.
    - Vì Python sẽ bỏ qua các ký tự chuỗi không được gán cho một biến, bạn có thể thêm một chuỗi nhiều dòng
    (ba dấu ngoặc kép) trong mã của bạn và đặt nhận xét của bạn bên trong nó:
"""

# Example

"""
    This is a comment
    written in
    more than just one line
"""

print("Hello, World!")

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# =====================================================================================================================


"""
    Variable Python - Biến Trong Python
    - What is variable? - Biến là gì?
"""

"""
    Biến là tên một vùng trong bộ nhớ Ram, được sử dụng để lưu trữ thông tin, bạn có thể gán thông tin cho một biến, 
    hoặc lấy thông tin đó ra để sử dụng khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho biến đó.
    
    Source: 
    https://www.howkteam.vn/course/kieu-du-lieu-list-trong-python--phan-1/bien-trong-python-1539
"""

# Example

name = "Hoang"

number = 121994

print(
    f"This is Type of Variable and Variable ID in Ram: ",
    f"Type of Variable name: {type(name)} - Variable ID in Ram of Variable name: {id(name)}",
    f"Type of Variable number: {type(number)} - Variable ID in Ram of Variable number: {id(number)}",
    sep='\n'
)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Note: 
    - Id mỗi Variable (Biến) sẽ khác nhau.
"""

"""
    Important Note (Python ID):
    - Python id() function returns the “identity” of the object. The identity of an object is an integer, which is 
    guaranteed to be unique and constant for this object during its lifetime.
    
    - Two objects with non-overlapping lifetimes may have the same id() value. In CPython implementation, this is the 
    address of the object in memory.
    
    Google Translate:
    - Hàm id () trong Python trả về “danh tính” của đối tượng. Nhận dạng của một đối tượng là một số nguyên,
    được đảm bảo là duy nhất và không đổi cho đối tượng này trong suốt thời gian tồn tại của nó.
    
    - Hai đối tượng có vòng đời không trùng nhau có thể có cùng giá trị id (). Trong triển khai CPython, đây là
    địa chỉ của đối tượng trong bộ nhớ.
    
    
    Source: 
    https://www.journaldev.com/22925/python-id
"""

"""
    - Python cache the id() value of commonly used data types, such as string, integer, tuples etc. So you might find 
    that multiple variables refer to the same object and have same id() value if their values are same.
    
    Google Translate
    
    - Python lưu vào bộ nhớ cache giá trị id() của các kiểu dữ liệu thường được sử dụng, chẳng hạn như chuỗi, số nguyên, 
    bộ giá trị, vv... Vì vậy, bạn có thể thấy rằng nhiều biến tham chiếu đến cùng một đối tượng và có cùng giá trị id() 
    nếu giá trị của chúng giống nhau.
"""

# Example

a = 10
b = 10
c = 11
d = 12

print(
    f"This is IDs: {id(a)} - {id(b) - id(10)}",
    f"This is IDs: {id(a)} - {id(b)} - {id(c)} - {id(d)}",
    sep='\n'
)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    *** Caching can work only with immutable objects, notice that integer, string, tuples are immutable. So Python 
    implementation can use caching to save memory space and improve performance.
    
    Google Translate:
    *** Bộ nhớ đệm chỉ có thể hoạt động với các đối tượng không thay đổi, lưu ý rằng số nguyên, chuỗi, bộ giá trị là 
    bất biến. Vì vậy việc triển khai Python có thể sử dụng bộ nhớ đệm để tiết kiệm không gian bộ nhớ và cải 
    thiện hiệu suất.
"""

# =====================================================================================================================

"""
    String (Python) - Chuỗi Trong Python
    
    Source: 
    https://www.programiz.com/python-programming/string
    https://o7planning.org/vi/11423/huong-dan-su-dung-string-trong-python
"""

"""
    Define - Định Nghĩa
    
    - A string is a sequence of characters.

    - A character is simply a symbol. For example, the English language has 26 characters.

    - Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on 
    your screen, internally it is stored and manipulated as a combination of 0s and 1s.

    - This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and 
    Unicode are some of the popular encodings used.

    - In Python, a string is a sequence of Unicode characters. Unicode was introduced to include every character in all 
    languages and bring uniformity in encoding. You can learn about Unicode from Python Unicode. 
    
    Google Translate
    
    - Một chuỗi là một chuỗi các ký tự.

    - Một ký tự chỉ đơn giản là một biểu tượng. Ví dụ, ngôn ngữ tiếng Anh có 26 ký tự.

    - Máy tính không xử lý các ký tự, chúng xử lý các số (nhị phân). Mặc dù bạn có thể thấy các ký tự trên màn hình của 
    mình, nhưng bên trong nó vẫn được lưu trữ và thao tác dưới dạng kết hợp của số 0 và số 1.

    - Quá trình chuyển đổi ký tự thành số này được gọi là mã hóa và quá trình ngược lại là giải mã. ASCII và Unicode là 
    một số bảng mã phổ biến được sử dụng.

    - Trong Python, một chuỗi là một chuỗi các ký tự Unicode. Unicode được giới thiệu để bao gồm mọi ký tự trong tất cả 
    các ngôn ngữ và mang lại sự đồng nhất trong bảng mã. Bạn có thể tìm hiểu về Unicode từ Python Unicode.
"""

"""
    Defining String In Python 3
"""

# Example

first_name = "Nguyễn"
last_name = "Đức Hoàng"
year = "1994"

# triple quotes string can extend multiple lines
program_language = """
    Well come to learning:
    - Python 3
"""

print(first_name)
print(last_name)
print(year)
print(program_language)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    How to access characters in a string? - Làm thế nào để truy cập các kí tự trong chuỗi?
    
    - We can access individual characters using indexing and a range of characters using slicing. Index starts from 0. 
    Trying to access a character out of index range will raise an IndexError. The index must be an integer. We can't 
    use floats or other types, this will result into TypeError.
    
    - Python allows negative indexing for its sequences.
    
    - The index of -1 refers to the last item, -2 to the second last item and so on. We can access a range of items in 
    a string by using the slicing operator :(colon).
    
    Google Translate
    - Chúng ta có thể truy cập các ký tự riêng lẻ bằng cách sử dụng lập chỉ mục và một loạt các ký tự bằng cách sử dụng 
    slicing. Index bắt đầu từ 0. Cố gắng truy cập một ký tự ngoài phạm vi Index sẽ làm xuất hiện lỗi Index. Index 
    phải là một số nguyên. Chúng tôi không thể sử dụng Fload hoặc các loại biến khác, điều này sẽ dẫn đến lỗi TypeError.
    
    - Python cho phép lập chỉ mục âm cho các chuỗi của nó.
    
    - Chỉ số -1 đề cập đến mục cuối cùng, -2 đến mục cuối cùng thứ hai, v.v. Chúng ta có thể truy cập một loạt các mục 
    trong một chuỗi bằng cách sử dụng toán tử cắt: (dấu hai chấm).
"""

# Accessing string characters in Python

str = 'programiz'
print('str = ', str)

# first character

print('str[0] = ', str[0])

# last character

print('str[-1] = ', str[-1])

# slicing 2nd to 5th character

print('str[1:5] = ', str[1:5])

# slicing 6th to 2nd last character

print('str[5:-2] = ', str[5:-2])

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    How to change or delete a string? - Làm thế nào để thay đổi hoặc xóa chuỗi?
    
    - Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. We 
    can simply reassign different strings to the same name.
    
    - We cannot delete or remove characters from a string. But deleting the string entirely is possible using the 
    "del" keyword.
    
    Google Translate
    - Chuỗi là bất biến. Điều này có nghĩa là các phần tử của một chuỗi không thể thay đổi khi chúng đã được gán. 
    Chúng ta có thể chỉ cần gán lại các chuỗi khác nhau cho cùng một tên.
    
    - Chúng tôi không thể xóa hoặc loại bỏ các ký tự khỏi một chuỗi. Nhưng có thể xóa hoàn toàn chuỗi bằng cách sử dụng
     từ khóa "del".
"""

# Example

my_string = 'programiz'

# my_string[5] = 'a'  # TypeError: 'str' object does not support item assignment

# Delete character

del my_string

# print(my_string)  # NameError: name 'my_string' is not defined


print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Python String Operations
    
    - There are many operations that can be performed with strings which makes it one of the most used data types in
     Python.

    Google Translate
    - Có rất nhiều thao tác có thể được thực hiện với chuỗi, điều này khiến nó trở thành một trong những kiểu dữ liệu 
    được sử dụng nhiều nhất trong Python.
"""

"""
    Concatenation of Two or More Strings - Nối hai hoặc nhiều chuỗi
"""

# Example

first_name = "Nguyễn"
last_name = "Đức Hoàng"
year = "1994"

# Using Plus (+)
print("This is First Name and Last Name:", first_name + ' ' + last_name)

print(f"This is First Name and Last Name: {first_name + ' ' + last_name}")

print(f"This is First Name and Last Name: {first_name} {last_name}")

print('This is First Name and Last Name: {} {}'.format(first_name, last_name))

# using *
print("First Name * 3", first_name * 3)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Iterating Through a string - Lặp lại từng kí tự trong chuỗi

    - We can iterate through a string using a for loop. Here is an example to count the number of 'l's in a string.
    
    Google Translate
    - Chúng ta có thể lặp qua một chuỗi bằng vòng lặp for. Đây là một ví dụ để đếm số lượng 'l trong một chuỗi.
"""

# Example:  Iterating through a string

count = 0
for letter in 'Hello World':
    if (letter == 'l'):
        count += 1
print(count, 'letters found')

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    String Membership Test - Kiểm tra kí tự trong chuỗi

    - We can test if a substring exists within a string or not, using the keyword in.
    
    Google Translate
    - Chúng ta có thể kiểm tra xem một chuỗi con có tồn tại trong một chuỗi hay không bằng cách sử dụng từ khóa "in".
"""

# Example

print('a' in 'program')

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Built-in functions to Work with Python - Các hàm tích hợp để làm việc trong Python 3

    - Various built-in functions that work with sequence work with strings as well.

    - Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object. 
    It contains the index and value of all the items in the string as pairs. This can be useful for iteration.

    - Similarly, len() returns the length (number of characters) of the string.
    
    Google Translate
    - Các hàm tích hợp khác nhau hoạt động với trình tự cũng hoạt động với chuỗi.

    - Một số cái thường được sử dụng là enumerate() và len(). Hàm enumerate() trả về một index liệt kê. 
    Nó chứa index và giá trị của tất cả các mục trong chuỗi dưới dạng cặp. Điều này có thể hữu ích cho việc lặp lại.

    - Tương tự, len() trả về độ dài (số ký tự) của chuỗi.
"""

# Example

str = 'cold'

# enumerate()

list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# character count

print('len(str) = ', len(str))

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Escape Sequence - Trình tự thoát
    
    Learning More Source:
    https://www.programiz.com/python-programming/string
"""

"""
    The format() Method for Formatting Strings
    
    - The format() method that is available with the string object is very versatile and powerful in formatting strings.
     Format strings contain curly braces {} as placeholders or replacement fields which get replaced.

    - We can use positional arguments or keyword arguments to specify the order.
    
    Google Translate
    - Phương thức format () có sẵn với đối tượng chuỗi rất linh hoạt và mạnh mẽ trong việc định dạng chuỗi. Chuỗi định 
    dạng chứa dấu ngoặc nhọn {} làm phần giữ chỗ hoặc trường thay thế được thay thế.

    - Chúng ta có thể sử dụng đối số vị trí hoặc đối số từ khóa để chỉ định thứ tự.
"""

# Example
# Python string format() method

# default(implicit) order

default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
print('\n--- Default Order ---')
print(default_order)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# order using positional argument

positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
print('\n--- Positional Order ---')
print(positional_order)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# order using keyword argument

keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

"""
    Note: 
    - The format() method can have optional format specifications. They are separated from the field name using colon. 
    For example, we can left-justify <, right-justify > or center ^ a string in the given space.

    - We can also format integers as binary, hexadecimal, etc. and floats can be rounded or displayed in the exponent 
    format. There are tons of formatting you can use. Visit here for all the string formatting available with the format() method.
    
    Google Translate
    
    - Phương thức format() có thể có các đặc tả định dạng tùy chọn. Chúng được phân tách khỏi tên trường bằng dấu hai 
    chấm. Ví dụ, chúng ta có thể căn trái <, right-justify> hoặc căn giữa ^ một chuỗi trong không gian đã cho.

    - Chúng tôi cũng có thể định dạng số nguyên dưới dạng nhị phân, thập lục phân, v.v. và số thực có thể được làm tròn 
    hoặc hiển thị ở định dạng số mũ. Có rất nhiều định dạng bạn có thể sử dụng. Truy cập vào đây để biết tất cả các 
    định dạng chuỗi có sẵn với phương thức format().
"""

# Example

# formatting integers
print(
    "Binary representation of {0} is {0:b}".format(12)
)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# formatting floats

print(
    "Exponent representation: {0:e}".format(1566.345)
)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)

# string alignment

print(
    "|{:<10}|{:^10}|{:>10}|".format('butter', 'bread', 'ham')
)

print(
    '============================================================================================================The'
    ' End=========================================================================================================='
)


"""
    Common Python String Methods - Các Method cơ bản của String
    
    - There are numerous methods available with the string object. The format() method that we mentioned above is one of 
    them. Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc. Here is a 
    complete list of all the built-in methods to work with strings in Python.
    Source: 
    - https://www.programiz.com/python-programming/methods/string
    
    Google Translate
    - Có rất nhiều phương thức có sẵn với đối tượng chuỗi. Phương thức format() mà chúng tôi đã đề cập ở trên là một 
    trong số chúng. Một số phương thức thường được sử dụng là Lower(), upper(), join(), split(), find(), 
    Replace(), vv... Dưới đây là danh sách đầy đủ của tất cả các phương thức tích hợp để làm việc với chuỗi trong 
    Python.
    Source: 
    - https://www.programiz.com/python-programming/methods/string
"""

# Example

print(
    f"Nguyễn Đức Hoàng".upper()
)
