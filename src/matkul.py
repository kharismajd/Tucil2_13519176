### Fungsi-fungsi tambahan ###
def getProblem(fileName) :
    # Mengembalikan matrix dari file fileName
    # Contoh: isi file.txt: 
    # C1, C3.
    # C2, C1, C4.
    # C3.
    # C4, C1, C3.
    # C5, C2, C4.
    # Maka akan mengembalikan:
    # [
    #    ["C1", "C3"],
    #    ["C2", "C1", "C4"],
    #    ["C3"],
    #    ["C4", "C1", "C3"],
    #    ["C5", "C2", "C4"]
    # ]
    f = open("../test/" + fileName, "r")
    dag = []
    for line in f :
        line = line.replace(".", "")
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")
        dag.append(line)
    f.close()
    return dag

def find_zero_in_degree(dag) :
    # Mengembalikan array simpul-simpul yang
    # memiliki in-degree 0
    # Contoh: dag = 
    # [
    #   ["C2"],
    #   ["C3"],
    #   ["C4", "C1", "C2", "C3"],
    #   ["C5", "C1", "C3", "C4"]
    # ]
    # Maka akan mengembalikan:
    # ["C2", "C3"]
    zero_in_degree = []
    for i in range (len(dag)) :
        if (len(dag[i]) == 1) :
            zero_in_degree.append(dag[i][0])
    return zero_in_degree

def delete_dag_node(dag, nodes) :
    # Menghapus simpul-simpul dan busur yang keluar dari
    # simpul tersebut di dag yang ada di array nodes
    # Contoh: 
    # dag = 
    # [
    #   ["C2"],
    #   ["C3"],
    #   ["C4", "C2", "C3"],
    #   ["C5", "C3", "C4"]
    # ]
    # nodes = ["C2", "C3"]
    #
    # Maka dag akan berubah menjadi:
    # dag =
    # [
    #   ["C4"],
    #   ["C5", "C4"]
    # ]
    empty = False
    i = 0
    while ((not(empty)) and (i < len(dag))) :
        j = 0
        while ((not(empty)) and (j < len(dag[i]))) :
            found = False
            k = 0
            while ((not(found)) and (k < len(nodes))) : 
                if (dag[i][j] == nodes[k]) :
                    dag[i].pop(j)
                    found = True
                    j -= 1
                k += 1
            j += 1
        if (len(dag[i]) == 0) :
            dag.pop(i)
            i -= 1
            if (len(dag) == 0) :
                empty = True
        i += 1
    return 0

def topo_sort(dag) :
    # Mengembalikan simpul hasil sorting dag
    # Jika tidak ada solusi, maka akan mengembalikan 0
    # Contoh:
    # dag = 
    # [
    #   ["C1"],
    #   ["C2", "C1"],
    #   ["C3", "C1"],
    #   ["C4", "C1", "C2", "C3"],
    #   ["C5", "C1", "C3", "C4"]
    # ]
    # Maka akan mengembalikan
    # [["C1"], ["C2", "C3"], ["C4"], ["C5"]]
    solution = []
    dag_copy = [node[:] for node in dag]    # Copy agar dag di parameter tidak terhapus
    while(len(dag_copy) != 0) :
        zero_in_degree = find_zero_in_degree(dag_copy)
        if (len(zero_in_degree) > 0) :
            solution.append(zero_in_degree)
            delete_dag_node(dag_copy, zero_in_degree)
        else :
            return 0
    return solution

### Main program ###
dag = getProblem(input("Masukkan nama file: "))
solution = topo_sort(dag)
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