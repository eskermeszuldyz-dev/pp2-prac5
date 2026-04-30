import re
#1
print("=== Exercise 1: 'a' followed by 0 or more 'b's ===")
pattern1 = r"ab*"
tests1 = ["a", "ab", "abb", "b", "ac"]
for t in tests1:
    print(t, "->", bool(re.fullmatch(pattern1, t)))
#2
print("\n=== Exercise 2: 'a' followed by 2-3 'b's ===")
pattern2 = r"ab{2,3}"
tests2 = ["ab", "abb", "abbb", "abbbb"]
for t in tests2:
    print(t, "->", bool(re.fullmatch(pattern2, t)))
#3
print("\n=== Exercise 3: lowercase sequences joined with underscore ===")
text3 = "hello_world test_value invalid-Test"
pattern3 = r"\b[a-z]+_[a-z]+\b"
print(re.findall(pattern3, text3))
#4
print("\n=== Exercise 4: one uppercase followed by lowercase letters ===")
text4 = "Hello World Test ABC example"
pattern4 = r"\b[A-Z][a-z]+\b"
print(re.findall(pattern4, text4))
#5
print("\n=== Exercise 5: 'a' followed by anything, ending in 'b' ===")
pattern5 = r"a.*b"
tests5 = ["ab", "acb", "axyzb", "a123b", "ac"]
for t in tests5:
    print(t, "->", bool(re.fullmatch(pattern5, t)))
#6
print("\n=== Exercise 6: replace space, comma, or dot with colon ===")
text6 = "Hello, world. Python is fun"
pattern6 = r"[ ,.]"
result6 = re.sub(pattern6, ":", text6)
print(result6)
#7
print("\n=== Exercise 7: snake_case to camelCase ===")
def snake_to_camel(s):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)

text7 = "hello_world_test"
print(snake_to_camel(text7))
#8
print("\n=== Exercise 8: split string at uppercase letters ===")
text8 = "HelloWorldTest"
result8 = re.split(r"(?=[A-Z])", text8)
print(result8)
#9
print("\n=== Exercise 9: insert spaces before capital letters ===")
text9 = "HelloWorldTest"
result9 = re.sub(r"([A-Z])", r" \1", text9).strip()
print(result9)
#10
print("\n=== Exercise 10: camel Case to snake_case ===")
def camel_to_snake(s):
    return re.sub(r"([A-Z])", r"_\1", s).lower().lstrip("_")

text10 = "helloWorldTest"
print(camel_to_snake(text10))