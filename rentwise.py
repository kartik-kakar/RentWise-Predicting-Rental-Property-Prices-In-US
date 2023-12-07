import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pickle
import json
from custom_transform_module import custom_transform
from PIL import Image

# Load the model
model = pickle.load(open('US_rental_property_price_predictor_model.pkl', 'rb'))



# Load the feature columns from JSON file
with open("columns.json", "r") as columns_file:
    columns_dict = json.load(columns_file)

# Extract the feature columns
columns = columns_dict['data_columns']




# Load the scaler
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)



# Load X_train
with open("X_train.pkl", "rb") as X_train_file:
    X_train = pickle.load(X_train_file)





# Sidebar content
def sidebar_content():


    st.sidebar.title("Navigation")
    pages = ["RentWise  🏘", "Make Predictions 💡", "Project Overview 🎯"]
    if "page_selection" not  in st.session_state:
        st.session_state.page_selection = pages[0]
    st.session_state.page_selection = st.sidebar.radio("Go to", pages,index=pages.index(st.session_state.page_selection))
    
    st.sidebar.subheader("Contact Me")
    st.sidebar.info('**Repo: [This Project](https://github.com/kartik-kakar/RentWise-Predicting-Rental-Property-Prices-In-US)**', icon="💡")

    st.sidebar.info('**My GitHub: [@kartik-kakar](https://github.com/kartik-kakar)**', icon="💻")
    st.sidebar.info('**My LinkedIn: [kartik--kakar](https://www.linkedin.com/in/kartik--kakar/)**', icon="🧠")
    
    image = Image.open('qr_code.png')

    st.sidebar.image(image, caption='Scan Me !!!',width=150) 


# The website information

st.set_page_config(page_title="RentWise")

