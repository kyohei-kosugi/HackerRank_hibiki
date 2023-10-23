regex_pattern = r"^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))