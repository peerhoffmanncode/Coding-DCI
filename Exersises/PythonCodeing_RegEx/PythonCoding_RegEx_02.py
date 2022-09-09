import re

text_to_search_in = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who 
actually visited Epsteins island. Oh boy how I hope no random Python Students 
extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pac.aintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""

email_pattern = r"([\w\.]+)@([\w\.]+)(\.)([a-zA-Z0-9]{1,3})" # the actual regular expression
results = re.finditer(email_pattern, text_to_search_in)      # using the pattern to search the target text

for item in results:        # for loop
    print(item)             # print the email


other_pattern = r"\br.+m" # the actual regular expression
result = re.search(other_pattern, text_to_search_in)      # using the pattern to search the target text
print(result)