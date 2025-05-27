
"""
filename = r'C:\Users\ayan.reyhanov\Documents\nosenose.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
"""
try:
    number_1 = int(input("Dime un número:\n"))
except TypeError:
    print("Pon un número, por favor.")

