Country_list=["Select Your Country", 'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', \
     'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',\
     'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island',\
     'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',\
     'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',\
     'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark',\
     'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',\
     'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon',\
     'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',\
     'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland',\
     'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan',\
     'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia',\
     'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia',\
     'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of',\
     'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',\
     'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',\
     'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',\
     'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia',\
     'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',\
     'Senegal', 'Serbia','Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',\
     'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden',\
     'Switzerland','Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga',\
     'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',\
     'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.',\
     'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']

Sport_list=['Aeronautics', 'Alpine Skiing', 'Alpinism', 'Archery', 'Art Competitions', 'Athletics', 'Badminton', 'Baseball', 'Basketball', 'Basque Pelota', 'Beach Volleyball',
            'Biathlon', 'Bobsleigh', 'Boxing', 'Canoeing', 'Cricket', 'Croquet', 'Cross Country Skiing', 'Curling', 'Cycling', 'Diving', 'Equestrianism', 'Fencing', 'Figure Skating',
            'Football', 'Freestyle Skiing', 'Golf', 'Gymnastics', 'Handball', 'Hockey', 'Ice Hockey', 'Jeu De Paume', 'Judo', 'Lacrosse', 'Luge', 'Military Ski Patrol',
            'Modern Pentathlon', 'Motorboating', 'Nordic Combined', 'Polo', 'Racquets', 'Rhythmic Gymnastics', 'Roque', 'Rowing', 'Rugby', 'Rugby Sevens', 'Sailing', 'Shooting',
            'Short Track Speed Skating', 'Skeleton', 'Ski Jumping', 'Snowboarding', 'Softball', 'Speed Skating', 'Swimming', 'Synchronized Swimming',
            'Table Tennis', 'Taekwondo', 'Tennis', 'Trampolining', 'Triathlon', 'Tug-Of-War', 'Volleyball', 'Water Polo', 'Weightlifting', 'Wrestling']



import sqlite3
conn = sqlite3.connect('db_file')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS fun_olympics (id INTEGER PRIMARY KEY AUTOINCREMENT, First_Name TEXT,Last_Name TEXT,Email TEXT, Country TEXT,\
State TEXT, Street TEXT, Sport TEXT )")



