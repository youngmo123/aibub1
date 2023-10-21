numbers = [
    ("abc", 2),
    ("def", 3),
    ("ghi", 4),
    ("jkl", 5),
    ("mno", 6),
    ("pqrs", 7),
    ("tuv", 8),
    ("wxyz", 9)
]
ch2num_map = {c: v for k, v in numbers for c in k}
s = input("문자열을 입력하시오.")
result = "".join(str(ch2num_map.get(v,v)) for v in s.lower())
print(result)