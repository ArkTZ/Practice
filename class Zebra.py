class Zebra:
    def __init__(self,count=0):
        self.count = count

    def which_stripe(self):
        if self.count % 2 == 0:

            print('Полоска белая')
            self.count += 1

        else:
            self.count += 1
            print("Полоска черная")