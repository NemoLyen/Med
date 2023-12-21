from Configuration.Config import connection

class Model:

    def get1(self, date):
        with connection().cursor() as cursor:
            query = (f"SELECT Date_P, COUNT(*) AS Calls_Count FROM medkorp.visits "
                     f"Where Date_P = '{date}'")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get2(self, Diagnosis):
        with connection().cursor() as cursor:
            query = (f"SELECT COUNT(DISTINCT ID_Patient) AS Patients_Count "
                     f"FROM medkorp.visits WHERE Diagnosis = '{Diagnosis}'")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get3(self, Name_Medicine):
        with connection().cursor() as cursor:
            query = (f"SELECT Side_Effects "
                     f"FROM medkorp.medicines "
                     f"WHERE Name_Medicine = '{Name_Medicine}'")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get4(self, Name_Medicine, How_to_Use, Drug_Actions, Side_Effects):
        with connection().cursor() as cursor:
            query = (f"INSERT INTO medkorp.medicines (Name_Medicine, How_to_Use, Drug_Actions, Side_Effects) "
                     f"VALUES ('{Name_Medicine}', '{How_to_Use}', '{Drug_Actions}', '{Side_Effects}')")
            cursor.execute(query)
            print("Запись добавлена.")
            return cursor.fetchall()
        connection().close()