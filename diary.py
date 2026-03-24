class Diary:
    """Diary class"""
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1
    
    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return "\n".join(self.entries)

class DiaryPersistence:
    """Diary presistence"""

    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, "w") as f:
            f.write("\n".join(diary.entries))

    @staticmethod
    def load_from_file(filename):
        diary = Diary()
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                diary.entries.append(line.strip())
                diary.count += 1
        return diary

class DiaryStatistics:
    """Diary statistics"""
    def print_statistics(diary):
        print(f"Entries count: {len(diary.entries)}")




if __name__ == "__main__":

 

# Loome Diary objekti (ainult andmed + äriloogika)

    diary = Diary()

 

diary.add_entry("Täna oli ilus ilm.")

diary.add_entry("Õppisin programmeerimist.")

diary.add_entry("SRP on tegelikult väga loogiline.")

 

print("---- DIARY SISU ----")

print(diary)

print()




# Statistika (kasutame staticmethod'e)

print("---- STATISTIKA ----")

DiaryStatistics.print_statistics(diary)

print()




# Salvestame faili (EI loo Persistence objekti)

filename = "diary.txt"

DiaryPersistence.save_to_file(diary, filename)

 

print(f"Salvestatud faili: {filename}")

print()




# Laeme uuesti failist

loaded_diary = DiaryPersistence.load_from_file(filename)

 

print("---- FAILIST LAETUD ----")

print(loaded_diary)

print()




# Kontrollime, kas loendur töötab edasi

loaded_diary.add_entry("See lisati pärast laadimist.")

 

print("---- PÄRAST UUT LISAMIST ----")

print(loaded_diary)
