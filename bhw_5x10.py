import hashlib

mapping = "1234567890"

def gc(group: int, index: int, attempt: int = 0) -> str:

    base = f"{group}:{index}:{attempt}".encode()
    h = hashlib.sha256(base).hexdigest()
    digits = []
    for i in range(5):
        nibble = int(h[i], 16)
        digits.append(nibble % 10)

    letters = "".join(mapping[d] for d in digits)
    code = f"1{letters[0]}2{letters[1]}3{letters[2]}4{letters[3]}5{letters[4]}"
    return code

def printt(code: str):
    raw_digits = [int(code[i]) for i in (1, 3, 5, 7, 9)]
    rei= [(10 if d == 0 else d + 1) for d in raw_digits]

    for i, val in enumerate(rei, start=1):
        print(f"{i}: {val}")



print("Введите номер вашей группы:")
g = int(input())
print("Введите ваш порядковый номер в группе:")
n = int(input())
s1 = gc(g, n)
print()
printt(s1)
