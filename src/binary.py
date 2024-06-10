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
    for i in range(0, 1000):
        x = 1000 - i
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

def add_bin_n(bin_a, bin_b, den = False):
    len_bin_a = len(bin_a)
    len_bin_b = len(bin_b)
    lis_bin_a = list(str(bin_a))
    lis_bin_b = list(str(bin_b))
    out = ""
    smallest = len_bin_a if len_bin_b > len_bin_a else len_bin_b
    small = lis_bin_a if len_bin_b > len_bin_a else lis_bin_b
    big = lis_bin_b if len_bin_b > len_bin_a else lis_bin_a
    carry = False
    if len(small) == len(big):
        for n in range(smallest):
            n += 1
            try:
                if small[-n] == "0" and big[-n] == "0" and carry:
                    toadd = "1"
                    carry = False
                elif small[-n] == "0" and big[-n] == "0":
                    toadd = "0"
                elif ((small[-n] == "1" and big[-n] == "0") or (small[-n] == "0" and big[-n] == "1")) and carry:
                    toadd = "0"
                    carry = True
                elif (small[-n] == "1" and big[-n] == "0") or (small[-n] == "0" and big[-n] == "1"):
                    toadd = "1"
                elif (small[-n] == "1" and big[-n] == "1")  and carry:
                    toadd = "1"
                elif (small[-n] == "1" and big[-n] == "1"):
                    toadd = "0"
                    carry = True
            except IndexError:
                pass
            out += toadd
        if carry:
            out += "1"
        output = out[::-1]
        if den:
            _out = bin2den(output)
            return _out
        else:
            return output
    else:
        n_to_add = len(big) - len(small)
        toadd = ""
        for n in range(n_to_add):
            toadd += "0"
        small.insert(0, toadd)
        for n in range(len(big)):
            n += 1
            try:
                if small[-n] == "0" and big[-n] == "0" and carry:
                    toadd = "1"
                    carry = False
                elif small[-n] == "0" and big[-n] == "0":
                    toadd = "0"
                elif ((small[-n] == "1" and big[-n] == "0") or (small[-n] == "0" and big[-n] == "1")) and carry:
                    toadd = "0"
                    carry = True
                elif (small[-n] == "1" and big[-n] == "0") or (small[-n] == "0" and big[-n] == "1"):
                    toadd = "1"
                elif (small[-n] == "1" and big[-n] == "1")  and carry:
                    toadd = "1"
                elif (small[-n] == "1" and big[-n] == "1"):
                    toadd = "0"
                    carry = True
            except IndexError:
                pass
            out += toadd
        if carry:
            out += "1"
        output = out[::-1]
        if den:
            _out = bin2den(output)
            return _out
        else:
            return output
