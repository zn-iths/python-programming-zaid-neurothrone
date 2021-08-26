from shared.week_38_oop import Unit


unit = Unit(5)
# del unit.value

print(f"{unit.value} inches to {unit.inches_to_cm()} cm.")
print(f"{unit.value} cm to {unit.cm_to_inches():.2f} inches.")
fail_unit = Unit(-5)

print(unit.value)
print(unit)
