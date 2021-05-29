def from_string_to_list(text, container):
    for i in text.split():
        container.append(i)


a = [1, 2, 3]
from_string_to_list("s s s s", a)
print(*a)