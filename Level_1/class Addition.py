class Addition:
    def __call__(self, *args, **kwargs):
        digits = []
        for i in range(len(args)):
            if isinstance(args[i], int):
                digits.append(args[i])
            if isinstance(args[i], float):
                digits.append(args[i])
        print(f"Сумма переданных значений = {sum(digits)}")
