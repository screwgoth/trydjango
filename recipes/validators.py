import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

valid_units_measurement = ['kg', 'oz', 'pounds']

def validate_units_measurement(units):
	ureg = pint.UnitRegistry()
	try:
		single_unit = ureg[units]
	except UndefinedUnitError as e:
		raise ValidationError(f'{units} is not a valid unit of measurement')
	except:
		raise ValidationError(f'{units} is invalid. Unknow error')

	# This is one of doing a limited validation if the "pint" packahe is not used
	# if units not in valid_units_measurement:
	# 	raise ValidationError(f'{units} is not a valid measurement unit')