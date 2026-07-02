import pickle
import datetime

FILENAME = "FUSION_MANIA.dat"

# --------------------------------------------------------------
# INTRODUCTION
# --------------------------------------------------------------
def show_intro():
    print("=" * 70)
    print(" WELCOME TO  FUSION MANIA — THE GRAND 4-DAY SCHOOL FEST ")
    print("=" * 70)
    print("""
A celebration of creativity, culture, and collaboration!

Organized by:
#President: Aarav Sharma
#Vice President: Meera Nair
#Event Coordinator: Rohan Mehta
#Technical Head: Tanya Kapoor
#Cultural Lead: Ishita Rao
#Hospitality & Registration: Arjun Singh

Registration closes 15 days before the fest.
All participants must attend their respective auditions.
""")
    print("-" * 70)


# --------------------------------------------------------------
# INSERT / APPEND RECORD
# --------------------------------------------------------------
def insert_or_append():
    try:
        with open(FILENAME, "ab") as f:
            participant = {}

            print("\n--- Participant Registration ---")
            participant["id"] = int(input("Enter Participant ID: "))
            participant["name"] = input("Enter Name: ")
            participant["class"] = input("Enter Class & Section: ")

            # CLUB CHOICES
            print("\nChoose a Club to Join:")
            print("1. Cultural Club")
            print("2. Tech Innovators")
            print("3. Literary League")
            print("4. Eco Warriors")
            print("5. Sports Squad")
            print("6. Discipline & Protocol Corps")
            print("7. Event Management & Operations Squad")

            ch = input("Enter your choice (1-7): ").strip()
            while ch not in ("1", "2", "3", "4", "5", "6", "7"):
                ch = input("Invalid choice! Enter again (1-7): ").strip()

            clubs = {
                "1": "Cultural Club",
                "2": "Tech Innovators",
                "3": "Literary League",
                "4": "Eco Warriors",
                "5": "Sports Squad",
                "6": "Discipline & Protocol Corps",
                "7": "Event Management & Operations Squad"
            }
            participant["club"] = clubs[ch]

            # CLUB-SPECIFIC ROLES
            print("\n Choose Your Role in the Club:")
            

            if ch == "1":  # Cultural Club
                print("1. Dancer")
                print("2. Actor / Drama Artist")
                print("3. Singer / Musician")
                print("4. Artist (Props/Posters)")
                roles = { "1": "Dancer", "2": "Actor", "3": "Singer/Musician", "4": "Artist" }

            elif ch == "2":  # Tech Innovators
                print("1. Coder")
                print("2. Robotics Engineer")
                print("3. AI Model Designer")
                print("4. Technical Support")
                roles = { "1": "Coder", "2": "Robotics Engineer", "3": "AI Model Designer", "4": "Technical Support" }

            elif ch == "3":  # Literary League
                print("1. Poet")
                print("2. Debater")
                print("3. Writer")
                print("4. Anchor")
                roles = { "1": "Poet", "2": "Debater", "3": "Writer", "4": "Anchor" }

            elif ch == "4":  # Eco Warriors
                print("1. Researcher")
                print("2. Plantation Lead")
                print("3. Recycling Coordinator")
                print("4. Awareness Volunteer")
                roles = { "1": "Researcher", "2": "Plantation Lead", "3": "Recycling Coordinator", "4": "Awareness Volunteer" }

            elif ch == "5":  # Sports Squad
                print("1. Athlete / Player")
                print("2. Coach Assistant")
                print("3. Team Manager")
                print("4. Equipment & Ground Support")
                print("5. Organizer – Athlete Care (Visiting Schools)")
                roles = { "1": "Athlete", "2": "Coach Assistant", "3": "Team Manager", "4": "Equipment Support", "5": "Organizer – Athlete Care" }

            elif ch == "6":  # Discipline & Protocol
                print("1. Protocol Officer")
                print("2. Discipline Marshal")
                print("3. Crowd Flow Coordinator")
                print("4. Safety & Order Lead")
                print("5. VIP Assistance Team")
                roles = { "1": "Protocol Officer", "2": "Discipline Marshal", "3": "Crowd Flow Coordinator", "4": "Safety & Order Lead", "5": "VIP Assistance Team" }

            elif ch == "7":  # Event Management
                print("1. Stage Manager")
                print("2. Backstage Coordinator")
                print("3. Logistics Lead")
                print("4. Hospitality & Guest Support")
                print("5. Technical Flow Assistant")
                roles = { "1": "Stage Manager", "2": "Backstage Coordinator", "3": "Logistics Lead", "4": "Hospitality & Guest Support", "5": "Technical Flow Assistant" }

            role_choice = input("Enter role choice: ").strip()
            while role_choice not in roles:
                role_choice = input("Invalid! Enter again: ").strip()
            participant["department"] = roles[role_choice]

            audition = input("Audition Required? after this step your fee will be deduced directly from your account. (Y/N): ").strip().lower()
            if audition == "y":
                participant["audition"] = True
                
                participant["fee_paid"] = 200
                
            else:
                participant["audition"] = False
                participant["fee_paid"] = 0

            participant["reg_date"] = datetime.date.today().strftime("%d-%m-%Y")
            pickle.dump(participant, f)
            print("registration date is ",participant["reg_date"])

            if participant["fee_paid"] > 0:
                print("\nRegistration Successful!\n")
            else:
                print("\nYour fest pass is ON HOLD. Payment required after audition approval.\n")

    except Exception as e:
        print("Error:", e)


