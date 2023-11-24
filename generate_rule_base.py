from model import input_lvs
from itertools import product

Communication = {   "Ineffective": 0,
					"Average": 0.33,
					"Effective": 0.66,
					"Exceptional": 1}

Professional_skills = { "Inadequate": 0,
						"Basic": 0.2,
						"Competent": 0.4,
						"Advanced": 0.6,
						"Expert": 0.8,
						"Professional": 1}

Leadership = {"Lack": 0,
			  "Limited": 0.2,
			  "Moderate": 0.4,
			  "Effective": 0.6,
			  "Strong": 0.8,
			  "Exceptional": 1}

Adaptability = {"Limited": 0,
				"Moderate": 0.33,
				"Good": 0.66,
				"Exceptional": 1}

coef = {"Communication": 0.27,
		"Professional_skills": 0.3,
		"Leadership": 0.2,
		"Adaptability": 0.23}

Class = {"Exceptional": 0.75,
		 "Expert": 0.67,
		 "Highly Qualified": 0.6,
	     "Effective": 0.54,
		 "Competent": 0.48,
		 "Average": 0.42,
		 "Satisfactory": 0.36,
		 "Irresponsible": 0.28,
		 "Unprofessional": 0}


# Извлекаем имена терминов принадлежности для каждой переменной
term_names_lists = [list(var['terms'].keys()) for var in input_lvs]

# Создаем список кортежей всех возможных комбинаций
combinations = list(product(*term_names_lists))
rule_base = []
values = set()
keys = []
for comb in combinations:
	Communication_coef = Communication[comb[0]] * coef["Communication"]
	Professional_coef = Professional_skills[comb[1]] * coef["Professional_skills"]
	Leadership_coef = Leadership[comb[2]] * coef["Leadership"]
	Adaptability_coef = Adaptability[comb[3]] * coef["Adaptability"]
	res = Communication_coef + Professional_coef + Leadership_coef + Adaptability_coef
	values.add(res)

	for key, value in Class.items():
		if res >= value:
			keys.append(key)
			rule_base.append((comb, key))
			break

# set_key = set(keys)

# for key in set_key:
# 	print(key, "-", keys.count(key))

# i = 0
# for value in sorted(values):
# 	i = i + 1
# 	if i == 70:
# 		print(value)
# 		i = 0

# for value in sorted(values):
# 	print(value)

# print(len(values))

for rule in rule_base:
	print(str(rule) + ",")

# print(len(rule_base))
