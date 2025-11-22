import json
import parent_module.child_module_1 as cm1
from parent_module.child_module_2 import func_2

def main():
    with open("data_obj.json", "r") as json_file:
        json_obj = json.load(json_file)
    
    print(json_obj)
    
    with open("data_list.json", "r") as json_file:
        json_list = json.load(json_file)
    
    print(json_list)
    
    data = {
        "key": "value",
        "int": 10
    }
    with open("data_out.json", "w") as json_file:
        json.dump(data, json_file)
    
    cm1.func_1()
    func_2()

if __name__ == "__main__":
    main()