# -----------------------------------------------------
# DISPLAY ALL RECORDS
# -----------------------------------------------------
def display():
    try:
        with open(FILENAME, "rb") as f:
            print("\n========= ALL PARTICIPANTS =========\n")
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break

                print(f"ID: {data.get('id')} | Name: {data.get('name')} | Class: {data.get('class')}")
                print(f"Club: {data.get('club')} | Role: {data.get('department')}")
                print(f"Audition: {'Yes' if data.get('audition') else 'No'}")
                print(f"Fee Paid: ₹{data.get('fee_paid')} | Reg Date: {data.get('reg_date')}")
                print("-" * 55)

        print("\n End of list.\n")

    except FileNotFoundError:
        print(" No data file found.\n")


# -----------------------------------------------------
# SEARCH
# -----------------------------------------------------
def search():
    try:
        print("\nSearch By:")
        print("1. ID")
        print("2. Name")
        print("3. Class")
        print("4. Club--Enter full name of the club")

        ch = input("Enter choice: ").strip()
        value = input("Enter search value: ").strip()
        found = False
        
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break

                if (ch == "1" and str(data["id"]) == value) or \
                   (ch == "2" and data["name"].lower() == value.lower()) or \
                   (ch == "3" and data["class"].lower() == value.lower()) or \
                   (ch == "4" and data["club"].lower() == value.lower()):
                    print("\nRecord Found:")
                    print(data)
                    found = True

        if not found:
            print("No matching record found.\n")

    except FileNotFoundError:
        print("Data file not found.\n")


