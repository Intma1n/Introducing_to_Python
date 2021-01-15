from abc import ABC, abstractmethod


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источник света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        lightmap = light_mapper.lighten(self.map)
        return lightmap


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
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
    def lighten(self, my_map):
        pass


class MappingAdapter(LightProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, my_map):
        dim = tuple(input('Enter dim:'))
        obstacles = []
        lights = []
        my_grid = [[0 for i in range(int(dim[0]))] for _ in range(int(dim[1]))]
        for i in range(len(my_map)):
            for j in range(len(my_map[i])):
                if my_map[i][j] == 1:
                    lights.append([i, j])
                if my_map[i][j] == -1:
                    obstacles.append([i, j])
                if my_map[i][j] == 0:
                    my_map[i][j] = 's'
        print(my_map.copy(), lights.copy(), obstacles.copy(), my_grid.copy())



def main():
    dim = [5, 5]
    system = System()
    light = Light(dim)
    light_adapter = MappingAdapter(light)
    print(system.get_lightening(light_adapter))


if __name__ == '__main__':
    main()
