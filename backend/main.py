from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],  # Allow all headers (adjust as needed)
    expose_headers=["*"],
    allow_methods=["*"]
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

# @app.post('/pipelines/parse')
# def parse_pipeline(pipeline: str = Form(...)):
#     return {'status': 'parsed'}

# from fastapi import FastAPI, Body, HTTPException

# app = FastAPI()

@app.post("/pipelines/parse")
async def parse_pipeline(pipeline: dict = Body(...)):
  """
  Parses a pipeline represented as a dictionary containing nodes and edges.

  Raises:
      HTTPException: If there's an error processing the pipeline.
  """
  try:
    nodes = pipeline.get("nodes", [])
    edges = pipeline.get("edges", [])

    num_nodes = len(nodes)
    num_edges = len(edges)

    # Implement DAG check logic (replace with your preferred algorithm)
    is_dag = check_dag(nodes, edges)  # Placeholder for DAG check function

    return {
      "num_nodes": num_nodes,
      "num_edges": num_edges,
      "is_dag": is_dag,
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error parsing pipeline: {str(e)}")

# Function to check if the pipeline forms a DAG (replace with your implementation)
def check_dag(nodes, edges):
  # Implement your chosen DAG detection algorithm here
  # (e.g., topological sort, Kahn's algorithm)
  # This is a placeholder and needs to be replaced with a working implementation
  return True  
