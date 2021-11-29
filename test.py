try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

print(ord('c') -ord('a'))
print(chr(ord('z') - 2))
print(3 * 'abc' + 'xyz')