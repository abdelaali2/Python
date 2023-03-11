# Q12: Write a function that takes a dictionary as input and returns a
# new dictionary with the keys and values swapped (i.e., the keys
# become the values and the values become the keys).

myDictionary = {"key1": "Value1", "key2": "Value2", "key3": "Value3"}
print(f"Original Dictionary is:\n{myDictionary}")

newDect = {}


def swapDictionary(dict):
    for key, value in myDictionary.items():
        newDect[value] = key
    return newDect


print(f"After swapping:\n{swapDictionary(myDictionary)}")
