
VALID_HCL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
VALID_ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

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
        """check number of fields"""
        if self.fields < 7 :
            return False
        if self.fields == 7 and self.cid != None :
            return False
        
        """check birth year"""
        if self.byr < 1920 or self.byr > 2002 :
            return False
        
        """check issue year"""
        if self.iyr < 2010 or self.iyr > 2020 :
            return False
        
        """check expiration year"""
        if self.eyr < 2020 or self.eyr > 2030 :
            return False
        
        """check height"""
        if self.hgt[-2:] == "cm" :
            if int(self.hgt[:-2]) < 150 or int(self.hgt[:-2]) > 193 :
                return False
        elif self.hgt[-2:] == "in" :
            if int(self.hgt[:-2]) < 59 or int(self.hgt[:-2]) > 76 :
                return False
        else :
            return False
        
        """check hair colour"""
        if self.hcl[0] != '#' :
            return False
        for i in range(1,7) :
            if self.hcl[i] not in VALID_HCL :
                return False
        
        """check eye colour"""
        if self.ecl not in VALID_ECL :
            return False
        
        """check passport id"""
        if len(self.pid) != 9 :
            return False
        
        """all checks satisfied"""
        return True
        
    def setField (self, field, value) :
        if field == "byr" :
            if self.byr == None :
                self.fields += 1
            self.byr = int(value)
        elif field == "iyr" :
            if self.iyr == None :
                self.fields += 1
            self.iyr = int(value)
        elif field == "eyr" :
            if self.eyr == None :
                self.fields += 1
            self.eyr = int(value)
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