# Tax Calculator - 8% Norte, 16, resto del pais.
print("Input subtotal: ")
subtotal = float(input())

if subtotal > 0:
    print("${:.2f} Mxn.".format(subtotal * 1.08))
