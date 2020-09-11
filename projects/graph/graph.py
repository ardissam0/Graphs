"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create queue
        q = Queue()
        visited = set()

        # add starting value
        q.enqueue(starting_vertex)

        #while q is not empty
        while q.size() > 0:
            #dequeue the vertex
            vertex = q.dequeue()
            #if not visited yet, mark as visited
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for neighbors in self.get_neighbors(vertex):
                    q.enqueue(neighbors)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create stack
        s = Stack()
        #create visited set
        visited = set()

        #prime the stack with starting value
        s.push(starting_vertex) 
        #while stack is not empty
        while s.size() > 0:
            vertex = s.pop()
            #if not visited, mark as visited
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for neighbors in self.get_neighbors(vertex):
                    s.push(neighbors)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create a set for visited
        visited = set()

        # create a function that has the vertex
        # if vertex is in the visited set then keep going
        # otherwise add it to visited
        # loop through neighbor and return neighbor vertex
        def dft(vertex):
            if vertex in visited:
                return
            else:
                visited.add(vertex)
                print(vertex)


            for neighbor in self.get_neighbors(vertex):
                dft(neighbor)


        dft(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        bft_path = Queue()
        # queue.enqueue([starting_vertex])
        bft_path.enqueue([starting_vertex])
        # create a set for visited vertices
        visited = set()
        # while queue is not empty
        while bft_path.size() > 0:
            # dequeue the first Path
            curr_path = bft_path.dequeue()
            # grab the last vertex in the path
            curr_path_last_vertex = curr_path[-1]
            # if it hasnt been visited
            if curr_path_last_vertex not in visited:
                # check if its the target
                if curr_path_last_vertex == destination_vertex:
                    # return the path if it is
                    return curr_path
                # mark it as visited if it is not
                else:
                    visited.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
                # make new versions of the the current path with each neighbor added to them
                    for neighbor in neighbors:
                        # duplicate the path
                        curr_path_copy = curr_path[:]
                        # add the neighbor
                        curr_path_copy.append(neighbor)
                        # add the new path
                        bft_path.enqueue(curr_path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack
        dfs_path = Stack()
        # path to starting vertex
        dfs_path.push([starting_vertex])
        # set for visited vetices
        visited_vertices = set()
        # while path is not empty
        while dfs_path.size() > 0:
            # pop the first path
            curr_path = dfs_path.pop()
            # take last vertex in path
            curr_path_last_vertex = curr_path[-1]
            # if we havent been there yet
            if curr_path_last_vertex not in visited_vertices:
                # check if current is the destination
                if curr_path_last_vertex == destination_vertex:
                    # return the path if it is
                    return curr_path
                # mark as visited if it is not
                else:
                    # get the neighbors / make new versions on the path
                    visited_vertices.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
                    for neighbor in neighbors:
                        # duplicate the path
                        curr_path_copy = curr_path[:]
                        # add the neighbor
                        curr_path_copy.append(neighbor)
                        # add the new path
                        dfs_path.push(curr_path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create visited set
        visited = set()

        # create function with path
        # define last path
        # if last path is in visited then return none
        # otherwise add last path to visited
        # if the last path is equal to the destination vertex then return that path
        # loop through neighbor and find the next path
        # define found
        # if found then return it
        def dfs(path):
            last_path = path[-1]

            if last_path in visited:
                return None

            else:
                visited.add(last_path)

            if last_path == destination_vertex:
                return path

            for neighbor in self.get_neighbors(last_path):
                next_path = path[:]
                next_path.append(neighbor)

                found = dfs(next_path)

                if found:
                    return found

            return None

        return dfs([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
