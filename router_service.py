class Router:
    def __init__(self):
        self.route_dict = {}

    def add_route(self, route_data, route_function):
        self.route_dict[route_data] = route_function

    def get_route(self, route_data):
        return self.route_dict.get(route_data, "No route specified")


if __name__ == '__main__':
    route = Router()
    route.add_route("/", "Home Page")
    route.add_route("/product", "This is the product page")
    while True:
        route_text = input("Enter the route :")
        if route_text == "exit":
            break
        print(f"The route data is {route.get_route(route_text)}")
