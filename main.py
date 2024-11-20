# Press the green button in the gutter to run the script.

from map_utils_xethhung12.GoogleMap import extrac_saved_places, Trip

if __name__ == '__main__':
    save_places= extrac_saved_places("https://maps.app.goo.gl/9R6zt8hqCzpt5Jw36")
    trip=Trip(save_places)
    print(trip.output_yaml())
    print(save_places)


    # for x in re.split("[{|}]", text):
    #     print(x)

    # txt = x.text.split(r")]}'\n")[2].split("]]\"],")[0] + "]]"
    # txt = html.unescape(txt)
    #
    # results = re.findall(r"\[null,null,[0-9]{1,2}\.[0-9]{4,15},[0-9]{1,2}\.[0-9]{4,15}]", txt)
    #
    # for cord in results:
    #     curr = txt.split(cord)[1].split("\\\"]]")[0]
    #     curr = curr[curr.rindex("\\\"") + 2:]
    #
    #     cords = str(cord).split(",")
    #     lat = cords[2]
    #     lon = cords[3][:-1]
    #
    #     print("Name: " + curr)
    #     print("Coords: " + lat + ", " + lon + "\n")


