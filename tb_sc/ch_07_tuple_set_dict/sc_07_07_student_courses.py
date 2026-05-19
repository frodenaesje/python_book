# file: sc_07_07_student_courses.py
# dict i dict - eksempel på nøstet datastruktur

# Studentdatabase: Studenten identifiseres med en student_id; - Hver student har et navn og flere fagkarakterer
# Struktur:
#    {student_id: {"name": string,
#     "courses": {course: grade, ...}}}
grades = {
    1001: {                                    # student_id 1001
        "name": "Paul Barnes",                 # Elevens fulle navn  
        "courses": {"math": 8, "physics": 7, "c++": 3}  # dict over fag og karakterer
    },
    1031: {                                    
        "name": "Bill Shankley",
        "courses": {"math": 6, "c++": 6}       
    },
    1011: {                                    
        "name": "Jane Jillingham", 
        "courses": {"physics": 2, "math": 5}   
    },
    1012: {                                    
        "name": "Bill Gates",
        "courses": {"java": 10, "c++": 7}      
    },
    1019: {                                    
        "name": "Jack The Ripper",
        "courses": {"math": 8, "physics": 7}   
    },
    1090: {                                   
        "name": "Don Henley",
        "courses": {"physics": 10, "c++": 8}
    }
}


"""
Studentdatabasen demonstrerer tre nivåer av dictionaries:

NIVÅ 1: student_id'er, nøkkel 1001, 1031, osv.
    - Hver representerer en unik elev

NIVÅ 2: Elevopplysninger, nøkler "name" og "courses" 
    - Hver elev har nøyaktig to attributter:
      * "name": en enkel streng med elevens navn
      * "courses": enda en dict som inneholder deres karakterer

NIVÅ 3: Individuelle fagkarakterer, nøkler "math", "physics", "c++", "java" etc
    - Det innerste nivået inneholder fag-karakter par
    - Karakterer er heltall fra 0-10
    - Ikke alle elever tar de samme fagene

Hente ut verdier:
1. Hent elevens navn:        grades[student_id]["name"]
2. Hent spesifikk karakter:  grades[student_id]["courses"]["subject"]
3. Hent alle fag:            grades[student_id]["courses"]
4. Sikker tilgang:           grades[student_id]["courses"].get("subject", 0)

"""

print("=== Aksessere data  ===")
print(f"Elev 1001 sitt navn: {grades[1001]['name']}")
print(f"Elev 1001 sin matematikk-karakter: {grades[1001]['courses']['math']}")
print(f"Alle fag for elev 1031: {grades[1031]['courses']}")

print("\n=== Mer sikker tilgang med get() metoden ===")
# Bruk get() for å unngå KeyError hvis elev eller fag ikke finnes
student_1001_physics = grades[1001]["courses"].get("physics", "Ikke tatt")
student_1012_physics = grades[1012]["courses"].get("physics", "Ikke tatt")
print(f"Elev 1001 fysikk-karakter: {student_1001_physics}")
print(f"Elev 1012 fysikk-karakter: {student_1012_physics}")

def get_grades(item):
    """Beregn summen av fysikk- og c++-karakterer for sortering
    Args:
        item: En tuple av (student_id, student_info_dict) fra grades.items()
    Returnerer:
        int: Sum av fysikk- og c++-karakterer (0 hvis fag ikke tatt)
    """
    courses = item[1]["courses"]  # Hent dicten over fag fra elevinfo
    return courses.get("physics", 0) + courses.get("c++", 0)

print("\n=== SORTERING ETTER BEREGNEDE VERDIER ===")
# Sorter elever etter deres fysikk + c++-karakterer (høyeste først)

# Dette gjør sorted() "bak kulissene", den gjør om en ikke-indekserbar view til en liste
# grades_list = list(grades.items()) # denne brukes mot get_grades()


# argumentene til get_grades er et tuple (student_id, student_info_dict)
sorted_list = sorted(grades.items(), key=get_grades, reverse=True)
sorted_dict = dict(sorted_list)

# Vis sorterte resultater
for student_id, info in sorted_dict.items():
    print(f"{student_id}: {info['name']}, Courses: {info['courses']}")

# Eksempel på å iterere gjennom hele strukturen
print("\n=== FULLSTENDIG DATAOVERSIKT ===")
for student_id, student_info in grades.items(): # student_info er en dict, nivå 2
    print(f"\nElev {student_id}: {student_info['name']}") # data fra nivå 2, en streng
    for course, grade in student_info["courses"].items(): # dict'et på nivå 3, tuple med nøkkel og verdi
        print(f"  {course}: {grade}")                     # som er (streng, int) par, kurs og karakter
