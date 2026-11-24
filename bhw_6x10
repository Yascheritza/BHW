import hashlib

mapping = "1234567890"


def gc(group: int, index: int, attempt: int = 1) -> str:
    base = f"{group}:{index}:{attempt}".encode()
    h = hashlib.sha256(base).hexdigest()
    digits = []
    for i in range(6):
        nibble = int(h[i], 16)
        digits.append(nibble % 10)

    letters = "".join(mapping[d] for d in digits)
    code = f"1{letters[0]}2{letters[1]}3{letters[2]}4{letters[3]}5{letters[4]}6{letters[5]}"
    return code


def printt(code: str):
    raw_digits = [int(code[i]) for i in (1, 3, 5, 7, 9, 11)]
    rei = []
    for d in raw_digits:
        rei.append(10 - d)
    for i, val in enumerate(rei, start=1):
        print(f"{i}: {val}")


print("Введите номер вашей группы:")
g = int(input())
print("Введите ваш порядковый номер в группе:")
n = int(input())
s1 = gc(g, n)
print()
printt(s1)
