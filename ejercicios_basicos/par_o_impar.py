def par_o_impar(num):
    if num %2 ==0:
        return "par"
    else:
        return "impar"

for n in range(1,16):
    print(n, "es",par_o_impar(n))

