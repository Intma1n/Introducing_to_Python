from abc import ABC, abstractmethod


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источник света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class LightProcessor:
    @abstractmethod
    def lighten(self, map):
        pass


class LightCounterAdapter(LightProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, map):
        pass


def main():
    my_dim = [5, 5]
    my_obstacles = []
    my_lights = []

    light = Light(my_dim)

    light.set_lights(my_dim[1])
    light.set_obstacles(my_dim[1])
    print(light.generate_lights())


if __name__ == '__main__':
    main()