# -----------------------------------------------------
# UPDATE (Password Protected)
# -----------------------------------------------------
def update():
    print("\nCLUB PRESIDENT ACCESS ONLY ")
    password = input("Enter President Password: ")

    if password != "president123":
        print(" Incorrect Password. Access Denied.\n")
        return

    print("Access Granted \n")
    print("\nUpdate By:")
    print("1. ID")
    print("2. Name")
    ch = input("Enter choice: ").strip()
    
    value = input("Enter value: ").strip().lower()  
    temp = []
    found = False

    try:
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break

                imatch = (ch == "1" and str(data["id"]).lower() == value) or \
                         (ch == "2" and data["name"].lower() == value)

                if imatch:
                    found = True
                    print("\nWhat do you want to update?")
                    print("1. Name")
                    print("2. Class")
                    print("3. Department / Role")
                    print("4. Club")
                    print("5. Audition")
                    print("6. Fee Paid")

                    opt = input("Choose field number: ")

                    # -------------------------
                    # Update NAME
                    # -------------------------
                    if opt == "1":
                        data["name"] = input("Enter new name: ")

                    # -------------------------
                    # Update CLASS
                    # -------------------------
                    elif opt == "2":
                        data["class"] = input("Enter new class: ")

                    # -------------------------
                    # Update ROLE (department) – SIMPLE PATTERN
                    # -------------------------
                    elif opt == "3":
                        club = data["club"]
                        print("\nChoose New Role for", club)

                        if club == "Cultural Club":
                            print("1. Dancer\n2. Actor\n3. Singer/Musician\n4. Artist")
                            roles = {"1":"Dancer","2":"Actor","3":"Singer/Musician","4":"Artist"}

                        elif club == "Tech Innovators":
                            print("1. Coder\n2. Robotics Engineer\n3. AI Model Designer\n4. Technical Support")
                            roles = {"1":"Coder","2":"Robotics Engineer","3":"AI Model Designer","4":"Technical Support"}

                        elif club == "Literary League":
                            print("1. Poet\n2. Debater\n3. Writer\n4. Anchor")
                            roles = {"1":"Poet","2":"Debater","3":"Writer","4":"Anchor"}

                        elif club == "Eco Warriors":
                            print("1. Researcher\n2. Plantation Lead\n3. Recycling Coordinator\n4. Awareness Volunteer")
                            roles = {"1":"Researcher","2":"Plantation Lead","3":"Recycling Coordinator","4":"Awareness Volunteer"}

                        elif club == "Sports Squad":
                            print("1. Athlete\n2. Coach Assistant\n3. Team Manager\n4. Equipment Support\n5. Organizer – Athlete Care")
                            roles = {"1":"Athlete","2":"Coach Assistant","3":"Team Manager","4":"Equipment Support","5":"Organizer – Athlete Care"}

                        elif club == "Discipline & Protocol Corps":
                            print("1. Protocol Officer\n2. Discipline Marshal\n3. Crowd Flow Coordinator\n4. Safety & Order Lead\n5. VIP Assistance Team")
                            roles = {"1":"Protocol Officer","2":"Discipline Marshal","3":"Crowd Flow Coordinator","4":"Safety & Order Lead","5":"VIP Assistance Team"}

                        elif club == "Event Management & Operations Squad":
                            print("1. Stage Manager\n2. Backstage Coordinator\n3. Logistics Lead\n4. Hospitality & Guest Support\n5. Technical Flow Assistant")
                            roles = {"1":"Stage Manager","2":"Backstage Coordinator","3":"Logistics Lead","4":"Hospitality & Guest Support","5":"Technical Flow Assistant"}

                        role_choice = input("Enter new role number: ").strip()
                        while role_choice not in roles:
                            role_choice = input("Invalid! Enter again: ").strip()
                        data["department"] = roles[role_choice]

                    # -------------------------
                    # UPDATE CLUB + SHOW ROLES (NEW SIMPLE FEATURE)
                    # -------------------------
                    elif opt == "4":
                        print("\nChoose New Club:")
                        print("1. Cultural Club")
                        print("2. Tech Innovators")
                        print("3. Literary League")
                        print("4. Eco Warriors")
                        print("5. Sports Squad")
                        print("6. Discipline & Protocol Corps")
                        print("7. Event Management & Operations Squad")

                        clubs = {
                            "1":"Cultural Club",
                            "2":"Tech Innovators",
                            "3":"Literary League",
                            "4":"Eco Warriors",
                            "5":"Sports Squad",
                            "6":"Discipline & Protocol Corps",
                            "7":"Event Management & Operations Squad"
                        }

                        new_club = input("Enter club number: ").strip()
                        while new_club not in clubs:
                            new_club = input("Invalid! Enter again: ").strip()
                        
                        data["club"] = clubs[new_club]

                        # Now role must be chosen from NEW club
                        print("\nChoose New Role for", data["club"])

                        if data["club"] == "Cultural Club":
                            print("1. Dancer\n2. Actor\n3. Singer/Musician\n4. Artist")
                            roles = {"1":"Dancer","2":"Actor","3":"Singer/Musician","4":"Artist"}

                        elif data["club"] == "Tech Innovators":
                            print("1. Coder\n2. Robotics Engineer\n3. AI Model Designer\n4. Technical Support")
                            roles = {"1":"Coder","2":"Robotics Engineer","3":"AI Model Designer","4":"Technical Support"}

                        elif data["club"] == "Literary League":
                            print("1. Poet\n2. Debater\n3. Writer\n4. Anchor")
                            roles = {"1":"Poet","2":"Debater","3":"Writer","4":"Anchor"}

                        elif data["club"] == "Eco Warriors":
                            print("1. Researcher\n2. Plantation Lead\n3. Recycling Coordinator\n4. Awareness Volunteer")
                            roles = {"1":"Researcher","2":"Plantation Lead","3":"Recycling Coordinator","4":"Awareness Volunteer"}

                        elif data["club"] == "Sports Squad":
                            print("1. Athlete\n2. Coach Assistant\n3. Team Manager\n4. Equipment Support\n5. Organizer – Athlete Care")
                            roles = {"1":"Athlete","2":"Coach Assistant","3":"Team Manager","4":"Equipment Support","5":"Organizer – Athlete Care"}

                        elif data["club"] == "Discipline & Protocol Corps":
                            print("1. Protocol Officer\n2. Discipline Marshal\n3. Crowd Flow Coordinator\n4. Safety & Order Lead\n5. VIP Assistance Team")
                            roles = {"1":"Protocol Officer","2":"Discipline Marshal","3":"Crowd Flow Coordinator","4":"Safety & Order Lead","5":"VIP Assistance Team"}

                        else:
                            print("1. Stage Manager\n2. Backstage Coordinator\n3. Logistics Lead\n4. Hospitality & Guest Support\n5. Technical Flow Assistant")
                            roles = {"1":"Stage Manager","2":"Backstage Coordinator","3":"Logistics Lead","4":"Hospitality & Guest Support","5":"Technical Flow Assistant"}

                        role_choice = input("Enter new role number: ").strip()
                        while role_choice not in roles:
                            role_choice = input("Invalid! Enter again: ").strip()
                        data["department"] = roles[role_choice]

                        print("Club and Role updated successfully!")

                    # -------------------------
                    # Update Audition (auto-fee)
                    # -------------------------
                    elif opt == "5":
                        audition_input = input("Audition (Y/N): ").strip().lower()
                        data["audition"] = (audition_input == "y")

                        if data["audition"]:
                            data["fee_paid"] = 200
                            print("Audition set to YES Fee = 200.")
                        else:
                            data["fee_paid"] = 0
                            print("Audition set to NO  Fee = 0.")

                    elif opt == "6":
                        print("Fee is system-controlled. Change audition status instead.")

                temp.append(data)

        if found:
            with open(FILENAME, "wb") as f:
                for rec in temp:
                    pickle.dump(rec, f)
            print(" Record Updated Successfully\n")
        else:
            print(" Record Not Found.\n")

    except FileNotFoundError:
        print("Data file not found.\n")


