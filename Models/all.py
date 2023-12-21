from Models.Model import Model

class all(Model):

    def get1(self):
        date = input("Введите дату для вывода количества вызовов ")
        return super().get1(date)

    def get2(self):
        Diagnosis = input("Введите диагноз чтобы узнать информацию о больных ")
        return super().get2(Diagnosis)

    def get3(self):
        Name_Medicine = input("Введите название лекарства чтобы узнать информацию о побочных действиях ")
        return super().get3(Name_Medicine)

    def get4(self):
        Name_Medicine = input("Введите название лекарства для добавления ")
        How_to_Use = input("Обьясните как использовать ")
        Drug_Actions = input("Введите показания для лечения ")
        Side_Effects = input("Введите побочные эффекты ")
        return super().get4(Name_Medicine, How_to_Use, Drug_Actions, Side_Effects)