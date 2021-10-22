class CalcList(list):
    def __init__(self, seq=()):
        for ind in range(len(seq)):
            if not isinstance(seq[ind], (int, float)):
                raise TypeError('There must be integer or float type')
        super(CalcList, self).__init__(seq)

    def __dop_arith(self, other):
        if not isinstance(other, list):
            raise TypeError('Incorrect type of data. There must be the list')
        my_len = len(self)
        oth_len = len(other)
        for k in range(oth_len):
            if not isinstance(other[k], (int, float)):
                raise ArithmeticError('You can use operators "-" and "+" only with list with integer or float types')
        fir = self[:]
        sec = other[:]
        if my_len > oth_len:
            diff = my_len - oth_len
            sec += [0 for i in range(diff)]
            max_ind = my_len
        else:
            diff = oth_len - my_len
            fir += [0 for i in range(diff)]
            max_ind = oth_len
        return fir, sec, max_ind

    def comp(self, operation, other):
        if not isinstance(other, list):
            raise TypeError('Incorrect type of argument')
        for i in range(len(other)):
            if not isinstance(other[i], (int, float)):
                raise TypeError('There must be integer or float type in list')
        fir_sum, sec_sum = float(sum(self)), float(sum(other))
        return operation(fir_sum, sec_sum)

    def __neg__(self):
        dop = self[:]
        for i in range(len(self)):
            dop[i] = -self[i]
        return CalcList(dop)

    def __add__(self, other):
        fir, sec, max_ind = self.__dop_arith(other)
        for ind in range(max_ind):
            fir[ind] = fir[ind] + sec[ind]
        return CalcList(fir)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        fir, sec, max_ind = self.__dop_arith(other)
        for ind in range(max_ind):
            fir[ind] = fir[ind] - sec[ind]
        return CalcList(fir)

    def __rsub__(self, other):
        dop = -self
        return dop.__add__(other)

    def __eq__(self, other):
        return self.comp(float.__eq__, other)

    def __ne__(self, other):
        return self.comp(float.__ne__, other)

    def __lt__(self, other):
        return self.comp(float.__lt__, other)

    def __le__(self, other):
        return self.comp(float.__le__, other)

    def __gt__(self, other):
        return self.comp(float.__gt__, other)

    def __ge__(self, other):
        return self.comp(float.__ge__, other)
