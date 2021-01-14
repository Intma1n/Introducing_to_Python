from abc import ABC, abstractmethod


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  #Источник света
        self.map[5][2] = -1  #Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range (dim[0])] for _ in range (dim[1])]

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
    def process_light(self, dim, lights, obstacles):
        pass


class LightCounterAdapter(LightProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, map):
        pass


def main():
    system = System()
    system.get_lightening()


if __name__ == '__main__':
    main()