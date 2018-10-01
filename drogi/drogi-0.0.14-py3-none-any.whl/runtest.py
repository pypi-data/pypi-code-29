import drogi
import datetime

cities = ["Warszawa",
          "Krakow",
          "Lodz",
          "Wroclaw",
          "Poznan",
          "Gdansk",
          "Szczecin",
          "Bydgoszcz",
          "Lublin",
          "Bialystok",
          ]

populations = BOUNDS_DICT = {
    "Warszawa": 1758143,
    "Krakow": 766739,
    "Lodz": 693797,
    "Wroclaw": 638364,
    "Poznan": 539545,
    "Gdansk": 464293,
    "Szczecin": 404403,
    "Bydgoszcz":353215,
    "Lublin": 340230,
    "Bialystok": 297288,
}

for city in cities:
    print(city)
    population = populations[city]
    num_of_trips = 200
    run = drogi.WorkRun(city, num_of_trips=num_of_trips)
    canvas = drogi.Canvas(run.way_map.bounds_to_fetch)
    run.way_map.render_on_canvas(canvas,
                                 color="black",
                                 aa=True,
                                 linewidth=0.5,
                                 alpha=0.5)
    for trip in run.list_of_trips:
        dev_factor = trip.path.deviation_factor
        trip.path.render_on_canvas(canvas,
                                   color="blue",
                                   aa=False,
                                   linewidth=0.7,
                                   alpha=100/num_of_trips)
        for obstacle in trip.path.obstacles:
            obstacle.render_on_canvas(canvas,
                                      color="red",
                                      alpha=((dev_factor / 1) * 200 / num_of_trips),
                                      linewidth=0,
                                      edgecolor=None)
    curr_time = str(datetime.datetime.utcnow()).replace(" ", "_")
    canvas.save(city + curr_time + ".png", dpi=150)
    break