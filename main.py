import getstation

class Node:

    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes=None):
        self.adj_mat = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    def add_edge(self, node1, node2, weight=1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight
        self.adj_mat[node2][node1] = weight

    def connection_edges(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if
                self.adj_mat[node][col_num] != 0]

    def print_adj_mat(self):
        for row in self.adj_mat:
            print(row)

    def node(self, index):
        return self.nodes[index]

    def get_node_by_name(self, node_name):
        return next((x for x in self.nodes if x.data == node_name), None)

    def get_index_by_name(self, node_name):
        return next((x for x in self.nodes if x.data == node_name), None).index

    def get_index_from_node(self, node):
        if isinstance(node, int):
            return node
        else:
            return node.index

    def dijkstra(self, node, dest):
        nodenum = self.get_index_by_name(node)
        destnum = self.get_index_by_name(dest)
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")]
            dist[i].append([self.nodes[nodenum]])
        dist[nodenum][0] = 0
        queue = [i for i in range(len(self.nodes))]
        seen = set()
        while len(queue) > 0:
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
            queue.remove(min_node)
            seen.add(min_node)
            if min_node == destnum:
                break
            connections = self.connection_edges(min_node)
            for (node, weight) in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[node.index][0]:
                    dist[node.index][0] = tot_dist
                    dist[node.index][1] = list(dist[min_node][1])
                    dist[node.index][1].append(node)
        return dist[destnum]


station_nodes = [Node(a) for a in getstation.get_stations_nodes()] # Создаем узлы
metro_graph = Graph.create_from_nodes(station_nodes) # Создаем графы
# Создаем связи между графами
for stat in getstation.stations_time:
    metro_graph.add_edge(metro_graph.get_node_by_name(stat[0]), metro_graph.get_node_by_name(stat[1]), stat[2])

short = metro_graph.dijkstra("Ленинский проспект", "Парнас")
print(short[0], [node.data for node in short[1]])
