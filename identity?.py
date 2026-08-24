# Arrays about my Personal Information, over-engineered but whatever lol (everything self explanatory, i guess)
Name     = ["Muhammad", "Azzam"]
ID       = ["2605060028"]
PDOB     = ["Magelang", "2007-07-06"]
Address  = ["Payaman", "Kec. Secang", "Kab. Magelang", "Jawa Tengah"]
Sex      = ["COwOk"]
Hobby    = ["Computer?", "Linux (BTW)", "Watching Anime (Sometimes but not really)"]

# For sentences that require a separator
c=", "
# For the regular sentences
nc=" "
# Check the NIM (String) is a Number with exactly 10 digits + Basic error handling
if not ID[0].isdigit() or len(ID[0]) != 10:
    raise ValueError("The NIM is not a valid integer with exactly 10 digits!")

# Join them and print my identities in indonesian*
print("\t\u00B0Let me introduce my self\u00B0")                 # the "\t" is for something and the "\u" is something-something unicode
print(f"Nama                 : {nc.join(Name)}")
print(f"Nama Panggilan       : {Name[-1]}")
print(f"NIM                  : {ID[0]}")
print(f"Tempat Tanggal Lahir : {c.join(PDOB)}")
print(f"Alamat               : {c.join(Address)}")
print(f"Jenis Kelamin        : {Sex[0]}")
print(f"Hobi                 : {c.join(Hobby)}")

# Just Reusing my code pretty much sorry, no regret :3
