# сравнить имеющиеся блезни с противопоказаниями новых лекарств (incompatibility)
# сравнить старые лекарства с противопоказаниями новых (в той же incompatibility)

import database
# создаем экземпляр класса для работы с БД
db = database.Database("Med", "postgres", 12345, "localhost", 5432)

# вводим данные о пациенте и новых лекарствах
patient_id = int(input())
count_of_medicine = int(input())
list_of_med = []
for i in range(count_of_medicine):
    list_of_med.append(input())

'''
anamnez = {"disease": ["disease_1", "disease_2"], "medicine": {"med_1": ["disease_3", "med_3"], "med_2": ["med_3"]}}
medicine = {"med_3": ["disease_1", "med_2"], "med_4": ["disease_5", "med_5"]}
'''
# обращение к БД за анемнезом и данными о лекарствах
anamnez = db.get_ananez(patient_id)
age = db.get_patient_age(patient_id)
medicine = db.get_medicine(list_of_med)

# Преобразование в нужный вид
list_of_incompatibility = []
list_of_medicine = []
list_of_disease = anamnez.get("disease")
anamnez_medicine = anamnez.get("medicine")
for i in anamnez_medicine:
    list_of_medicine.append(i)
    list_of_incompatibility.extend(anamnez_medicine.get(i))

#print(list_of_incompatibility)
# проверка несовместимостей
for med in medicine:
    #print(med)
    #print(medicine.get(med))
    incompatibility = medicine.get(med)
    incompatibility.append(med)
    for i in incompatibility:
        if i == "Пожилой":
            if age > 65:
                print("Warning : incopatible age")
        if i == "Дети":
            if age < 18:
                print("Warning : incopatible age")
        if i in list_of_disease:
            print("Warning (disease) :", med, i)  # новое лекарство несовместимо с существующей болезнью
            # TODO incopatible_disease.append(i)
        if i in list_of_medicine:
            print("Warning (medicine) :", med, i)  # новое лекарство несовместимо со старым

# сортировка шкал частоты и серьёзности
list_of_side_effects = db.get_side_effects(list_of_med)
print(sorted(list_of_side_effects, key=lambda elem: (-elem[2], -elem[1])))
