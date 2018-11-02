import sys
import re

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.id = None
        self.neighbors = set()

    def __repr__(self):
        return "P(%d,%d)" % (self.x, self.y)


class Street(object):
    def __init__(self, name, points):
        self.name = name
        self.original_points = points
        self.points = list()
        self.points_pool = set()

    def __repr__(self):
        return "St(%s)" % self.name

    def reset(self):
        self.points = list()
        self.points_pool = set()
        for p in self.original_points:
            self.points.append(p)
            self.points_pool.add((p.x, p.y))


class StreetGraph(object):
    def __init__(self):
        self._streets = dict()
        self.intersections = set()
        self._edges = set()
        self._p2in = dict()
        self._vertices = set()
        self._id_generator = 1

    def reset(self):
        for _, s in self._streets.items():
            s.reset()
        for _, p in self._p2in.items():
            p.neighbors = set()
        self.intersections = set()
        self._edges = set()
        self._vertices = set()

    def add_street(self, name, points):
        if name not in self._streets:
            p_list = list()
            for p in points:
                if (p[0], p[1]) not in self._p2in:
                    tmp = Point(float(p[0]), float(p[1]))
                    tmp.id = self._id_generator
                    self._p2in[(p[0], p[1])] = tmp
                    self._id_generator += 1
                p_list.append(self._p2in[(p[0], p[1])])
            self._streets[name] = Street(name, p_list)
            return 0
        else:
            return -1

    def change_street(self, name, points):
        if name in self._streets:
            self.remove_street(name)
            self.add_street(name, points)
            return 0
        else:
            return -1

    def remove_street(self, name):
        if name in self._streets:
            self._streets.pop(name)
            return 0
        else:
            return -1

    def is_intersected(self, a, b, c, d):
        if (b.y - a.y) * (c.x - d.x) - (b.x - a.x) * (c.y - d.y) == 0:
            return -1

        x = ((b.x - a.x) * (c.x - d.x) * (c.y - a.y) - c.x * (b.x - a.x) * (c.y - d.y) + a.x * (b.y - a.y) * (c.x - d.x)) / ((b.y - a.y) * (c.x - d.x) - (b.x - a.x) * (c.y - d.y))
        y = ((b.y - a.y) * (c.y - d.y) * (c.x - a.x) - c.y * (b.y - a.y) * (c.x - d.x) + a.y * (b.x - a.x) * (c.y - d.y)) / ((b.x - a.x) * (c.y - d.y) - (b.y - a.y) * (c.x - d.x))

        if (x - a.x) * (x - b.x) <= 0 and (x - c.x) * (x - d.x) <= 0 and (y - a.y) * (y - b.y) <= 0 and (y - c.y) * (y - d.y) <= 0:
            if (x, y) in self._p2in:
                return self._p2in[(x, y)]
            else:
                return Point(x, y)
        else:
            return -1

    @staticmethod
    def is_neighbor(a, b):
        return b in a.neighbors

    def generate_graph(self):
        self.reset()
        streets = list()
        for _, street in self._streets.items():
            streets.append(street)
        # generate the vertices
        for i in range(len(streets)):
            for j in range(i + 1, len(streets)):
                a = 0
                while a < len(streets[i].points) - 1:
                    a1 = streets[i].points[a]
                    a2 = streets[i].points[a + 1]
                    b = 0
                    while b < len(streets[j].points) - 1:
                        b1 = streets[j].points[b]
                        b2 = streets[j].points[b + 1]
                        intersection = self.is_intersected(a1, a2, b1, b2)
                        if intersection != -1:
                            if (intersection.x, intersection.y) not in streets[i].points_pool:
                                streets[i].points.insert(a + 1, intersection)
                                streets[i].points_pool.add((intersection.x, intersection.y))
                                a += 1
                            if (intersection.x, intersection.y) not in streets[j].points_pool:
                                streets[j].points.insert(b + 1, intersection)
                                streets[j].points_pool.add((intersection.x, intersection.y))
                                b += 1
                            self.intersections.add((intersection.x, intersection.y))
                            if (intersection.x, intersection.y) not in self._p2in:
                                intersection.id = self._id_generator
                                self._id_generator += 1
                                self._p2in[(intersection.x, intersection.y)] = intersection
                            for p in [a1, a2, b1, b2, intersection]:
                                self._vertices.add((p.x, p.y))
                        b += 1
                    a += 1
        for s in streets:
            s.points[0].neighbors.add(s.points[1])
            s.points[-1].neighbors.add(s.points[-2])
            for i in range(1, len(s.points) - 1):
                s.points[i].neighbors.add(s.points[i - 1])
                s.points[i].neighbors.add(s.points[i + 1])
        # generate the edges
        for (x, y) in self.intersections:
            intersection = self._p2in[(x, y)]
            for _, point in self._p2in.items():
                if intersection is not point and self.is_neighbor(intersection, point) and (intersection.id, point.id) not in self._edges and (point.id, intersection.id) not in self._edges:
                    self._edges.add((intersection.id, point.id))

    def print_graph(self):
        print 'V = {'
        for p in self._vertices:
            print '  %d: (%.2f,%.2f)' % (self._p2in[p].id, p[0], p[1])
        print '}'

        print 'E = {'
        edges = list(self._edges)
        for i in range(len(edges) - 1):
            print '  <%d,%d>,' % (edges[i][0], edges[i][1])
        if len(edges) > 0:
            print '  <%d,%d>' % (edges[-1][0], edges[-1][1])
        print '}'

# TODO: change the parsing about the white spaces

def main():
    graph = StreetGraph()
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        if line[0] not in {'a', 'c', 'r', 'g'}:
            sys.stderr.write('Error: the command must be a, c, r or g\n')
            continue
        if line[0] == 'g':
            if len(line) != 2 or line[1] != '\n':
                sys.stderr.write('Error: command g does not have any parameters\n')
            else:
                graph.generate_graph()
                graph.print_graph()
            continue

        parts = line.split('"')
        if len(parts[0].replace(' ', '')) != 1:
            sys.stderr.write('Error: check the command part\n')
            continue
        if line[0] == 'a' or line[0] == 'c':
            num_part = parts[2].replace(' ', '')
            if len(parts) != 3 or not re.match(r'^\(-?\d+,-?\d+\)(\(-?\d+,-?\d+\))+$', num_part):
                sys.stderr.write('Error: check your input\n')
            else:
                name = parts[1].strip().lower()
                nums = re.findall(r'-?\d+', num_part)
                if len(nums) % 2 != 0:
                    sys.stderr.write('Error: check your input\n')
                    continue
                points = list()
                i = 0
                while i < len(nums):
                    points.append((int(nums[i]), int(nums[i+1])))
                    i += 2
                if line[0] == 'a':
                    if graph.add_street(name, points) == -1:
                        sys.stderr.write('Error: a specified a street that has already existed\n')
                else:
                    if graph.change_street(name, points) == -1:
                        sys.stderr.write('Error: c specified a street that does not exist\n')
        elif line[0] == 'r':
            if len(parts) != 3 or parts[2][0] != '\n':
                sys.stderr.write('Error: check your input\n')
            else:
                name = parts[1].strip().lower()
                if graph.remove_street(name) == -1:
                    sys.stderr.write('Error: r specified a street that does not exist\n')
    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()
