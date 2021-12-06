"""
Write a function using 'if/elif/else' conditionals to compute the
BMI of a person, and return the risk associated
with cardiovascular diseases.

BMI = weight(kg)/( height(m)*height(m) )

BMI				|	Risk
------------------------------------------
27.5 and above	|	High Risk
23 - 27.4		|	Moderate Risk
18.5 - 22.9		|	Low Risk
Below 18.5		|	Risk of nutritional deficiency diseases

Examples

   >>> HealthScreen(85, 1.75)
   'Your BMI is 27.8 (High Risk).'
   >>> HealthScreen(68, 1.65)
   'Your BMI is 25.0 (Moderate Risk).'
   >>> HealthScreen(60, 1.63)
   'Your BMI is 22.6 (Low Risk).'
   >>> HealthScreen(40,1.58)
   'Your BMI is 16.0 (Risk of nutritional deficiency diseases).'
"""

def HealthScreen(weight, height):
	""" Prints the Risk acco. to BMI """
	BMI = float(weight)/float( height*height )
	m = ""
	
	if BMI >= 27.5:
		m = "High Risk"
	elif 23<=BMI<=27.4:
		m = "Moderate Risk"
	elif 18.5<BMI<=22.9:
		m = "Low Risk"
	else :
		m = "Risk of nutritional deficiency diseases"
	return  'Your BMI is {} ({}).'.format(round(BMI,1) , m)


print(HealthScreen(85, 1.75))
print(HealthScreen(60, 1.63))
print(HealthScreen(40, 1.58))













