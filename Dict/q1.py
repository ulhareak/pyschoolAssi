"""
he dictionary data structure consists of key-value data pair.

Examples

>>>a = {} # empty dictionary
>>>type(a)
< type 'dict' >
>>>book = {"Author":"Lewis Carroll"}
>>>book["Title"] = "Alice's Adventures in Wonderland"
>>>book
{'Title': "Alice's Adventures in Wonderland", 'Author': 'Lewis Carroll'}
>>>contactinfo["Tom"]
{'Email':'tom@gmail.com', 'Phone':61234567}
>>>contactinfo["Sally"]
{'Email':'sally@hotmail.com', 'Phone':67654321}
"""
# Initialize dictionary "contactinfo" with the values
# as shown in above examples. Hint: The key is a string
# literal while the value is a dictionary type.
contactinfo ={
    "Tom": {'Email': 'tom@gmail.com', 'Phone': 61234567},
    "Sally":{'Email': 'sally@hotmail.com', 'Phone': 67654321}
}
print(contactinfo["Sally"])
