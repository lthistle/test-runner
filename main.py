from flask import Flask, jsonify, request
import subprocess
import uuid
import os
app = Flask(__name__)

@app.route("/test_runner", methods=["POST"])
def setName():
    if request.method=='POST':
        return do_docker_run(request)


def do_docker_run(request):
    dir_name = "./" + str(uuid.uuid4())
    #copy init files
    subprocess.run(f"mkdir {dir_name}", shell = True)
    subprocess.run(f"cp -r ./init_files/* {dir_name}", shell = True)

    #copy in tc
    with open(dir_name + "/test.cc", "wb") as f:
        f.write(request.get_data())

    output = b""
    #run docker compiler
    sp = subprocess.run(f"cd {dir_name} && docker run -v $(pwd):/outside --rm tc_compiler", shell = True, capture_output=True)
    output += sp.stdout

    #run docker runner
    sp = subprocess.run(f"cd {dir_name} && docker run -v $(pwd)/bin:/outside --rm tc_runner", shell = True, capture_output=True)
    output += sp.stdout

    #cleanup
    subprocess.run(f"rm -rf {dir_name}", shell = True)

    return output

