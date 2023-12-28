import map_utils_xethhung12

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # # response = requests.get("https://saibara.sakura.ne.jp/map/convgeo.cgi")
    # # resp_text = response.text.encode("utf-8")
    # text = "t=freewgsdeg&freewgsdeg=https%3A%2F%2Fwww.google.co.jp%2Fmaps%2F%4035.6782389%2C139.7534472%2C18z&freewgsdms=35%C2%B040%2741.66N%2F139%C2%B045%2712.41E&wgs_lat=35.6782389&wgs_lon=139.7534472&wgs_lat_degree=35&wgs_lat_min=40&wgs_lat_sec=41.66&wgs_lon_degree=139&wgs_lon_min=45&wgs_lon_sec=12.41&freejpndeg=http%3A%2F%2Fwww.mapion.co.jp%2Fm%2F35.675001_139.756666_10%2F&freejpndms=35%C2%B040%2730.00N%2F139%C2%B045%2724.00E&jpn_lat=35.6750012&jpn_lon=139.7566659&jpn_lat_degree=35&jpn_lat_min=40&jpn_lat_sec=30.00&jpn_lon_degree=139&jpn_lon_min=45&jpn_lon_sec=24.00&olc=8Q7XMQH3%2B79WF&mapcode=645+023*77&lpa=SD9.XC4.XV2.GT2&geopo=Z4RP7EhQ"
    # formatData={}
    # for kv in  [
    #     {
    #     "key": kv[0],
    #     "value": kv[1] if len(kv) == 2 else 'unknown'
    #    }
    #     for pair in text.split("&")
    #     for kv in [pair.split("=")]
    # ]:
    #     # print("KV",kv)
    #     formatData.update({kv['key']: kv['value']})
    #
    # HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    # formatData.update({"freewgsdeg":"https://www.google.com/maps/@33.602595293647155,130.4207145388183"})
    #
    # response = requests.post("https://saibara.sakura.ne.jp/map/convgeo.cgi", data=formatData, headers=HEADERS)
    # data = response.text
    # soup = BeautifulSoup(data, "html.parser")
    # values = soup.select("input[type='text'][name='mapcode']")
    # if len(values) == 1:
    #     print(values[0].get("value"))
    # else:
    #     raise Exception("no mapcodes found: ",values)

    # print(
    #     map_utils_xethhung12.DensoMapCode.from_google_map_link(
    #         "https://www.google.com/maps/@33.602595293647155,130.4207145388183")
    # )

    print(
        map_utils_xethhung12.GoogleMap.get_real_url("https://maps.app.goo.gl/wKzFwJzZPwLikbwGA")
    )
