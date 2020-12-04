
class Passport :
    def __init__ (self) :
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
    
        self.fields = 0
    
    def Valid (self) :
        if self.fields == 8 :
            return True
        if self.fields == 7 and self.cid == None :
            return True
        return False
        
    def setField (self, field, value) :
        if field == "byr" :
            if self.byr == None :
                self.fields += 1
            self.byr = value
        elif field == "iyr" :
            if self.iyr == None :
                self.fields += 1
            self.iyr = value
        elif field == "eyr" :
            if self.eyr == None :
                self.fields += 1
            self.eyr = value
        elif field == "hgt" :
            if self.hgt == None :
                self.fields += 1
            self.hgt = value
        elif field == "hcl" :
            if self.hcl == None :
                self.fields += 1
            self.hcl = value
        elif field == "ecl" :
            if self.ecl == None :
                self.fields += 1
            self.ecl = value
        elif field == "pid" :
            if self.pid == None :
                self.fields += 1
            self.pid = value
        elif field == "cid" :
            if self.cid == None :
                self.fields += 1
            self.cid = value

passports = []
fields = []

file = open("input.txt", "r")

"""parse input"""
for line in file :
    if line == "\n" :
        passport = Passport()
        for field in fields :
            field = field.split(':')
            passport.setField(field[0], field[1])    
        
        passports.append(passport)
        fields = []
    else :
        fields.extend(line.split())
        
passport = Passport()
for field in fields :
    field = field.split(':')
    passport.setField(field[0], field[1])    

passports.append(passport)
    
file.close()

counter = 0

for passport in passports :
    if passport.Valid() :
        counter += 1

print (f"valid passports:{counter}")