import re

# class to instantiate travelers' passaports
class Passenger:
    def __init__(self,info):
        self.infolist = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
        for each in self.infolist: setattr(self,each,False)
        self.cid = False    # exclude cid from list to differentiate passport from north pole
        self.passport_valid = False
        self.northpole_valid = False

        # set passport info from input
        self.set_passport(info)

    # set info
    def set_passport(self,info):
        for each in info:
            for field in each.split(): setattr(self,field.split(':')[0],field.split(':')[1].strip())

    # check each info field, set passport and northpole status, and return only northpole status
    def check_passport(self):
        for each in self.infolist:
            if not getattr(self,each): return False
        else:
            if not self.validate_year(self.byr,4,1920,2002): return False   #byr
            if not self.validate_year(self.iyr,4,2010,2020): return False   #iyr
            if not self.validate_year(self.eyr,4,2020,2030): return False   #eyr
            if (self.hgt).endswith("cm"):   #hgt
                if not self.validate_year((self.hgt).split("cm")[0],3,150,193): return False
            elif (self.hgt).endswith("in"):
                if not self.validate_year((self.hgt).split("in")[0],2,59,76): return False
            else: return False
            if not (re.search("\#[0-9a-f]{6}",self.hcl)): return False  #hcl
            if self.ecl not in ("amb","blu","brn","gry","grn","hzl","oth"): return False    #ecl
            if not (len(self.pid)==9 and (self.pid).isnumeric()): return False    #pid
            
            # if no previous return was called, nortpole is valid
            self.northpole_valid = True
            if self.cid: self.passport_valid = True #cid
            return self.northpole_valid

    def validate_year(self,field,l,min,max):
        if len(field)==l and int(field)>=min and int(field)<=max: return True
        else: return False

# open input file and go thorugh each passport and register into objects
with open("passports.txt","r") as passports:
    passenger_info = []
    count_valid = 0
    for line in passports.readlines():
        if line=="\n":  # fill passenger info and check if it's valid, and reset parser list
            newPassenger = Passenger(passenger_info)
            if newPassenger.check_passport(): count_valid +=1
            passenger_info = []
        else: passenger_info.append(line)
    
    # in case last passport isn't followed by "\n", there is need to account for info recorded in passenger_info
    if passenger_info:
        newPassenger = Passenger(passenger_info)
        if newPassenger.check_passport(): count_valid +=1

# output answers
print("There are %s valid passports\n\n" % count_valid)