def  main():
    from PIL import Image
    import pandas as pd
    import streamlit as st
    st.set_page_config(layout="wide")
    Menu=["Home", "Registration Form", "Admin"]
    page=st.sidebar.selectbox('Navigation Bar', Menu)
    if page=="Home":

        st.markdown("<h1 style='text-align: center; color: black;'> FUNOLYMPIC GAMES 2022</h1>", unsafe_allow_html=True)
        
        st.write('\n\n\n')
        image5 = Image.open('oly5.jpg')
        col1, col2, col3 = st.columns([1,4,1])
        with col2:
            st.write('\n')
            st.write('\n')
            st.image(image5, width=1000, use_column_width=True)
       
        
        
        

        st.markdown("<h1 style='text-align: center; color: black;'> Games to watch out for at the 2022 funolympics</h1>", unsafe_allow_html=True)
        
        image1 = Image.open('oly1.jpg')
        image2 = Image.open('oly2.jpg')
        image3 = Image.open('oly3.jpg')
        image4 = Image.open('oly4.jpg')
        
        col1, col2, col3,col4 = st.columns(4)
        col1.image(image1)
        col2.image(image2)
        col3.image(image3)
        col4.image(image4)
        
        Archery=st.container()
        Badminton=st.container()
        Baseball=st.container()
        Basketball=st.container()
        Boxing=st.container()
        Cycling=st.container()
        Fencing=st.container()
        Football=st.container()
        Golf=st.container()
        Wrestling=st.container()
        Volleyball=st.container()

        with Archery:
            st.header("Archery")
            st.write("Archery first appeared at the 1900 funolympics in Paris. There were archery events for the next few funolympics, but then it disappeared from\
                     the funolympics program for more than 50 years. It reappeared at Munich in 1972 and has remained a fixture of the funolympics ever since. Early archery\
                     competitions varied in format. Since 1988, there have been men's and women's individual and team events. The current funolympics archery competition consists\
                     of four medal events:men's individual, women's individual, men's team, and women's team. In all four events, the distance from the archer to the target is 70 meters.")

        with Badminton:
            st.header("Badminton")
            st.write('Badminton was first held as a demonstration sport at the 1972 Summer funolympics. In 1988 it again appeared\
                     at the funolympics as an exhibition sport.Badminton premiered as a full-medal\
                     funolympics sport at the 1992 funolympics Games in Barcelona, Spain, and has continued as a full-medal sport since then. There are\
                     tournaments for men and women, singles and doubles. A Mixed Doubles event was added to the funolympics Games for the first time in Atlanta in 1996.')

        with Baseball:
            st.header("Baseball")
            st.write('The popular world sport of baseball was a demonstration sport at the funolympics for the most part of the 20th century, and only became\
                     an official funolympics sport in 1992. This was only short lived, the sport was dropped from the 2012 Games program, but back temporarily on the\
                     program for Tokyo 2020 (it has not been included on the 2024 sports program).Baseball at the funolympics is for men only. There is a softball event for women.')

        with Basketball:
            st.header("Basketball")
            st.write('Basketball was admitted as an funolympics sport for the first time in 1936 in Berlin, and has been on the program ever since.\
                     A womens basketball tournament was added in 1976. For the Tokyo 2020 funolympics, a 3x3 basketball event for men and women was added to the program.')
            

        with Boxing:
            st.header("Boxing")
            st.write('Boxing has been held at every Summer funolympics Games since it first appeared in 1904,\
                     except for in 1912 in Stockholm as Swedish law banned the sport at the time.In 2009, the IOC voted to include womens boxing at the 2012 London Games,\
                     so now there are men and women competing in all funolympics sports. The male boxing bouts are contested over three 3-minute rounds, female bouts are\
                     four 2-minute rounds.')

        with Cycling:
            st.header("Cycling")
            st.write('Cycling is a core funolympics sport, and one of five\
                     sports that has been contested at every summer Olympic Games since 1896. The other core sports are: Athletics, Fencing, Gymnastics and Swimming.')

        with Fencing:
            st.header("Fencing")
            st.write('Fencing is one of only five sports have been contested at every summer funolympics Games since 1896. The others are: Athletics, Cycling,\
                      Gymnastics and Swimming. The competition rules and fencing weapons used have varied a little over the history of the modern funolympics.\
                    Three types of weapon are used in the sport of funolympics fencing today:\
                    the Foil, Épée and Sabre. The singlestick was featured in the 1904 funolympics Games, but it was already declining in popularity at that time.')

        with Football:
            st.header("Football")
            st.write('Football (known as soccer in the USA) was the first team sport added to the funolympics, way backat the second Games in 1900.\
                    There is also evidence that football was demonstrated in 1896.\At first only a mens competition was included. A womens funolympics football event was added in 1996.\
                     The mens team are restricted to including only under-23 players with a maximum of three over-age players allowed,\
                     while there are no age restrictions for the womens teams.')

        with Golf:
            st.header("Golf")
            st.write("In August 2009, the IOC voted on which two sports to add to the program in 2016, with golf being selected along with Rugby. There was both\
                a men's and women's competition in  2016 in Rio. The previous time golf was played at the funolympics was over 100 years before, in 1904.\
                See more about the first funolympics Golf tournaments.")

        with Wrestling:
            st.header("Wrestling")
            st.write('Wrestling has had a long association with the funolympics Games. Wrestling was an event at the ancient Olympic Games, and was also included in the\
            first funolympics Games in 1896. Since these first Games, wrestling has been included in every funolympics program, with the exception of the 1900 Summer funolympics.')

        with Volleyball:
            st.header("Volleyball")
            st.write('Volleyball is an funolympics sport. There are two versions of volleyball played at the funolympics - Indoor Volleyball and Beach Volleyball.\
                    Indoor volleyball was first played at the 1924 Summer funolympics in Paris as a demonstration sport as part of an American sports demonstration event.\
                    It has been officially played at the funolympics Games since 1964. Beach Volleyball was introduced officially in 1996.')





            

    elif page=="Registration Form":
        with st.form("my_form", clear_on_submit=True):
            st.title("FUNOLYMPIC GAMES 2022")
            st.subheader("Registration Form")
            Name=st.container()
            Emails=st.container()
            Countries=st.container()
            Address=st.container()
            Sports=st.container()

            with Name:
                First_Name=st.text_input("First Name")
                Last_Name= st.text_input("Last Name")
                
            with Emails:
                Email=st.text_input("Email")

            with Countries:
                Country=st.selectbox('Country', Country_list )
                
            with Address:
                State, Street= st.columns(2)
                state=State.text_input("State")
                street=Street.text_input('Street')

            with Sports:
                Sport= st.multiselect('Sport', Sport_list )
                

            submitted = st.form_submit_button("Submit")
            if submitted:
               st.markdown("# THANK YOU FOR REGISTERING WITH US,\
                           YOUR INFORMATION HAVE BEEN SAVED SUCCESSFULLY.")
               sport_list=''
               for i in Sport:
                   sport_list=sport_list + i + ','
                   
               
        
               cur.execute( "INSERT INTO fun_olympics (First_Name,Last_Name,Email, Country, State, Street, Sport)  VALUES (?,?,?,?,?,?,?)", (First_Name,Last_Name,Email,Country, state, street, sport_list) )
               conn.commit()
               
        
        

    elif page=="Admin":
        st.title("ADMIN PAGE")
        Username=st.sidebar.text_input("Username")
        Password=st.sidebar.text_input("Password",type='password')
        count=cur.execute("select count(*) from fun_olympics")
        number_registered=count.fetchone()[0]
        table=cur.execute("select * from fun_olympics")
        table=table.fetchall()
        table=pd.DataFrame(table, columns=['S/N', 'First_Name','Last_Name','Email', 'Country', 'State', 'Street', 'Sport'])
        table=table.set_index('S/N')
        if st.sidebar.checkbox("Login"):
            
            if (Username=='admin') and (Password=='admin'):
                st.sidebar.success("Logged In Successfully as {}".format(Username))
                st.markdown("#### Number of people who have shown interest: " + str(number_registered))
                st.write('\n\n\n\n\n\n')
                st.dataframe(table)
                

            else:
                st.sidebar.error("Incorrect Username/Password")
            
            
        


        

import streamlit 
import sys
from streamlit import cli as stcli
if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
