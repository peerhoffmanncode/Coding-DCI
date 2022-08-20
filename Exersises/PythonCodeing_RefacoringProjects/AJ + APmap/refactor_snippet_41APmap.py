import sqlite3

#defining Alpha Protocol World Map Function
def APMap():
    
    ## // -- refactored by Peer Hoffmann 16aug2022 - 17aug2022 ##
    
    ## // -- Country Dict from the inet! ##
    
    countries = {
            "Afghanistan": 0,
            "Aland Islands": 0,
            "Albania": 0,
            "Algeria": 0,
            "American Samoa": 0,
            "Andorra": 0,
            "Angola": 0,
            "Anguilla": 0,
            "Antarctica": 0,
            "Antigua and Barbuda": 0,
            "ARGENTINIA": 0,
            "Armenia": 0,
            "Aruba": 0,
            "Australia": 0,
            "Austria": 0,
            "Azerbaijan": 0,
            "Bahamas": 0,
            "Bahrain": 0,
            "Bangladesh": 0,
            "Barbados": 0,
            "Belarus": 0,
            "Belgium": 0,
            "Belize": 0,
            "Benin": 0,
            "Bermuda": 0,
            "Bhutan": 0,
            "Bolivia": 0,
            "Bonaire, Sint Eustatius and Saba": 0,
            "Bosnia & Herzegovina": 0,
            "Botswana": 0,
            "Bouvet Island": 0,
            "Brasil": 0,
            "British Indian Ocean Territory": 0,
            "Brunei": 0,
            "Bulgaria": 0,
            "Burkina Faso": 0,
            "Burundi": 0,
            "CAR": 0,
            "Cambodia": 0,
            "Cameroon": 0,
            "Canada": 0,
            "Cape Verde": 0,
            "Cayman Islands": 0,
            "Central African Republic": 0,
            "Chad": 0,
            "Chile": 0,
            "China": 0,
            "Christmas Island": 0,
            "Cocos": 0,
            "Columbia": 0,
            "Comoros": 0,
            "Congo": 0,
            "Congo, The Democratic Republic of the": 0,
            "Cook Islands": 0,
            "Costa Rica": 0,
            "IVORY COAST": 0,
            "Croatia": 0,
            "Cuba": 0,
            "Curaçao": 0,
            "Cyprus": 0,
            "Czech Republic": 0,
            "Denmark": 0,
            "Djibouti": 0,
            "Dominica": 0,
            "Dominican Republic": 0,
            "DRC": 0,
            "Ecuador": 0,
            "Egypt": 0,
            "El Salvador": 0,
            "Equatorial Guinea": 0,
            "Eritrea": 0,
            "Estonia": 0,
            "Ethiopia": 0,
            "Falkland Islands (Malvinas)": 0,
            "Faroe Islands": 0,
            "Fiji": 0,
            "Finland": 0,
            "France": 0,
            "French Guiana": 0,
            "French Polynesia": 0,
            "French Southern Territories": 0,
            "Gabon": 0,
            "The Gambia": 0,
            "Georgia": 0,                
            "Germany": 0,
            "Ghana": 0,
            "Gibraltar": 0,
            "Greece": 0,
            "Greenland": 0,
            "Grenada": 0,
            "Guadeloupe": 0,
            "Guam": 0,
            "Guatemala": 0,
            "Guernsey": 0,
            "Guinea": 0,
            "Guinea-Bissau": 0,
            "Guyana": 0,
            "Haiti": 0,
            "Heard Island and McDonald Islands": 0,
            "Vatican City": 0,
            "Honduras": 0,
            "Hong Kong": 0,
            "Hungary": 0,
            "Iceland": 0,
            "India": 0,
            "Indonesia": 0,
            "Iran": 0,
            "Iraq": 0,
            "Ireland": 0,
            "Northern Ireland": 0,
            "Isle of Man": 0,
            "Israel": 0,
            "Italy": 0,
            "Jamaica": 0,
            "Japan": 0,
            "Jersey": 0,
            "Jordan": 0,
            "Kazakhstan": 0,
            "Kenya": 0,
            "Kiribati": 0,
            "NORTH KOREA": 0,
            "SOUTH KOREA": 0,
            "Kuwait": 0,
            "Kyrgyzstan": 0,
            "Laos": 0,
            "Latvia": 0,
            "Lebanon": 0,
            "Lesotho": 0,
            "Liberia": 0,
            "Lybia": 0,
            "Lichtenstein": 0,
            "Lithuania": 0,
            "Luxemburg": 0,
            "Macau": 0,
            "Macedonia": 0,
            "Madagascar": 0,
            "Malawi": 0,
            "Malaysia": 0,
            "Maldives": 0,
            "Mali": 0,
            "Malta": 0,
            "Marshall Islands": 0,
            "Martinique": 0,
            "Mauritania": 0,
            "Mauritius": 0,
            "Mayotte": 0,
            "Mexico": 0,
            "Micronesia": 0,
            "Moldova": 0,
            "Monaco": 0,
            "Mongolia": 0,
            "Montenegro": 0,
            "Montserrat": 0,
            "Morocco": 0,
            "Mozambique": 0,
            "Myanmar": 0,
            "Namibia": 0,
            "Nauru": 0,
            "Nepal": 0,
            "Netherlands": 0,
            "New Caledonia": 0,
            "New Zealand": 0,
            "Nicaragua": 0,
            "Niger": 0,
            "Nigeria": 0,
            "Niue": 0,
            "Norfolk Island": 0,
            "Northern Mariana Islands": 0,
            "Norway": 0,
            "Oman": 0,
            "Pakistan": 0,
            "Palau": 0,
            "PALESTINE": 0,
            "Panama": 0,
            "Papua New Guinea": 0,
            "Paraguay": 0,
            "Peru": 0,
            "PHILLIPPINES": 0,
            "Pitcairn": 0,
            "Poland": 0,
            "Portugal": 0,
            "Puerto Rico": 0,
            "Qatar": 0,
            "RC": 0,
            "Reunion": 0,
            "Romania": 0,
            "Russia": 0,
            "Rwanda": 0,
            "Saint Barthélemy": 0,
            "Saint Helena, Ascension and Tristan da Cunha": 0,
            "Saint Kitts and Nevis": 0,
            "Saint Lucia": 0,
            "Saint Martin (French part)": 0,
            "Saint Pierre and Miquelon": 0,
            "Saint Vincent and the Grenadines": 0,
            "Samoa": 0,
            "San Marino": 0,
            "Sao Tome & Principe": 0,
            "Saudi Arabia": 0,
            "Senegal": 0,
            "Serbia": 0,
            "Seychelles": 0,
            "Sierra Leone": 0,
            "Singapore": 0,
            "Sint Maarten (Dutch part)": 0,
            "Slovakia": 0,
            "Slovenia": 0,
            "Solomon Islands": 0,
            "Somalia": 0,
            "Somaliland": 0,
            "South Africa": 0,
            "South Georgia and the South Sandwich Islands": 0,
            "Spain": 0,
            "Sri Lanka": 0,
            "Sudan": 0,
            "Suriname": 0,
            "South Sudan": 0,
            "Svalbard and Jan Mayen": 0,
            "Swaziland": 0,
            "Sweden": 0,
            "Switzerland": 0,
            "Syria": 0,
            "Taiwan": 0,
            "Tajikistan": 0,
            "Tanzania": 0,
            "Thailand": 0,
            "Timor-Leste": 0,
            "Togo": 0,
            "Tokelau": 0,
            "Tonga": 0,
            "Trinidad and Tobago": 0,
            "Tunisia": 0,
            "Turkey": 0,
            "Turkmenistan": 0,
            "Turks and Caicos Islands": 0,
            "Tuvalu": 0,
            "UAE": 0,
            "Uganda": 0,
            "Ukraine": 0,
            "United Arab Emirates": 0,
            "United Kingdom": 0,
            "USA": 0,
            "United States Minor Outlying Islands": 0,
            "Uruguay": 0,
            "Uzbekistan": 0,
            "Vanuatu": 0,
            "Venezuela": 0,
            "Vietnam": 0,
            "Virgin Islands, British": 0,
            "Virgin Islands, U.S.": 0,
            "Wallis and Futuna": 0,
            "WESTERN SAHARA": 0,
            "Yemen": 0,
            "Zambia": 0,
            "Zimbabwe": 0,
            }
    
    ## // -- continents Dict from Peer ;-) ##
    continents = {                
                "NORTH AMERICA": 0,
                "SOUTH AMERICA": 0,
                "ANTARCTICA": 0,
                "EUROPE": 0,
                "AFRICA": 0,
                "ASIA": 0,
                "AUSTRALIA": 0,
                }

    # Convert the country Dict to ALL UPPERCASE KEYS and add ", "+KEY+"," to the key name.
    # Important for if statement later!
    for k,v in list(countries.items()):
        del countries[k]
        countries.update({", " + k.upper() + ",": v})
    
    # Convert the Dict to ALL UPPERCASE KEYS and add KEY+"," to the key name.
    # Important for if statement later!
    for k,v in list(continents.items()):
        del continents[k]
        continents.update({k.upper()+",": v})
    
    clear      = "\033[2J\033[1;1f"         # added this line, it was missing in function.
    print(clear)                            # clear full screen
    print("\n"*2)                           # print empty lines
    
    #PART I : CONTINENTS
    
    db = sqlite3.connect("Components\\Data\\APDB")              # open SQLlite DB and create db object
    cursor = db.cursor()                                        # create DB cursor 
    cursor.execute("""SELECT * FROM subjectsGREEN;""")          # execute search query subjectsGREEN
    for i in cursor.fetchall():
        if str(i[15]).upper() in continents:                    # is given continent in DICT ? including +KEY+","
            continents[str(i[15]).upper()] += 1                 # country found - add 1 to current value

    cursor.execute("""SELECT * FROM subjectsRED;""")            # execute search query subjectsRED
    for i in cursor.fetchall():                                 
        if   str(i[15]).upper() in continents:                  # is given continent in DICT ? including +KEY+","
            continents[str(i[15]).upper()] += 1                 # country found - add 1 to current value


    #### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #### c1, ... C7, all need to be changed to: continents[">CONTINENT NAME<,"]
    #### >> use the DICT and not the individual vars !
    #### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # c1 = 0 #North America, c2 = 0 #South America, c3 = 0 #Antarctica, c4 = 0 #Europe, c5 = 0 #Africa, c6 = 0 #Asia, c7 = 0 #Australia

    c1 = str(continents["NORTH AMERICA,"])
    c2 = str(continents["SOUTH AMERICA,"])
    c3 = str(continents["ANTARCTICA,"])
    c4 = str(continents["EUROPE,"])
    c5 = str(continents["AFRICA,"])
    c6 = str(continents["ASIA,"])
    c7 = str(continents["AUSTRALIA,"])
    
    
    pic = Fore.LIGHTBLACK_EX+"""          
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWX0KKkxkkONWWWWWNXOkd:'';ldxKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0Kk:,:,...  'clo:,,;:,'.    ....;oxolo0XXXXXXXXXXXXXXXWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNNXNXWX0Kl..lc'.. .,;;oc.                  ..ck0NXXXXXXXXXX0oxxoooldKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx:;oO0KWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXN0lkWKooOdxOl:o:. .:OKxc.                    .;OWXXXXXXXXXXXX0oo,.;clKXXXXXXXXXXXXXXXXXXXXWXXXXXXXXXXXN0OkccOWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKdloOk;c00dcx0x::c,..,xWXNOo;,;.                  .dWXXXXXXXXXXXXXXXKkXXKWXXXXXXXXXXXXXXXNOxxkONXXXXXXXWXKOxdxc..;;;dXXXXXXXXXXXKxxONNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXklcoOxlccoOo;xxlo:;c;c0XXXXXWNWWXc                 ,OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo;cd0NWNKNXXXN0x;.        ..;x00XWWKKNXXKdoxKXOKWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXK: ..,:coock0:'dold:,,.,:cOWXXXXXXX0'      """+Fore.LIGHTGREEN_EX+c3+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""      .'lXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo.oNXXXWo.lO00o,.          .......;;..oXXKKKxcoxxkXWXWXXXXXXXXXXNKNXXXXXXXXXX
                      XXXXXXXXWXOxdxkO0KXXWXXXNXKKKxdOx,     :0xol:OXl..... .;lOWXXXXXo'           .',dNXXXWKXXXXXXXXXXXXWNNNkocclkXWXXXXXWN0lx0K00O, ':,...                      .......     '::;:kKOO00xxkxxKXXXXXXXXXX
                      XXXXXXKxc'.    .....;cdd;...,,;lc,,::,;d0dl:.,xkc;dko:.  cXWXXXKo'        .'.'cOWXXXXXWWXXXXXXXXXXXXxlc.    ..:oON0k0kdoo:,..',..cc..                                        ..  ..   .':okXWXXXXXX
                      XXXXWKo,.                         .';..,,...  .;,cKKkk; .;,oNXXNc      ..'dXXNKkdxxxXXXXXXXXXXXXXXKc.   ..    ';cd:.'.          .,.                                                      .,,;cxNXXX
                      XXXXNd,'.                                    ';;oXWOo:. .:o0WXXWk.    c0XNWXXXXo,..cKXXXXXXXXXXNko,   .:l.    ,c,.                                                                       :OOdlkWXXX
                      XXXWKo,.                                   ,dK0kKWKooxdc:dXXXXXXWo.  :XXXXXXXXXWNKXWXXXXXXXXXKo,.    ;Ol                                                                      .''..    .:o0WXWXXXXX
                      XXXWx.    .'.;c;..                       .dNXXXXXWd   ;0NKNXXXXXXN0olKXXXXXXXXXXXXXXXXXXXWNWX0'      'O0:..                                                             ...''.cXKo,;odd0XXXXXXXXXXX
                      XXXXWOl'..dkkNXWXOl,.                    .dKNXXXXX:   .;:.cXXXXXXXXXXXXXXXXXXXXXXXXXXXWKol0XXWOccc;. cX0c.                                                            .dKXKXNKXNo..oNXXXXXXXXXXXXXX
                      XXWKkdddkkKXXXXXXXXNx.                    ..;oOXW0,       .oXXXXXXXXXXXXXXXXXXXXXXXXXWKx:.:XXXXk:cxdlkO:                                                             .dNWWWXXXXX:  :XXXXXXXXXXXXXXX
                      XXNkdkXWXXXXXXXXXXXXWx.                       .oNc          ,kWXXXXXXXXXXXXXXXXXXXXXXO,,o; :KKd;...,..                                                                .'cokNXXXXO,;0WXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXWo.                       ':.     ....''oWXXXXXXXXXXXXXXXXXXXXXXXOKkc,,;'                                            """+Fore.LIGHTGREEN_EX+c6+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                             .lckWXXXWXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXX0:.                             ..oKKd'.dWXXXXXXXXXXXXXXXXXXXXXXXWXd,.    """+Fore.LIGHTGREEN_EX+c4+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""               ..      .                                               .kKKWXXXXXXXXXXXXXXXXXXXXXX
  """+Style.RESET_ALL+Style.BRIGHT+"""    XXXXXXXXXXX     """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXX:           """+Fore.LIGHTGREEN_EX+c1+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                   .:dKX0kOWXXXXXXXXXXXXXXXXXXXXXXXWWX:        '.       ,l,;l'    ,do'   .lc                                       .dWKkKWXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""XXXXXXXXXXX    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""   X           X    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXWd.                            .lkkOXWXXXXXXXXXXXXXXXXXXXXXXXXXXNd;:c. .:lol:,;l:.    ;0Kxx0kc.  cKx,.  .,'                                    .;lOWWk;lXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X          X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXX:                           .cOWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK,    ,kNXXkkOkcco, 'c;,'..'::.   cKO,                                   .;,...oNXXXXkcOXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXNo.                         ;KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK:...,kK0Okxx0NOkXKld0l...        'kk'                                   .clkk,;0WWNO;.kXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXc.                       'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd,;;'..    cNWWXXWNNNK0kd'       ..                                     .lNXk;dKxc::dXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  XXXXXXXXXXXXXXX   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXNk'                   .;xKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc.          .:okXk:cx0K0Oo.                                               .kXWNKdxKWXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""XXXXXXXXXXXXX  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXWd;,.        .,,':lc.,0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXc.               ..   .....       ';.                                       :XXXXWWXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXNd:;.      ;0WNXWXXx'xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo.                         .;;.     .;ll:,.....                              .dNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXWxcl'    '0XXXXXXN0okXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNl                             cd.      .:;':xKKOd'           ..            ..:xx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXWXXO'   .OXXXdxXX00kdkXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'                             .dx.         .kWXXXKo:.      .l00c.      .::d0KNWXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWOc.  ,ll' cNXXXKloxoo0KNXXXXXXXXXXXXXXXXXXXXXXXXXXK,                              .dk,      .:OWXXXXXXK,    .cOWXXNl..    ;xkXXXXWOl0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXkoll'  ,lkNXWNWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXWk.                               .ll..',cxXWXXXXXXXXWx.  :0WXXXXXXOc     .xWXXXWd,dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOx, cNXXXNOxONXWWWXXXXXXXXXXXXXXXXXXXXXXXX0,                    """+Fore.LIGHTGREEN_EX+c5+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""            ':xOkkXXXXXXXXXXXXWd. dXXXXXXXXWk.,c.  lWXXXW0kdxNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc:dxkx;.  ':;,lXXXXXXXXXXXXXXXXXXXXXXXXXK:                                 ....:XXXXXXXXXXXXXNo;lOWXXXXXXXWxckkldXXXXW0OKxcoXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKkxl.         'oxONXXXXXXXXXXXXXXXXXXXXXNx,  ...,cc.                         ;KXXXXXXXXXXXXXXWNkxNXXXXXW00K:.lXXXXXNd:xXKxdXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWk.             ,kWXXXXXXXXXXXXXXXXXXXXXXxkKKXNXWKx:..                   .c0XXXXXXXXXXXXXXXXXXXXXXXXXW0xo:.,OWN0d, .dXNXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd.               ,OKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXWd..                 .c0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO,.lKXd.   ,oodO0k0XWXKXNXXXXXWNWXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.                ...':odONXXXXXXXXXXXXXXXXXXXXXXXXWkc'                ,OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.;OXd;,;xl.cKNXKXNd,',cokNXNkONXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.                       .,kWXXXXXXXXXXXXXXXXXXXXXXXXXK;              .xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNkllodxkKN0xkXXXWWWXO;   .:OO0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.                        cNXXXXXXXXXXXXXXXXXXXXXXXXXWd.              oWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0kdoxKXK0KNWXXWWXWOo:okccOWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.                     .lXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'              ;XXXW0KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWNWWKo:lkWNddNWKKWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.        """+Fore.LIGHTGREEN_EX+c2+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""           cNXXXXXXXXXXXXXXXXXXXXXXXXXXXXc               ,KN0l.lWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXd;:'   cKX:.dNXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKd;.                 oWXXXXXXXXXXXXXXXXXXXXXXXXXXX0'             'o0Nd. 'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx'        .,. '0WXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:                ,KXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.           ;KXXNl .oWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNOo:,.              ,xNXXXXXXW0KXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl             .:l0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl           cNXXK; ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXc.                   .oNXXXXXXNNXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN:            cXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.         cXWXXWKkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;           """+Fore.LIGHTGREEN_EX+c7+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""         .kXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'           '0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo.       cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo                     '0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.          ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:    .,xNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.   .,;cl:.         .dNXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk.       .,lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0loxkONXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWkclodONXXXW0d:.     ,OWXXXXXXXXXW00XXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo        ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo'..,oKXXXXXXXXXXXWd;dNX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNc     .cOXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxdKXXXXXXXXXXXW0xc:OWX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.   .oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXocKXXXXXXXXWXkl:xXNXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'  .cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWXXXXXXXXXK:'dXWXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.  .dWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKKWXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0,  ,0XXNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.cKWXKk0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0do0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL
    
    effect1.stop()      # stop any current sound
    effect1.play()      # play sound
    print(pic)          # print current MAP state

    input("")           # wait for user input (key press/ enter)
    
    #PART II : COUNTRIES
   
    cursor.execute("""SELECT * FROM subjectsGREEN;""")                                                      # execute search query subjectsGREEN
    for i in cursor.fetchall():
        if str(i[15]).upper() in countries:                                                                 # is given country in DICT ? including ", "+KEY+","
                countries[str(i[15]).upper()] += 1                                                          # add +1 if country is found
        
    cursor.execute("""SELECT * FROM subjectsRED;""")                                                        # execute search query subjectsRED
    for i in cursor.fetchall():
        if str(i[15]).upper() in countries:                                                                 # is given country in DICT ? including ", "+KEY+","
                countries[str(i[15]).upper()] += 1                                                          # add +1 if country is found
    
    for k,v in list(countries.items()):
        del countries[k]
        if v == 0:
            v_str = LIGHTGREEN_EX + str(v) + Style.RESET_ALL + Fore.LIGHTBLACK_EX                               # adding spaces [*3, 2, 1, 0]
        else:
            v_str = LIGHTGREEN_EX + str(v) + (" " * 2 - len(str(v))) + Style.RESET_ALL + Fore.LIGHTBLACK_EX     # adding spaces [*3, 2, 1, 0]
        
        countries.update({k: v_str})
    
    #### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #### t155, ... t189, need to be changed to: countries[", >COUNTRY NAME<,"]
    #### >> use the DICT and not the individual vars !
    #### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # t155, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, hh, t17, t18, t19, jj, t21, AD, ww, nn, ss, mm, t27, rr, uu, pp, qq, AA, zz, t34, tt, AE, ii, yy, AF, t40, t41, AC, vv, oo, AB, xx, t47, AL, AJ, WW, AK, AG, t53, AI, AH, t56, t57, t58, t59, t60, ll, t62, kk, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, LL, KK, JJ, II, HH, t92, t93, t94, t95, t96, t97, t98, t99, t100, t101, t102, t103, t104, t105, t106, t107, t108, GG, t110, t111, FF, DD, EE, CC, BB, AX, t118, t119, t120, t121, t122, t123, t124, t125, t126, t127, t128, t129, t130, t131, t132, t133, t134, t135, t136, XX, YY, t139, t140, SS, RR, QQ, PP, OO, t146, t147, t148, MM, t150, t151, TT, t153, VV, UU, ZZ, aa, bb, cc, NN, t161, t162, t163, t164, t165, t166, t167, t168, gg, t170, t171, t172, t173, t174, t175, t176, t177, t178, t179, t180, dd, t182, ff, t184, ee, t186, t187, t188, t189   =   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        
    t1 = str(countries[", CANADA,"])
    t2 = str(countries[", USA,"])
    t3 = str(countries[", MEXICO,"])
    t4 = str(countries[", ARGENTINIA,"])
    t5 = str(countries[", BOLIVIA,"])
    t6 = str(countries[", BRASIL,"])
    t7 = str(countries[", CHILE,"])
    t8 = str(countries[", ECUADOR,"])
    t9 = str(countries[", GUYANA,"])
    t10 = str(countries[", COLUMBIA,"])
    t11 = str(countries[", PARAGUAY,"])
    t12 = str(countries[", PERU,"])
    t13 = str(countries[", SURINAME,"])
    t14 = str(countries[", URUGUAY,"])
    t15 = str(countries[", VENEZUELA,"])
    t16 = str(countries[", PORTUGAL,"])
    hh = str(countries[", GERMANY,"])
    t17 = str(countries[", FRANCE,"])
    t18 = str(countries[", ITALY,"])
    t19 = str(countries[", SPAIN,"])
    jj = str(countries[", UNITED KINGDOM,"])
    t21 = str(countries[", SWITZERLAND,"])
    AD = str(countries[", GREECE,"])
    ww = str(countries[", CROATIA,"])
    nn = str(countries[", NETHERLANDS,"])
    ss = str(countries[", POLAND,"])
    mm = str(countries[", BELGIUM,"])
    t27 = str(countries[", ICELAND,"])
    rr = str(countries[", SWEDEN,"])
    uu = str(countries[", AUSTRIA,"])
    pp = str(countries[", DENMARK,"])
    qq = str(countries[", NORWAY,"])
    AX = str(countries[", SERBIA,"])
    zz = str(countries[", UKRAINE,"])
    t34 = str(countries[", MALTA,"])
    tt = str(countries[", CZECH REPUBLIC,"])
    AE = str(countries[", ROMANIA,"])
    ii = str(countries[", IRELAND,"])
    yy = str(countries[", HUNGARY,"])
    AF = str(countries[", BULGARIA,"])
    t40 = str(countries[", FINLAND,"])
    t41 = str(countries[", CYPRUS,"])
    AC = str(countries[", ALBANIA,"])
    vv = str(countries[", SLOVENIA,"])
    oo = str(countries[", LUXEMBURG,"])
    AB = str(countries[", MONTENEGRO,"])
    xx = str(countries[", SLOVAKIA,"])
    t47 = str(countries[", MONACO,"])
    AL = str(countries[", LITHUANIA,"])
    AJ = str(countries[", ESTONIA,"])
    WW = str(countries[", BOSNIA & HERZEGOVINA,"])
    AK = str(countries[", LATVIA,"])
    AG = str(countries[", MACEDONIA,"])
    t53 = str(countries[", VATICAN CITY,"])
    AI = str(countries[", BELARUS,"])
    AH = str(countries[", MOLDOVA,"])
    t56 = str(countries[", GIBRALTAR,"])
    t57 = str(countries[", LICHTENSTEIN,"])
    t58 = str(countries[", ANDORRA,"])
    t59 = str(countries[", FAROE ISLANDS,"])
    t60 = str(countries[", SAN MARINO,"])
    ll = str(countries[", ISLE OF MAN,"])
    t62 = str(countries[", JERSEY,"])
    kk = str(countries[", NORTHERN IRELAND,"])
    t64 = str(countries[", GUERNSEY,"])
    t65 = str(countries[", ALAND ISLANDS,"])
    t66 = str(countries[", AUSTRALIA,"])
    t67 = str(countries[", FIJI,"])
    t68 = str(countries[", KIRIBATI,"])
    t69 = str(countries[", MARSHALL ISLANDS,"])
    t70 = str(countries[", MICRONESIA,"])
    t71 = str(countries[", NAURU,"])
    t72 = str(countries[", NEW ZEALAND,"])
    t73 = str(countries[", PALAU,"])
    t74 = str(countries[", PAPUA NEW GUINEA,"])
    t75 = str(countries[", SAMOA,"])
    t76 = str(countries[", SOLOMON ISLANDS,"])
    t77 = str(countries[", TONGA,"])
    t78 = str(countries[", TUVALU,"])
    t79 = str(countries[", VANUATU,"])
    t80 = str(countries[", EGYPT,"])
    t81 = str(countries[", LYBIA,"])
    t82 = str(countries[", TUNISIA,"])
    t83 = str(countries[", ALGERIA,"])
    t84 = str(countries[", MOROCCO,"])
    t85 = str(countries[", WESTERN SAHARA,"])
    t86 = str(countries[", MAURITANIA,"])
    LL = str(countries[", SENEGAL,"])
    KK = str(countries[", THE GAMBIA,"])
    JJ = str(countries[", GUINEA-BISSAU,"])
    II = str(countries[", GUINEA,"])
    HH = str(countries[", SIERRA LEONE,"])
    t92 = str(countries[", ERITREA,"])
    t93 = str(countries[", ETHIOPIA,"])
    t94 = str(countries[", SOMALIA,"])
    t95 = str(countries[", SOMALILAND,"])
    t96 = str(countries[", DRC,"])
    t97 = str(countries[", EQUATORIAL GUINEA,"])
    t98 = str(countries[", RWANDA,"])
    t99 = str(countries[", BURUNDI,"])
    t100 = str(countries[", ANGOLA,"])
    t101 = str(countries[", MALAWI,"])
    t102 = str(countries[", MOZAMBIQUE,"])
    t103 = str(countries[", NAMIBIA,"])
    t104 = str(countries[", SOUTH AFRICA,"])
    t105 = str(countries[", LESOTHO,"])
    t106 = str(countries[", COMOROS,"])
    t107 = str(countries[", MAURITIUS,"])
    t108 = str(countries[", SAO TOME & PRINCIPE,"])
    GG = str(countries[", LIBERIA,"])
    t110 = str(countries[", MALI,"])
    t111 = str(countries[", UGANDA,"])
    FF = str(countries[", IVORY COAST,"])
    DD = str(countries[", BURKINA FASO,"])
    EE = str(countries[", GHANA,"])
    CC = str(countries[", TOGO,"])
    BB = str(countries[", BENIN,"])
    AA = str(countries[", NIGERIA,"])
    t118 = str(countries[", NIGER,"])
    t119 = str(countries[", CHAD,"])
    t120 = str(countries[", SUDAN,"])
    t121 = str(countries[", SOUTH SUDAN,"])
    t122 = str(countries[", DJIBOUTI,"])
    t123 = str(countries[", KENYA,"])
    t124 = str(countries[", CAR,"])
    t125 = str(countries[", RC,"])
    t126 = str(countries[", GABON,"])
    t127 = str(countries[", CAMEROON,"])
    t128 = str(countries[", TANZANIA,"])
    t129 = str(countries[", ZAMBIA,"])
    t130 = str(countries[", ZIMBABWE,"])
    t131 = str(countries[", MADAGASCAR,"])
    t132 = str(countries[", BOTSWANA,"])
    t133 = str(countries[", SWAZILAND,"])
    t134 = str(countries[", CAPE VERDE,"])
    t135 = str(countries[", MAYOTTE,"])
    t136 = str(countries[", REUNION,"])
    XX = str(countries[", PAKISTAN,"])
    YY = str(countries[", AFGHANISTAN,"])
    t139 = str(countries[", IRAN,"])
    t140 = str(countries[", TURKEY,"])
    SS = str(countries[", IRAQ,"])
    RR = str(countries[", SYRIA,"])
    QQ = str(countries[", LEBANON,"])
    PP = str(countries[", JORDAN,"])
    OO = str(countries[", ISRAEL,"])
    t146 = str(countries[", PALESTINE,"])
    t147 = str(countries[", SAUDI ARABIA,"])
    t148 = str(countries[", YEMEN,"])
    MM = str(countries[", QATAR,"])
    t150 = str(countries[", UAE,"])
    t151 = str(countries[", OMAN,"])
    TT = str(countries[", KUWAIT,"])
    t153 = str(countries[", GEORGIA,"])
    VV = str(countries[", ARMENIA,"])
    UU = str(countries[", AZERBAIJAN,"])
    t155 = str(countries[", KAZAKHSTAN,"])
    ZZ = str(countries[", TURKMENISTAN,"])
    aa = str(countries[", UZBEKISTAN,"])
    bb = str(countries[", TAJIKISTAN,"])
    cc = str(countries[", KYRGYZSTAN,"])
    NN = str(countries[", BAHRAIN,"])
    t161 = str(countries[", CHRISTMAS ISLAND,"])
    t162 = str(countries[", RUSSIA,"])
    t163 = str(countries[", JAPAN,"])
    t164 = str(countries[", INDIA,"])
    t165 = str(countries[", CHINA,"])
    t166 = str(countries[", INDONESIA,"])
    t167 = str(countries[", VIETNAM,"])
    t168 = str(countries[", SINGAPORE,"])
    gg = str(countries[", THAILAND,"])
    t170 = str(countries[", PHILLIPPINES,"])
    t171 = str(countries[", NORTH KOREA,"])
    t172 = str(countries[", SOUTH KOREA,"])
    t173 = str(countries[", MALAYSIA,"])
    t174 = str(countries[", HONG KONG,"])
    t175 = str(countries[", MYANMAR,"])
    t176 = str(countries[", SRI LANKA,"])
    t177 = str(countries[", CAMBODIA,"])
    t178 = str(countries[", BANGLADESH,"])
    t179 = str(countries[", TAIWAN,"])
    t180 = str(countries[", MALDIVES,"])
    dd = str(countries[", NEPAL,"])
    t182 = str(countries[", MACAU,"])
    ff = str(countries[", LAOS,"])
    t184 = str(countries[", MONGOLIA,"])
    ee = str(countries[", BHUTAN,"])
    t186 = str(countries[", BRUNEI,"])
    t187 = str(countries[", TIMOR-LESTE,"])
    t188 = str(countries[", COCOS,"])  
        
    pic = Fore.LIGHTBLACK_EX+"""          
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWX0KKkxkkONWWWWWNXOkd:'';ldxKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0Kk:,:,...  'clo:,,;:,'.    ....;oxolo0XXXXXXXXXXXXXXXWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNNXNXWX0Kl..lc'.. .,;;oc.                  ..ck0NXXXXXXXXXX0oxxoooldKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx:;oO0KWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXN0lkWKooOdxOl:o:. .:OKxc.                    .;OWXXXXXXXXXXXX0oo,.;clKXXXXXXXXXXXXXXXXXXXXWXXXXXXXXXXXN0OkccOWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKdloOk;c00dcx0x::c,..,xWXNOo;,;.                  .dWXXXXXXXXXXXXXXXKkXXKWXXXXXXXXXXXXXXXNOxxkONXXXXXXXWXKOxdxc..;;;dXXXXXXXXXXXKxxONNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXklcoOxlccoOo;xxlo:;c;c0XXXXXWNWWXc                 ,OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo;cd0NWNKNXXXN0x;.        ..;x00XWWKKNXXKdoxKXOKWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXK: ..,:coock0:'dold:,,.,:cOWXXXXXXX0'             .'lXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo.oNXXXWo.lO00o,.          .......;;..oXXKKKxcoxxkXWXWXXXXXXXXXXNKNXXXXXXXXXX
                      XXXXXXXXWXOxdxkO0KXXWXXXNXKKKxdOx,     :0xol:OXl..... .;lOWXXXXXo'           .',dNXXXWKXXXXXXXXXXXXWNNNkocclkXWXXXXXWN0lx0K00O, ':,...                      .......     '::;:kKOO00xxkxxKXXXXXXXXXX
                      XXXXXXKxc'.    .....;cdd;...,,;lc,,::,;d0dl:.,xkc;dko:.  cXWXXXKo'        .'.'cOWXXXXXWWXXXXXXXXXXXXxlc.    ..:oON0k0kdoo:,..',..cc..                                        ..  ..   .':okXWXXXXXX
                      XXXXWKo,.                         .';..,,...  .;,cKKkk; .;,oNXXNc      ..'dXXNKkdxxxXXXXXXXXXXXXXXKc.   ..    ';cd:.'.          .,.                                                      .,,;cxNXXX
                      XXXXNd,'.                                    ';;oXWOo:. .:o0WXXWk.    c0XNWXXXXo"""+t27+"""cKXXXXXXXXXXNko,   .:l.    ,c,.                                                                       :OOdlkWXXX
                      XXXWKo,.                                   ,dK0kKWKooxdc:dXXXXXXWo.  :XXXXXXXXXWNKXWXXXXXXXXXKo,.    ;Ol  """+t40+"""                                                                 .''..    .:o0WXWXXXXX
                      XXXWx.    .'.;c;..            """+t1+"""         .dNXXXXXWd   ;0NKNXXXXXXN0olKXXXXXXXXXXXXXXXXXXXWNWX0'"""+qq+"""   """+rr+""" 'O0:..                        """+t162+"""                               ...''.cXKo,;odd0XXXXXXXXXXX
                      XXXXWOl'..dkkNXWXOl,.                    .dKNXXXXX:   .;:.cXXXXXXXXXXXXXXXXXXXXXXXXXXXWKol0XXWOccc;. cX0c"""+AJ+"""                                                           .dKXKXNKXNo..oNXXXXXXXXXXXXXX
                      XXWKkdddkkKXXXXXXXXNx.                    ..;oOXW0,       .oXXXXXXXXXXXXXXXXXXXXXXXXXWkx"""+ll+""":XXXXk:cxdlkO:"""+AK+"""                                                           .dNWWWXXXXX:  :XXXXXXXXXXXXXXX
                      XXNkdkXWXXXXXXXXXXXXWx.                       .oNc          ,kWXXXXXXXXXXXXXXXXXXXXXXO"""+ii+""".;"""+jj+"""XXd;"""+pp+""".,.. """+AL+"""  """+AI+"""                                                         .'cokNXXXXO,;0WXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXWo.                       ':.     ....''oWXXXXXXXXXXXXXXXXXXXXXXXOKkc,,;'"""+nn+"""    """+ss+"""        """+zz+"""                   """+t155+"""                                 .lckWXXXWXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXX0:.                             ..oKKd'.dWXXXXXXXXXXXXXXXXXXXXXXXWXd,. """+mm+oo+""" """+hh+""" """+tt+""" """+xx+"""  """+AH+"""  ..      .                                               .kKKWXXXXXXXXXXXXXXXXXXXXXX
  """+Style.RESET_ALL+Style.BRIGHT+"""    XXXXXXXXXXX     """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXX:                               .:dKX0kOWXXXXXXXXXXXXXXXXXXXXXXXWWX: """+t17+"""     """+t21+uu+""" """+yy+AE+""" ,l,;l'    ,do'   .lc                                      .dWKkKWXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   XXXXXXXXXXX    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""   X           X    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXWd.         """+t2+"""                 .lkkOXWXXXXXXXXXXXXXXXXXXXXXXXXXXNd;:c. .:lol:."""+vv+ww+WW+AX+AF+"""0Kxx0kc.  cKx,.  .,'                                   .;lOWWk; XXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X          X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXX:                           .cOWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK,  """+t19+""",kNXXkk..xco,"""+AB+"""c;,'..'::."""+t153+"""KO,    """+aa+"""                             .;,  """+t171+"""XXXk  XXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXNo.                         ;KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK: """+t16+""",kK0Okxx0x."""+t18+"."+AC+"""."""+AD+""" """+t140+"""  """+UU+VV+"""k'  """+ZZ+"""       """+cc+"""                      .clkk  0WWNO;"""+t163+"""XXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXc.                       'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd,;;'....."""+t82+"""WWXX  N K0kd' """+RR+SS+"""  ..          """+bb+"""              """+t165+"""       .lNXk"""+t172+"""c   XXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  XXXXXXXXXXXXXXX   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXNk'                   .;xKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc."""+t84+"""       .:okXk:cx0K0Oo."""+QQ+"""      """+t139+"""  """+YY+"""                               .kXWNKdxKWXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   XXXXXXXXXXXXX  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXWd;,.        .,,':lc.,0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXc.                   """+t80+"""   """+OO+PP+"""  """+TT+""";.         """+XX+"""       """+dd+" "+ee+"""                :XXXXWWXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXNd:;.  """+t3+"""  ;0WNXWXXx'xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo.       """+t83+"""      """+t81+"""       ;;.     .;ll:,.....             """+t178+"""             .dNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXWxcl'    '0XXXXXXN0okXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNl"""+t85+"""                          cd. """+t147+NN+MM+"""':xKKOd'    """+t164+"""   .."""+t175+ff+"""      ..:xx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXWXXO'   .OXXXdxXX00kdkXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'   """+t86+"""                       .dx.       """+t150+"""WXXXKo:.      .l00c.      .::d0KNWXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWOc.  ,ll' cNXXXKloxoo0KNXXXXXXXXXXXXXXXXXXXXXXXXXXK,        """+t110+t118+t119+"""  """+t120+"""    .dk,      """+t151+"""XXXXXXK,    .cOWXXNl.."""+gg+"""  ;xkXXXXWOl0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXkoll'  ,lkNXWNWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXWk."""+KK+LL+"""                          """+t92+"""l.."""+t148+"""XWXXXXXXXXWx.  :0WXXXXXXOc    """+t176+"""XXXWd,dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOx, cNXXXNOxONXWWWXXXXXXXXXXXXXXXXXXXXXXXX0,"""+JJ+"""    """+DD+"""          """+t124+t121+"""      """+t122+"""OkkXXXXXXXXXXXXXXXXXXXXXXXXXWk.,"""+t177+"""lWXXXW0k"""+t170+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc:dxkx;.  ':;,lXXXXXXXXXXXXXXXXXXXXXXXXXK:"""+II+HH+FF+EE+CC+BB+""" """+AA+"""                  ....:XXXXXXXXXXXXXXXXXXXXXXXXXXWxckkldXXXXW0OKxcoXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKkxl."""+t10+"""   """+t15+"""'oxONXXXXXXXXXXXXXXXXXXXXXNx,"""+GG+"""...,"""+cc+""".   """+t127+"""            """+t93+""" """+t95+"""KXXXXXXXXXXXXXXXXXXXXXXXXW00K:"""+t173+"""XXXNd:xXKxdXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWk.       """+t9+""" """+t13+""",kWXXXXXXXXXXXXXXXXXXXXXXxkKKXNXWKx:.."""+t97+t125+t111+""" """+t123+"""   .c0XXXXXXXXXXXXXXXXXXXXXXXXXW0xo:.,OWN0d, .dXNXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd.               ,OKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXWd.."""+t126+t96+t98+"""      """+t94+"""0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO,"""+t168+"""d.   ,oodO0k0XWXKXNXXXXXWNWXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO."""+t8+"""              ...':odONXXXXXXXXXXXXXXXXXXXXXXXXWkc'       """+t99+"""  """+t128+""",OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.;OXd;,;xl.cKNXKXNd,',cokNXNkONXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.                       .,kWXXXXXXXXXXXXXXXXXXXXXXXXXK;              .xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNkllodxkKN0x"""+t166+"""WWWXO; """+t74+""":OO0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx. """+t12+"""        """+t6+"""          cNXXXXXXXXXXXXXXXXXXXXXXXXXWd."""+t100+t129+t101+"""  oWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0kdoxKXK0KNWXXWWXWOo:okccOWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.                     .lXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'             """+t102+"""XW0KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWNWWKo:lkWNddNWKKWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.    """+t5+"""              cNXXXXXXXXXXXXXXXXXXXXXXXXXXXXc        """+t130+"""   ,KN0l.lWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXd;:'   cKX:.dNXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKd;.                 oWXXXXXXXXXXXXXXXXXXXXXXXXXXX0'"""+t103+""" """+t132+"""    'o0Nd. 'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx'        .,. '0WXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:    """+t11+"""         ,KXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.           ;KXXNl"""+t131+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNOo:,.              ,xNXXXXXXW0KXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl             .:l0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl           cNXXK; ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXc.         """+c7+"""        .oNXXXXXXNNXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN:"""+t7+"""          cXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.         cXWXXWKkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;                     .kXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'           '0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo."""+t104+"""   cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo                     '0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.        """+t14+""" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:    .,xNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.   .,;cl:.         .dNXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk.  """+t4+"""   .,lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0loxkONXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWkclodONXXXW0d:.     ,OWXXXXXXXXXW00XXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo        ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo'..,oKXXXXXXXXXXXWd;dNX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNc     .cOXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxdKXXXXXXXXXXXW0xc:OWX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.   .oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXocKXXXXXXXXWXk"""+t72+"""XNXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'  .cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWXXXXXXXXXK:'dXWXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.  .dWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKKWXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0,  ,0XXNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.cKWXKk0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0do0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""
    
    
    print(clear)    # clear screen
    print("\n"*2)   # print two empyt lines
    effect1.stop()  # stop sound
    effect1.play()  # play sound
    print(pic)      # print current MAP
    input("")       # wait for user input (key press/ enter)

APMap()