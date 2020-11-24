import os
import utils
import json

uploaded_files_path = utils.BASE_PATH + "uploaded_files/"
bash_command_submit_trx = "java -cp ./takamakachain-1.0-SNAPSHOT-jar-with-dependencies.jar " \
                    " -Djava.awt.headless=true " \
                    "com.h2tcoin.takamakachain.main.DirectCall -e=test -w=walletIsacco -s=asdasdasd -i=0 -t="

list_of_files = os.listdir(uploaded_files_path)
file_processed = utils.load_resource("file_processed.txt")

for single_file in list_of_files:
    splitted_file_name = single_file.split(".")
    if splitted_file_name[0] not in file_processed and splitted_file_name[1] == 'json':
        f = open(uploaded_files_path + single_file, "r")
        opened_json_resource = json.loads(f.read())
        print(opened_json_resource)
        if opened_json_resource['fileWritten']:
            os.system(bash_command_submit_trx + json.dumps(opened_json_resource['transactionJson']))
            file_processed.append(splitted_file_name[0])

utils.update_resource(file_processed, 'file_processed.txt')