import os
import sys
import time
import ollama
import pygraphviz as pgv
from xml.dom.minidom import Document

MODEL1 = "llama3"
MODEL2 = "mistral"
list_models = [MODEL1, MODEL2]

PROMPT = "Analyzing the Python code and converting its structure into a dot format text for later do visualization with Graphviz. The dot format text should represent the flow of the code, including functions, classes, and their relationships. Provide only the dot file content, dont explain or comment the code. Do not create a code solution for generate the dot files. You must generate the dot file only in clear dot format. These are the rules 1) Parse the given Python code. 2) Identify all classes and functions. 3) Create nodes for each class and function. 4) Create edges to represent calls or dependencies between functions and classes. 5) Generate the corresponding dot format text. 6) Please ensure the dot format text accurately reflects the structure and relationships within the provided Python code. 7) Each class and function should be represented as a node, and edges should represent the relationships and calls between them. 8) the final result must start with 'digraph {' and end with '}'. 9) Review the result, confirm the brackets are correctly opened and closed."

def analize(data, mdl=MODEL1, prompt=PROMPT):
     response = ollama.chat(model=mdl, messages=[
          {
          'role': 'system',
          'content': prompt   
          },
     {
          'role': 'user',
          'content': data,
     },
     ])
     return response['message']['content']
  
def save_results(result, filename, model_name):
    epoch_time = str(int(time.time()))
    base_filename = os.path.basename(filename)
    new_filename = f"data/{base_filename.split('.')[0]}_{epoch_time}_{model_name}.dot"
    with open(new_filename, "w") as f:
        f.write(result)
    print(f"Results saved to {new_filename}")

def generate_drawio(dot_file_path, drawio_file_path):
    try:
        # Load the .dot file and create a graph from it
        graph = pgv.AGraph(filename=dot_file_path)
    except Exception as e:
        print(f"Failed to load .dot file: {e}")
        return
    
    try:
        # Create a new XML document
        doc = Document()
        
        # Create the mxfile and diagram elements
        mxfile = doc.createElement('mxfile')
        mxfile.setAttribute('host', 'app.diagrams.net')
        doc.appendChild(mxfile)

        diagram = doc.createElement('diagram')
        diagram.setAttribute('name', 'Page-1')
        mxfile.appendChild(diagram)

        # Create the mxGraphModel element
        graph_model = doc.createElement('mxGraphModel')
        diagram.appendChild(graph_model)

        # Create the root element
        root = doc.createElement('root')
        graph_model.appendChild(root)

        # Add the base elements
        mxCell = doc.createElement('mxCell')
        mxCell.setAttribute('id', '0')
        root.appendChild(mxCell)

        mxCell = doc.createElement('mxCell')
        mxCell.setAttribute('id', '1')
        mxCell.setAttribute('parent', '0')
        root.appendChild(mxCell)

        # Create elements for each node in the graph
        node_id_map = {}  # To map node names to IDs
        for i, node in enumerate(graph.nodes(), start=2):
            node_id = str(i)
            node_id_map[node] = node_id
            
            node_element = doc.createElement('mxCell')
            node_element.setAttribute('id', node_id)
            node_element.setAttribute('value', node)
            node_element.setAttribute('style', 'shape=ellipse;fillColor=#FF0000;strokeColor=#000000;')
            node_element.setAttribute('vertex', '1')
            node_element.setAttribute('parent', '1')
            
            geometry = doc.createElement('mxGeometry')
            geometry.setAttribute('x', '20')
            geometry.setAttribute('y', str(40 * i))  # Spread nodes vertically
            geometry.setAttribute('width', '80')
            geometry.setAttribute('height', '40')
            geometry.setAttribute('as', 'geometry')
            
            node_element.appendChild(geometry)
            root.appendChild(node_element)

        # Create elements for each edge in the graph
        edge_id = len(graph.nodes()) + 2  # Start edge IDs after node IDs
        for edge in graph.edges():
            edge_element = doc.createElement('mxCell')
            edge_element.setAttribute('id', str(edge_id))
            edge_id += 1
            edge_element.setAttribute('value', '')
            edge_element.setAttribute('style', 'edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;')
            edge_element.setAttribute('edge', '1')
            edge_element.setAttribute('source', node_id_map[edge[0]])
            edge_element.setAttribute('target', node_id_map[edge[1]])
            edge_element.setAttribute('parent', '1')
            
            edge_geometry = doc.createElement('mxGeometry')
            edge_geometry.setAttribute('relative', '1')
            edge_geometry.setAttribute('as', 'geometry')
            
            edge_element.appendChild(edge_geometry)
            root.appendChild(edge_element)

        # Write the XML document to the .drawio file
        with open(drawio_file_path, 'w') as f:
            f.write(doc.toprettyxml(indent='  '))
    except Exception as e:
        print(f"Failed to write .drawio file: {e}")



def main():
    if len(sys.argv) < 2:
        print("Please provide a filename as an argument.")
        return

    filename = sys.argv[1]
    extension = filename.split(".")[-1]

    if extension not in ["txt", "py"]:
        print("Invalid file extension. Only 'txt' and 'py' extensions are allowed.")
        return

    with open(filename) as f:
        data = f.read()
        
    # generate as meny dot files as models in the list
    for mdl in list_models:
        print(f"Output using model: {mdl}")

        start_time = time.time()
        result = analize(data, mdl=mdl, prompt=PROMPT)
        end_time = time.time()
        print(f"Time taken for analysis: {end_time - start_time} seconds")
        model_name = mdl.split(":")[0]
        save_results(result, filename, model_name)

        # TODO improve the output from dot files to use for drawio generation
        # # generate the drawio diagram
        # drawio_file = f'{filename}_{model_name}.drawio'
        # generate_drawio(result, drawio_file)

if __name__ == "__main__":
    main()