# -----------------------------------------------------
# DELETE (BY ID OR NAME)
# -----------------------------------------------------
def delete():
    print("\nDelete By:")
    print("1. ID")
    print("2. Name")

    ch = input("Enter choice: ").strip()
    value = input("Enter value: ").strip()

    temp = []
    found = False

    try:
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break

                if (ch == "1" and str(data["id"]) != value) or \
                   (ch == "2" and data["name"].lower() != value.lower()):
                    temp.append(data)
                else:
                    found = True

        if found:
            with open(FILENAME, "wb") as f:
                for rec in temp:
                    pickle.dump(rec, f)
            print("Record deleted.\n")
        else:
            print("Record not found.\n")

    except FileNotFoundError:
        print("Data file not found.\n")


# -----------------------------------------------------
# SCHEDULES
# -----------------------------------------------------
def fest_schedule():
    print("\nFUSION MANIA--> 4-DAY FEST SCHEDULE ")
    print("Day 1: Opening & Cultural Show")
    print("Day 2: Tech Fair & Robotics Expo")
    print("Day 3: Literary & Eco Workshops")
    print("Day 4: Sports Tournament + Closing Ceremony\n")


def schedule_by_club(club):
    print("\n Schedule for", club)
    
    if club == "Sports Squad":
        print("Trial Match: 5 days before fest (Main Ground)")
        print("Organizer Role: Assist visiting school athletes")

    elif club == "Discipline & Protocol Corps":
        print("Briefing Session: 6 days before fest")
        print("Venue: Seminar Hall")

    elif club == "Event Management & Operations Squad":
        print("Backstage Training: 7 days before fest")
        print("Venue: Audi Stage")

    print()


# -----------------------------------------------------
# FEST PASS
# -----------------------------------------------------
def generate_pass():
    print("\nGenerate Pass By:")
    print("1. ID")
    print("2. Name")

    ch = input("Choice: ").strip()
    value = input("Enter value: ").strip()

    found = False

    try:
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break

                if (ch == "1" and str(data["id"]) == value) or \
                   (ch == "2" and data["name"].lower() == value.lower()):
                    found = True
                    print("\n*** FEST PASS ***")
                    print("=" * 40)
                    print(f"Name      : {data.get('name')}")
                    print(f"Class     : {data.get('class')}")
                    print(f"Club      : {data.get('club')}")
                    print(f"Audition  : {'Yes' if data.get('audition') else 'No'}")
                    print(f"Fee Paid  : ₹{data.get('fee_paid')}")
                    print(f"Reg Date  : {data.get('reg_date')}")
                    if data.get("fee_paid") == 0:
                        print("\nPASS ON HOLD: Payment pending or audition not cleared.")
                    print("=" * 40)

                    schedule_by_club(data.get("club"))
                    fest_schedule()
                    break

        if not found:
            print(" Not Found.\n")

    except FileNotFoundError:
        print("Data file not found.\n")


# -----------------------------------------------------
# MENU
# -----------------------------------------------------
def menu():
    show_intro()
    while True:
        print("\n============== MAIN MENU ==============")
        print("1. Insert Participant")
        print("2. Display All Records")
        print("3. Search Participant")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Generate Fest Pass")
        print("7. View Fest Schedule")
        print("8. Exit")
        print("=======================================")

        choice = input("Choice: ").strip()

        if choice == "1":
            insert_or_append()
        elif choice == "2":
            display()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            generate_pass()
        elif choice == "7":
            fest_schedule()
        elif choice == "8":
            print("Thank you for being part of Fusion Mania!")
            break
        else:
            print(" Invalid Choice!\n")


# -----------------------------------------------------
# PROGRAM START
# -----------------------------------------------------
menu()
