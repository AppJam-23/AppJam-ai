import random
import csv
import names

# Generate random float with one decimal point between min_val and max_val
def random_float(min_val, max_val):
    return round(random.uniform(min_val, max_val), 1)

with open("generated_data.csv", "w", encoding="utf-8") as csvfile:
    fieldnames = ["id", "Name", "Age", "Gender", "Temperature", "Step", "Heart", "Sleep", "Suspected", "Patient"]
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    for i in range(100):
        age = random.randint(14, 17)
        name = names.get_full_name()
        gender = random.randint(0, 1)
        temperature = random_float(35.0, 39.0)
        step = random.randint(5000, 15000)
        heart = random.randint(60, 100)
        sleep = random.randint(360, 540)
        status = random.choices([0, 1, 2], weights=[70, 20, 10], k=1)[0]
        suspected = 1 if status == 1 else 0
        patient = 1 if status == 2 else 0

        csv_writer.writerow({
            "id": i + 1,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Temperature": temperature,
            "Step": step,
            "Heart": heart,
            "Sleep": sleep,
            "Suspected": suspected,
            "Patient": patient
        })
