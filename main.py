import sys
import subprocess
#INPUTS: A string query
#OUTPUTS: A json internal file that contains the text from the pubmed scripts
def GetABS(query, resultNum):
    print(f"Lookup query is {query}")
    print(f"Looking for result number {resultNum}")
    
 
 
    # If your shell script has shebang, 
    # you can omit shell=True argument.
    subprocess.run(["./ed.sh", f"pubmed {query} {resultNum}"], shell=True)





if __name__ == '__main__':
    print(f"Searching pubmed for query : {sys.argv[1]}")
    queryString = sys.argv[1]


