### Fungsi-fungsi tambahan ###
def add_vertice(graph, vertice_name):
    # Menambahkan simpul baru pada graph
    # Jika nama simpul sudah ada, akan mengeluarkan pesan
    if (vertice_name not in graph):
        graph[vertice_name] = []
    else:
        print("Sudah ada simpul " + vertice_name + " pada graph")

def add_edge(graph, from_vertice, to_vertice):
    # Menambahkan edge baru pada graph
    # Jika tidak ada simpul bernama from_vertice atau to_vertice pada graph,
    # akan mengeluarkan pesan
    if ((from_vertice in graph) and (to_vertice in graph)):
        graph[from_vertice].append(to_vertice)
    else:
        print("Tidak ada simpul " + from_vertice + " atau " + to_vertice + " pada graph")

def delete_vertice(graph, vertices):
    # Menghapus simpul beserta busur yang keluar dari simpul tersebut dari graph.
    # Vertices berupa array berisi nama simpul
    # Jika simpul yang ingin di hapus tidak ada pada graph,
    # akan mengeluarkan pesan.
    for vertice in vertices:
        if (vertice in graph):
            graph.pop(vertice)
        else:
            print("Tidak ada simpul " + vertice + " pada graph")

def get_graph(fileName) :
    # Mengembalikan graph yang terbentuk dari file fileName.
    # Graph yang dibentuk merupakan representasi adjacency list.
    # Dalam python memanfaatkan dictionary.
    # Contoh: isi file.txt: 
    # C1, C3.
    # C2, C1, C4.
    # C3.
    # C4, C1, C3.
    # C5, C2, C4.
    # Maka akan mengembalikan:
    # {
    # 'C1': ['C2', 'C4'], 
    # 'C2': ['C5'], 
    # 'C3': ['C1', 'C4'], 
    # 'C4': ['C2', 'C5'], 
    # 'C5': []
    # }
    f = open("../test/" + fileName, "r")
    problem = []
    for line in f :
        line = line.replace(".", "")
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")
        problem.append(line)
    f.close()

    graph = {}
    for vertices in problem:
        add_vertice(graph, vertices[0])

    for vertices in problem:
        for i in range(1, len(vertices)):
            add_edge(graph, vertices[i], vertices[0])
    
    return graph

def get_zero_in_degree_vertices(graph):
    # # Mengembalikan array simpul-simpul yang
    # memiliki in-degree 0
    # Contoh: graph = 
    # {
    # 'C2': ['C4'], 
    # 'C3': ['C4', 'C5'], 
    # 'C4': ['C5'], 
    # 'C5': []
    # }
    # Maka akan mengembalikan:
    # ["C2", "C3"]
    vertices_in_degree = {}
    for vertice in graph:
        vertices_in_degree[vertice] = 0

    for vertice in graph:
        for in_vertice in graph[vertice]:
            vertices_in_degree[in_vertice] += 1

    zero_in_degree_vertices = []
    for vertice in vertices_in_degree:
        if (vertices_in_degree[vertice] == 0):
            zero_in_degree_vertices.append(vertice)

    return zero_in_degree_vertices

def topo_sort(graph):
    # Mengembalikan simpul hasil sorting graph
    # Jika graph bukan dag, maka akan mengembalikan 0
    # Contoh:
    # graph = 
    # {
    # 'C1': ['C2', 'C3', 'C4', 'C5'], 
    # 'C2': ['C4'], 
    # 'C3': ['C4', 'C5'], 
    # 'C4': ['C5'], 
    # 'C5': []
    # }
    # Maka akan mengembalikan
    # [["C1"], ["C2", "C3"], ["C4"], ["C5"]]
    sorted = []
    graph_copy = dict(graph)    # Copy agar graph pada parameter tidak terhapus
    while (len(graph_copy) != 0):
        zero_in_degree_vertices = get_zero_in_degree_vertices(graph_copy)
        if (len(zero_in_degree_vertices) > 0):
            sorted.append(zero_in_degree_vertices)
            delete_vertice(graph_copy, zero_in_degree_vertices)
        else:
            return 0
    return sorted

### Main program ###
graph = get_graph(input("Masukkan nama file: "))
solution = topo_sort(graph)
if (not(solution)) :
    print("Graph bukan sebuah DAG")
else :
    for i in range(len(solution)) :
        print("Semester " + str(i + 1) + "  : ", end="")
        for j in range(len(solution[i])) :
            if (j == 0) :
                print(solution[i][j], end="")
            else :
                print(", " + solution[i][j], end="")
        print()