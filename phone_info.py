### pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

# number="+13122730409"
# number="+919986233833"
# number="+919738476056"
# number="+17812771004"
number="+16828025166"
ch_num=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_num,"en"))  ## Prints the country which the phone number belongs to

service_provider=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_provider,"en"))  ## Prints the service provider for that number