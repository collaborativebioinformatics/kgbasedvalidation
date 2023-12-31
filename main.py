import sys
import subprocess
#INPUTS: A string query
#OUTPUTS: A json internal file that contains the text from the pubmed scripts
def GetABS(db, query, resultNum):
    print(f"Lookup query is {query}")
    print(f"Looking for result number {resultNum}")
    
 
 
    # If your shell script has shebang, 
    # you can omit shell=True argument.
    subprocess.run(["./ed.sh " + f"\"{db}\" \"{query}\" {resultNum}"], shell=True)


def LinkLLM(llmDir):
    subprocess.run(["./vicuna_model7b/llama.cpp/main -m ./vicuna_model7b/llama.cpp/models/vicuna-7b-v1.5.Q4_K_M.gguf -f ./results.txt > kg.txt"], shell = True)
    return




if __name__ == '__main__':
    print(f"Searching pubmed for query : {sys.argv[1]}")
    db = sys.argv[1]
    queryString = sys.argv[2]
    GetABS(db, queryString, sys.argv[3])
    llmDir = "./vicuna_model7b/"
    LinkLLM(llmDir)
