#digit
import re
text="apple 20 mango 40 guava 90"
print(re.findall(r"\d+",text))

# word
import re
text="apple 20 mango 40 guava 90"
print(re.findall(r"\w+",text))

#space
import re
text="apple 20 mango 40 guava 90"
print(re.findall(r"\s+",text))

#special character
import re
text="$1000"
print(re.findall(r"\$",text))
