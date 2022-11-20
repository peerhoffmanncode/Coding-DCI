1. colou?r  
--> color or colour

Explanation: this RegEx will ma^(?=.\*[a-z])(?=.\*[A-Z])(?=.\*\d).{6,12}$ ch both versions of the word "Color" or Colour".
The ? means the u is 0 to 1 times in the word. 


2. (\W|^)[\w.\-]{0,25}@(gmail|deliveryhero)\.com(\W|$)  
--> emails with TLD gmail.com or deliveryhero.com

Explanation: Checks for a valid emails address.
(\W|^) is a group that searches for one char of anything other than a letter, digit or underscore, or marks the beginning of the string. After that, it searches for 0-25 letters, digits or underscores including the "." and "-". Then the @ is included, as well as the domain "gmail, or deliveryhero. The string is ending with the "." and the domain "com". The patter closes with any other than a letter, digit or underscore, or the end of the string.


3. ^(?=.\*[a-z])(?=.\*[A-Z])(?=.\*\d).{6,12}$  
--> PW  
6 to 12 characters in length  
Must have at least one uppercase letter  
Must have at least one lower case letter  
Must have at least one digit  
Should contain other characters  


4. ^\#?([a-f0-9]{6}|[a-f0-9]{3})$  
--> hex color code  

5. done$  
--> a text that ends with "done"  
