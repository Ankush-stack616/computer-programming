#  Find elements in one tuple that are not in another.

tuple1 = tuple(input("Enter elements of the first tuple separated by spaces: ").split())
tuple2 = tuple(input("Enter elements of the second tuple separated by spaces: ").split())

difference = set(tuple1).difference(tuple2)
print("Elements in first tuple but not in second:", tuple(difference))
