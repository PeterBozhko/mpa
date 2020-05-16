import psycopg2


class Database:
    def __init__(self, database, login, password, host, port):
        self._database = database
        self._login = login
        self._password = password
        self._host = host
        self._port = port

    def _execute(self,
                 sql_statement='SELECT "ID", "Name " FROM public."Doctor";'):  # TODO убрать стандартное значение для sql_statement
        try:
            with psycopg2.connect(database=self._database, user=self._login,
                                  password=self._password, host=self._host, port=self._port) as conn:
                with conn.cursor() as cursor:
                    try:
                        cursor.execute(sql_statement)
                        result = cursor.fetchall()
                    except psycopg2.DatabaseError as err:
                        print("Error: ", err)
                    else:
                        conn.commit()
                    return result
        except psycopg2.OperationalError as err:
            print("Error: ", err)

    def get_ananez(self, patientId):  # можно переделать на Name или ещё что-нибудь
        sql_statement = 'SELECT "ID", "Name " FROM public."Doctor";'  # TODO сделать sql_statement
        data = self._execute(sql_statement)
        # TODO обработка данных для выдачи в нужном виде
        return {"disease": ["disease_1", "disease_2"],
                "medicine": {"med_1": ["disease_3", "med_3"], "med_2": ["med_3"]}}

    def get_medicine(self, listOfMed):  # можно переделать на Name или ещё что-нибудь
        sql_statement = 'SELECT "ID", "Name " FROM public."Doctor";'  # TODO сделать sql_statement
        data = self._execute(sql_statement)
        # TODO обработка данных для выдачи в нужном виде
        return {"med_3": ["disease_1", "med_2"], "med_4": ["disease_5", "med_5"]}

    def get_side_effects(self, list_of_med):
        sql_statement = 'SELECT "ID", "Name " FROM public."Doctor";'  # TODO сделать sql_statement
        data = self._execute(sql_statement)
        # TODO обработка данных для выдачи в нужном виде
        return [["allergey", 5, 3], ["headache", 2, 2], ["stomachache", 6, 2],
                ["pain", 4, 4]]  # [[name, frequency, seriousness], [], [], []]

    def get_patient_age(self, patient_id):
        sql_statement = 'SELECT "ID", "Name " FROM public."Doctor";'  # TODO сделать sql_statement
        data = self._execute(sql_statement)
        # TODO обработка данных для выдачи в нужном виде
        return 34