# Define the first page
def landing_page():
    # Add background image to the entire app
    st.markdown(
    """
    <style>
    .main {
        background: url("https://getwallpapers.com/wallpaper/full/9/1/6/101497.jpg");
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        text-color: white;
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
    )


    # Header
    st.markdown("<h1 style='text-align: center;'>RentWise</h1>", unsafe_allow_html=True)
    
    # Add empty space
    st.markdown("&nbsp;")

   # Header
    st.markdown("<h2 style='text-align: center;'>Your Home Search, Simplified!</h2>", unsafe_allow_html=True)

    
    st.markdown("<h5 style='text-align: center;'>Welcome to RentWise, your go-to tool for smarter property valuation.\
                This application leverages machine learning to predict property prices based on \
                various features. Explore property details, make predictions and informed decisions on the\
     real estate market. Let RentWise be your guide to finding the right property at the right price.</h5>", unsafe_allow_html=True)           

    st.markdown("&nbsp;")

    st.markdown("<h5 style='text-align: center;'>Let's get started.</h5>", unsafe_allow_html=True)
    col_num = 9
    c1,c2,c3,c4,c5,c6,c7,c8,c9 = st.columns([0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1,0.1])
    with c5:

        st.button("Demo",on_click=demo_btn(), type='primary',use_container_width=True)

def demo_btn():
    st.session_state.page_selection = "Make Predictions 💡"
    



# Define the third page
def project_overview():
    # Add background image to the entire app
    st.markdown(
    """
    <style>
    .main {
        background: url(https://getwallpapers.com/wallpaper/full/9/1/6/101497.jpg);
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        text-color: white;
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    
    # Header
    st.markdown("<h1 style='text-align: center;'>Project Overview</h1>", unsafe_allow_html=True)

    # Overview
    st.subheader("**Introduction** 🏠")
    # Description
    st.markdown("RentWise is your gateway to understanding and predicting rental property prices in the United States. "
                "Our data-driven approach, incorporating various Data Science techniques like Exploratory Data Analysis, Feature Engineering and Machine Learning, "
                "unveils the intricate dynamics of rental housing prices. The goal is to provide accurate price estimates, "
                "offering invaluable insights for renters, landlords, and the real estate industry.\n\n"
                "This tool, powered by machine learning, predicts property prices based on various features. Whether you're a buyer, "
                "seller, or investor, explore property details, make predictions, and make informed decisions with RentWise as your guide.")
    

    st.subheader("**Main Questions 🤔**")
    # Description
    st.markdown("- What are the primary factors influencing rental property prices in different regions of the United States?\n\n"
                "- Can we construct a dependable predictive model to accurately forecast rental prices based on property features and amenities?\n\n"
                "- Who can benefit from the insights provided by this project, and how can it be advantageous for different stakeholders in the real estate market?"
                )


    st.subheader("**Roadmap** 🚀")
    # Description
    st.markdown("**1. Data Cleaning** 🧹")
    st.markdown("Our journey begins with cleaning the raw dataset, ensuring it's polished for analysis. We bid farewell to unnecessary columns and addressed pesky 'NaN' values. The result? A pristine dataset ready for the next steps")
    
    st.markdown("**2 .Exploratory Data Analysis (EDA)** 🕵️‍♂️")
    st.markdown("Time to play detective! We delved into the dataset's secrets, unveiling its characteristics, relationships, and patterns. Visualizations and stats took the spotlight, guiding us in model selection and feature engineering. Outliers got the boot for a dose of reality, and our modified dataset was saved for later.")

    st.markdown("**3. Feature Engineering and Baseline Modeling** 🧠")
    st.markdown("Enter the brainy phase. We transformed data, turning categorical columns into numerical wizards. Test and train sets were prepared for the big show, where models like Linear Regression, Decision Trees, and the cool Random Forest stepped onto the stage. Scaling the dataset brought fairness to the comparison, with R2 and MSE metrics as our judges.")
    
    st.markdown("**4. Hyperparameter Tuning and Evaluation** 📊")
    st.markdown("The star of the show emerged: Random Forest Regressor. With consistently high predictive accuracy, we fine-tuned its performance. Hyperparameters got their makeover, and voila! We found the winning combo. The model strutted its stuff on the entire dataset, leaving us with some intriguing predictions.")


    st.subheader("**Learnings and Conclusion** 📝 ")
    st.markdown("In conclusion, this project marks a significant stride in leveraging data science to understand and predict rental property prices. Through meticulous data cleaning, exploratory data analysis, and the development of a robust predictive model, we've gained insights into the intricate factors influencing rental prices. The application of machine learning techniques not only enhances our understanding of real estate dynamics but also provides a valuable tool for both renters and landlords to make informed decisions. This project underscores the power of data-driven approaches in addressing complex challenges and fostering a more transparent and efficient real estate market.")


                
# Define the second page
def make_predictions():
    # Add background image to the entire app
    st.markdown(
    """
    <style>
    .main {
        background: url("https://getwallpapers.com/wallpaper/full/9/1/6/101497.jpg");
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        text-color: white;
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Header
    st.markdown("<h1 style='text-align: center;'>Make Predictions with RentWise!</h1>", unsafe_allow_html=True)

    st.markdown("&nbsp;")

    st.subheader("Property Details")

    c1, c2, c3 = st.columns([0.5,0.5,0.5])
    with c1:
        state = st.selectbox("**State**", ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]) 
    with c2:
        region = st.selectbox("**Region**", ['reno / tahoe',
        'sacramento',
        'boulder',
        'visalia-tulare',
        'santa barbara',
        'SF bay area',
        'siskiyou county',
        'ventura county',
        'san diego',
        'san luis obispo',
        'stockton',
        'santa maria',
        'susanville',
        'colorado springs',
        'yuba-sutter',
        'denver',
        'northwest CT',
        'fort collins / north CO',
        'western slope',
        'eastern CT',
        'hartford',
        'new haven',
        'washington, DC',
        'high rockies',
        'pueblo',
        'daytona beach',
        'ft myers / SW florida',
        'gainesville',
        'jacksonville',
        'ocala',
        'eastern CO',
        'heartland florida',
        'delaware',
        'lakeland',
        'florida keys',
        'north central FL',
        'orlando',
        'panama city',
        'pensacola',
        'sarasota-bradenton',
        'south florida',
        'okaloosa / walton',
        'space coast',
        'tallahassee',
        'tampa bay area',
        'atlanta',
        'augusta',
        'brunswick',
        'athens',
        'treasure coast',
        'albany',
        'st augustine',
        'macon / warner robins',
        'columbus',
        'northwest GA',
        'savannah / hinesville',
        'hawaii',
        'boise',
        'east idaho',
        'statesboro',
        "spokane / coeur d'alene",
        'valdosta',
        'bloomington-normal',
        'champaign urbana',
        'chicago',
        'twin falls',
        'decatur',
        'la salle co',
        'quad cities, IA/IL',
        'st louis, MO',
        'peoria',
        'evansville',
        'springfield',
        'bloomington',
        'lewiston / clarkston',
        'pullman / moscow',
        'indianapolis',
        'fort wayne',
        'rockford',
        'south bend / michiana',
        'ames',
        'richmond',
        'southern illinois',
        'mattoon-charleston',
        'muncie / anderson',
        'western IL',
        'lafayette / west lafayette',
        'kokomo',
        'terre haute',
        'cedar rapids',
        'des moines',
        'omaha / council bluffs',
        'wichita',
        'fort dodge',
        'lawrence',
        'salina',
        'sioux city',
        'bowling green',
        'lexington',
        'eastern kentucky',
        'iowa city',
        'louisville',
        'dubuque',
        'baton rouge',
        'waterloo / cedar falls',
        'manhattan',
        'western KY',
        'lafayette',
        'monroe',
        'mason city',
        'new orleans',
        'kansas city, MO',
        'southeast IA',
        'topeka',
        'lake charles',
        'southeast KS',
        'huntington-ashland',
        'northwest KS',
        'southwest KS',
        'shreveport',
        'central louisiana',
        'houma',
        'owensboro',
        'maine',
        'lansing',
        'annapolis',
        'baltimore',
        'frederick',
        'southern maryland',
        'boston',
        'south coast',
        'western massachusetts',
        'worcester / central MA',
        'western maryland',
        'ann arbor',
        'battle creek',
        'detroit metro',
        'holland',
        'cumberland valley',
        'flint',
        'kalamazoo',
        'muskegon',
        'saginaw-midland-baycity',
        'upper peninsula',
        'eastern shore',
        'cape cod / islands',
        'grand rapids',
        'bemidji',
        'central michigan',
        'northern michigan',
        'jackson',
        'southwest michigan',
        'the thumb',
        'port huron',
        'brainerd',
        'duluth / superior',
        'fargo / moorhead',
        'minneapolis / st paul',
        'rochester',
        'gulfport / biloxi',
        'st cloud',
        'hattiesburg',
        'asheville',
        'north mississippi',
        'joplin',
        'kirksville',
        'mankato',
        'southwest MS',
        'columbia / jeff city',
        'southwest MN',
        'st joseph',
        'charlotte',
        'boone',
        'billings',
        'missoula',
        'fayetteville',
        'eastern NC',
        'greensboro',
        'raleigh / durham / CH',
        'hickory / lenoir',
        'lake of the ozarks',
        'meridian',
        'southeast missouri',
        'kansas city',
        'st louis',
        'bozeman',
        'eastern montana',
        'kalispell',
        'great falls',
        'helena',
        'butte',
        'outer banks',
        'wilmington',
        'winston-salem',
        'lincoln',
        'las vegas',
        'north platte',
        'central NJ',
        'north jersey',
        'jersey shore',
        'south jersey',
        'albuquerque',
        'buffalo',
        'ithaca',
        'farmington',
        'long island',
        'hudson valley',
        'syracuse',
        'plattsburgh-adirondacks',
        'catskills',
        'watertown',
        'grand island',
        'santa fe / taos',
        'scottsbluff / panhandle',
        'new york city',
        'binghamton',
        'utica-rome-oneida',
        'new hampshire',
        'elko',
        'clovis / portales',
        'finger lakes',
        'chautauqua',
        'elmira-corning',
        'las cruces',
        'roswell / carlsbad',
        'glens falls',
        'oneonta',
        'potsdam-canton-massena',
        'twin tiers NY/PA',
        'cincinnati',
        'north dakota',
        'akron / canton',
        'bismarck',
        'grand forks',
        'dayton / springfield',
        'cleveland',
        'lima / findlay',
        'toledo',
        'northern panhandle',
        'oklahoma city',
        'zanesville / cambridge',
        'ashtabula',
        'lawton',
        'chillicothe',
        'texoma',
        'tulsa',
        'bend',
        'corvallis/albany',
        'tuscarawas co',
        'east oregon',
        'eugene',
        'medford-ashland',
        'oregon coast',
        'portland',
        'mansfield',
        'stillwater',
        'parkersburg-marietta',
        'northwest OK',
        'sandusky',
        'youngstown',
        'fort smith, AR',
        'klamath falls',
        'salem',
        'roseburg',
        'harrisburg',
        'philadelphia',
        'erie',
        'pittsburgh',
        'lehigh valley',
        'rhode island',
        'scranton / wilkes-barre',
        'altoona-johnstown',
        'reading',
        'charleston',
        'williamsport',
        'lancaster',
        'state college',
        'columbia',
        'greenville / upstate',
        'myrtle beach',
        'hilton head',
        'chattanooga',
        'poconos',
        'clarksville',
        'meadville',
        'south dakota',
        'cookeville',
        'york',
        'sioux falls / SE SD',
        'florence',
        'northeast SD',
        'rapid city / west SD',
        'pierre / central SD',
        'memphis',
        'knoxville',
        'nashville',
        'amarillo',
        'austin',
        'college station',
        'lubbock',
        'dallas / fort worth',
        'abilene',
        'el paso',
        'corpus christi',
        'del rio / eagle pass',
        'galveston',
        'houston',
        'killeen / temple / ft hood',
        'laredo',
        'mcallen / edinburg',
        'tri-cities',
        'brownsville',
        'beaumont / port arthur',
        'deep east texas',
        'odessa / midland',
        'waco',
        'san antonio',
        'san angelo',
        'san marcos',
        'tyler / east TX',
        'victoria',
        'wichita falls',
        'provo / orem',
        'ogden-clearfield',
        'salt lake city',
        'fredericksburg',
        'charlottesville',
        'lynchburg',
        'norfolk / hampton roads',
        'roanoke',
        'winchester',
        'texarkana',
        'southwest TX',
        'vermont',
        'logan',
        'st george',
        'danville',
        'harrisonburg',
        'new river valley',
        'southwest VA',
        'bellingham',
        'kennewick-pasco-richland',
        'seattle-tacoma',
        'moses lake',
        'olympic peninsula',
        'yakima',
        'morgantown',
        'madison',
        'wenatchee',
        'skagit / island / SJI',
        'milwaukee',
        'west virginia (old)',
        'wausau',
        'janesville',
        'kenosha-racine',
        'eastern panhandle',
        'southern WV',
        'green bay',
        'la crosse',
        'wyoming',
        'appleton-oshkosh-FDL',
        'eau claire',
        'sheboygan',
        'northern WI',
        'auburn',
        'birmingham',
        'phoenix',
        'gadsden-anniston',
        'huntsville / decatur',
        'dothan',
        'mobile',
        'montgomery',
        'florence / muscle shoals',
        'tuscaloosa',
        'anchorage / mat-su',
        'fairbanks',
        'flagstaff / sedona',
        'tucson',
        'little rock',
        'prescott',
        'yuma',
        'bakersfield',
        'fresno / madera',
        'hanford-corcoran',
        'humboldt county',
        'inland empire',
        'los angeles',
        'kenai peninsula',
        'southeast alaska',
        'mohave county',
        'fort smith',
        'jonesboro',
        'show low',
        'gold country',
        'sierra vista',
        'chico',
        'imperial county',
        'modesto',
        'orange county',
        'mendocino county',
        'merced',
        'palm springs',
        'monterey bay',
        'redding'])
    with c3:
        property_type = st.selectbox("**Type**", ['apartment',
        'condo',
        'house',
        'duplex',
        'townhouse',
        'loft',
        'manufactured',
        'cottage/cabin',
        'flat',
        'in-law',
        'assisted living',
        'land']) 
    
    c1, c2 = st.columns([0.5,0.5])
    with c1:
        laundry = st.selectbox("**Laundry**", ['w/d in unit',
        'w/d hookups',
        'laundry on site',
        'laundry in bldg',
        'no laundry on site']) 
    
    with c2:
        parking = st.selectbox("**Parking**", ['carport',
        'attached garage',
        'off-street parking',
        'detached garage',
        'street parking',
        'no parking',
        'valet parking'])  


    c1, c2, c3= st.columns([0.5,0.5,0.5])
    with c1:
        sq_feet = st.number_input("**Square Feet**", min_value=0)
    
    with c2:
        beds = st.number_input("**Beds**", min_value=0)

    with c3:
        baths = st.number_input("**Baths**", min_value=0)
 
    c1, c2, c3 = st.columns(3)
    with c1:
        cats = st.checkbox("**Cats Allowed**")
    
    with c2:
        dogs = st.checkbox("**Dogs Allowed**")

    with c3:
        smoking = st.checkbox("**Smoking Allowed**")
    

    c4, c5, c6 = st.columns(3)
    with c4:
        wheelchair_access = st.checkbox("**Wheelchair Accessible**")

    with c5:
        ev_charge = st.checkbox("**Electric Vehicle Charging**")

    with c6:
        furnished = st.checkbox("**Comes Furnished**")


    # Button to trigger predictions
    if st.button("Make Predictions"):
        

        user_inputs = pd.DataFrame({
            "region": [region],
            "type": [property_type],
            "sqfeet": [sq_feet],
            "beds": [beds],
            "baths": [baths],
            "cats_allowed": [1 if cats else 0],
            "dogs_allowed": [1 if dogs else 0],
            "smoking_allowed": [1 if smoking else 0],
            "wheelchair_access": [1 if wheelchair_access else 0],
            "electric_vehicle_charge": [1 if ev_charge else 0],
            "comes_furnished": [1 if furnished else 0],
            "laundry_options": [laundry],
            "parking_options": [parking],
            "state": [state]
        })

        # Transform the user inputs using custom_transform
        transformed_inputs = custom_transform(user_inputs, X_train, scaler)

        # Make prediction
        prediction = model.predict(transformed_inputs)

        


    # Display the predicted price without a box
        st.markdown(
            f"<h4 style='color: #333333;'>Predicted Price: ${prediction[0]:,.2f}</h4>",
            unsafe_allow_html=True
        )


    # Add empty space
    st.markdown("&nbsp;")


# Create a function to handle page routing
def main():
    # page = 
    sidebar_content()

    if st.session_state.page_selection == "RentWise  🏘":
        landing_page()
    elif st.session_state.page_selection == "Project Overview 🎯":
        project_overview()
    elif st.session_state.page_selection == "Make Predictions 💡":
        make_predictions()

# Run the app
main()
