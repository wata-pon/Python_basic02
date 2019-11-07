def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    sum_temper = 0
    for temper in weather_information:
        sum_temper += temper['temperature']
    print(f'{sum_temper / len(weather_information)}')

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_stations = []  # list()または[]でリスト作成
    for osaka_station in range(0, len(weather_information)):  # range関数について
        if weather_information[osaka_station]['prefecture'] == '大阪府':
            osaka_stations.append(weather_information[osaka_station]["station"])
    print(f'{",".join(osaka_stations)}')  # " ".join(リスト)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    temp_sum_fukuoka = []
    for list_num in range(0, len(weather_information)):
        if weather_information[list_num]['prefecture'] == '福岡県':
            temp_sum_fukuoka.append(weather_information[list_num]['temperature'])
    average_temp_fukuoka = sum(temp_sum_fukuoka) / len(temp_sum_fukuoka)
    print(f'平均気温 : {average_temp_fukuoka} 度')

    # わからないので、とりあえずみんなの回答を参考にした


if __name__ == '__main__':
    main()
