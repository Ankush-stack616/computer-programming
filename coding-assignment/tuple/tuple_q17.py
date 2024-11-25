# Duplicate a tuple n times as specified by the user.

values = tuple(input("Enter tuple elements separated by spaces: ").split())
n = int(input("Enter the number of times to duplicate the tuple: "))

duplicated_tuple = values * n
print("Duplicated Tuple:", duplicated_tuple)
