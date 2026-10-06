import json
from collections.abc import Iterable
from pathlib import Path

class DataPath():
    Any = "_any_"
    def __init__(self, *keys):
        self.value = keys

    def __len__(self):
        return len(self.get())

    def get(self):
        return self.value

class DataLoader():
    def __init__(self, path):
        self.path = Path(path)
        with open(self.path, 'r') as file:
            self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def __len__(self):
        return len(self.data)
        
    def get(self, data_path=DataPath()):
        out_values = []
        self._iter(data_path.get(), self.data, out_values)
        return out_values

    def get_keys(self, data_path=DataPath()):
        out_keys = []
        self._iter(DataPath(*data_path.get(), DataPath.Any).get(), self.data, [], out_keys)
        return out_keys
    
    def filter_keys(self, fn=lambda a, b: bool, path_start=DataPath(DataPath.Any)):
        out_keys = []
        out_values = []
        self._iter(path_start.get(), self.data, out_values, out_keys)
        r = []
        for i, _ in enumerate(out_values):
            if fn(out_values[i], out_keys[i]) == True:
                r.append(out_keys[i])
        return tuple(r)

    def _iter(self, keys, v=None, out_values=[], out_keys=[], last_key = None):
        
        for i, k in enumerate(keys):
            if i+1 <= len(keys):
                next_keys = keys[i+1:]
            else:
                next_keys = ()

            if not isinstance(v, dict):
                v = None
                break
            elif k == DataPath.Any:
                for candidate_k in v:
                    self._iter(next_keys, v[candidate_k], out_values, out_keys, candidate_k)
                v = None
                break
            elif isinstance(k, tuple):
                for candidate_k in k:
                    if candidate_k in v.keys():
                        self._iter(next_keys, v[candidate_k], out_values, out_keys, candidate_k)
                v = None
                break
            else:
                if k in v:
                    v = v[k]
                    last_key = k
                else:
                    v = None
                                   
        if v != None:
            out_values.append(v)
            out_keys.append(last_key)



