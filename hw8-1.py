class Date:
    def __init__(self, day):
        self.day = str(day)

    @classmethod
    def extract(cls, day):
        new_date = []

        for i in day.split():
            if i != '-': new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 9999:
                    return f'дата верна'
                else:
                    return f'указан неверный год год'
            else:
                return f'указан неверный месяц'
        else:
            return f'указан неверный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day)}'


today = Date('11 - 8 - 2020')
print(today)
print(Date.valid(40, 1, 2123))
print(Date.valid(1, 12, 9999))