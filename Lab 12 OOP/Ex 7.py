class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

weather = Weather(["rain", "sunny", "cloudy", "windy"])
print("rain" in weather)
print("snow" in weather)