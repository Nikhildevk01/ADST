print("------HOSPITAL MANAGEMENT APPOINTMENT------")


name = input("Enter patient name: ")

req = input("Enter requested departments: ")
availa = input("Enter available departments: ")
prev = input("Enter previously visited departments: ")
doc = input("Enter preferred doctors: ")
adoc = input("Enter available doctors: ")
emer = input("Enter emergency departments: ")

print("PATIENT:", name)


print("Requested departments:", req)
print("First department:", req[0])
print("First 2 departments:", req[:2])


r = set(req)
a = set(availa)
p = set(prev)
e = set(emer)


common = r.intersection(a)


un = r.difference(a)


old = r.intersection(p)


em = r.intersection(e)


dup = len(req) - len(r)
all_dep = r.union(a)
a.add("Emergency")


if "Emergency" in a:
    a.remove("Emergency")


d = set(doc).intersection(set(adoc))


if "Cardiology" in r:
    print("Cardiology is requested")


if len(em) > 0:
    rec = list(em)[0]
elif len(common) > 0:
    rec = list(common)[0]
else:
    rec = "No department"


if len(em) > 0:
    status = "Emergency Appointment"
elif len(common) > 0:
    status = "Appointment Available"
else:
    status = "Appointment Not Available"


print("\n----- APPOINTMENT REPORT -----")
print("Patient Name:", name)
print("Requested:", req)
print("Available:", list(common))
print("Unavailable:", list(un))
print("Previous:", list(old))
print("Emergency:", list(em))
print("Duplicate Requests:", dup)
print("Common Doctors:", list(d))
print("Recommended Department:", rec)