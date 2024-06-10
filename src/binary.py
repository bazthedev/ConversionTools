def bin2den(bin_n):
    bin_l = list(str(bin_n))
    bin_len = len(bin_l)
    bin_len -= 1
    numerical_val = 0
    for n in bin_l:
        if n == "1":
            numerical_val += 2**(bin_len)
        bin_len -= 1
    return numerical_val

def den2bin(den_n : int):
    odd = False
    if den_n % 2 == 1:
        odd = True
    bin_conv = ""
    for i in range(0, 100):
        x = 100 - i
        if (den_n - (2**x)) >= 0:
            den_n -= (2**x)
            bin_conv += "1"
        else:
            try:
                if bin_conv[0] == "1":
                    bin_conv += "0"
            except IndexError:
                pass
    if bin_conv == "":
        bin_conv = "0"
    if odd and bin_conv != "":
        bin_conv += "1"
    elif not odd and bin_conv != "":
        bin_conv += "0"
    return bin_conv
