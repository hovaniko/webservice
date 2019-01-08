import os
import datetime

#This is for local deployment
# AccountPackages_path=r"C:\Users\hmina\Desktop\AccountPackages\AccountPackages"

# This is for pythanywheredeployment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AccountPackages_path = os.path.join(os.path.join(BASE_DIR, "media"),"accountpackages")



def get_docs_list(client_id):
    result=[]
    list_of_folders=os.listdir(AccountPackages_path)
    if client_id in list_of_folders:
        client_folder=os.path.join(AccountPackages_path,client_id)
        list_of_files= os.listdir(client_folder)

        for file in list_of_files:
            doc_info=[]
            doc_info.append(file)
            doc_info.append(datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(client_folder,file))))
            result.append(doc_info)


    return result
