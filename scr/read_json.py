import json
import glob
import os

DATA_DIR = "../tiki_data"
GLOB_PATTERN = os.path.join(DATA_DIR, "*.json")

def load_all_data():
    data_list=[]
    try:
        files=sorted(glob.glob(GLOB_PATTERN))
        if not files:
            raise FileNotFoundError(f"Khong tim thay file {DATA_DIR}")
    except FileNotFoundError as f:
        print(f)
        return []
    print(f"da tim thay {len(files)}")
    for file_path in files:
        try:
            with open(file_path,"r",encoding="utf-8") as f:
                data=json.load(f)
                if not isinstance(data,list):
                    raise ValueError(f"du lieu khong phai list")
                for item in data:
                    if not isinstance(item,dict):
                        raise TypeError(f"du lieu trong phai khong o dang dict")

                data_list.extend(data)
        except FileNotFoundError:
            print(f"Khong tim thay file")
        except exception as f:
            print(f"Loi khong xac dinh")
    print(f"Doc xong.Tong so record trong data_list {len(data_list)}")
    return data_list
if __name__ == "__main__":
    data_list = load_all_data()
