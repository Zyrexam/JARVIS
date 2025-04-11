import os

def Phonenumber_location_tracker():
    import datetime
    import phonenumbers
    from phonenumbers import geocoder
    import folium
    from phonenumbers import carrier
    from opencage.geocoder import OpenCageGeocode

    current_path = os.getcwd()
    
    num = input("Enter a number with country code (+91...): ")
    time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    API_key = "_OPEN_CAGE_GEOCODE_API_KEY_"
    
    #     # Read API key from Environment Variable
    # API_key = os.getenv("OPENCAGE_API_KEY")
    # if not API_key:
    #     print("API key not found in environment variables!")
    #     return


    sanNumber = phonenumbers.parse(num)

    # Country Location
    location = geocoder.description_for_number(sanNumber, "en")

    # Service Provider
    service_provider = carrier.name_for_number(sanNumber, 'en')

    # Latitude & Longitude
    geocode = OpenCageGeocode(API_key)
    query = str(location)
    result = geocode.geocode(query)

    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    # Create Maps Directory if not exists
    map_dir = os.path.join(current_path, "Maps")
    os.makedirs(map_dir, exist_ok=True)

    # Create Map
    mymap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)

    filename = f"{num}-{time_}.html"
    map_path = os.path.join(map_dir, filename)
    mymap.save(map_path)

    print(f"[+] Location  : {location}")
    print(f"[+] Provider  : {service_provider}")
    print(f"[+] Latitude  : {lat}")
    print(f"[+] Longitude : {lng}")
    print(f"[+] Map saved at : {map_path}")

    return location, service_provider, lat, lng
