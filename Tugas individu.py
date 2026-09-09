class PersonalData:
    def __init__(self, name, kelas, nim, campus, faculty, department):
        self.name = name
        self.kelas = kelas
        self.nim = nim
        self.campus = campus
        self.faculty = faculty
        self.department = department
    

# Membuat object
data = PersonalData(
    "Muhammad Avin Nugraha",
    "2025D",
    "25091397128",
    "Universitas Negeri Surabaya",
    "Fakultas Vokasi",
    "Manajemen Informatika"
)

# Menampilkan data
print("=== PERSONAL DATA ===")
print("Name       :", data.name)
print("Class      :", data.kelas)
print("NIM        :", data.nim)
print("Kampus     :", data.department)
print("Fakultas   :", data.faculty)
print("Prodi      :", data.campus)