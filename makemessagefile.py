import subprocess

def compile_proto(proto_file, output_dir):
    command = r"python -m grpc_tools.protoc C:\Users\User\Desktop\ProjectgGF\msgs.proto --go_out=. C:\Users\User\Desktop\ProjectgGF\ "
    subprocess.call(command, shell=True)

# Usage example
#"python -m grpc_tools.protoc --proto_path=. --python_out={output_dir} {proto_file}"
#proto_file = r"msgs.proto"
#output_dir = r"C:\Users\User\Desktop\ProjectgGF"

compile_proto()#proto_file, output_dir)
