db_password = "MyPassword123"   # ❌ తప్పు 1: సీక్రెట్ పాస్‌వర్డ్ బయట పెట్టారు (Vulnerability)
unused_bonus = 5000             # ❌ తప్పు 2: ఈ వేరియబుల్ క్రియేట్ చేశారు కానీ ఎక్కడా వాడలేదు (Code Smell)

def check_age(age):
    if age < 0:
        return 0                # ❌ తప్పు 3: మైనస్ వయస్సు ఉండదు, లాజిక్ తప్పు (Bug)