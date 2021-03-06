import _pickle as cPickle
import numpy as np
import math
from torch.utils.data import Dataset, DataLoader

from .constants import TEST_LIST_20, TEST_LIST_30

class RawDataLoader(object):
    def __init__(self, data_path, data_name):
        self.path = data_path
        self.dataset = self._load_file(data_name)
    
    def _load_file(self, file_name):
        with open(self.path.joinpath(file_name), 'rb') as f:
            u = cPickle.Unpickler(f)
            dataset = u.load()
        return dataset


    def load_dataset(self, mode, x_keys):
        test_list = TEST_LIST_30
        valid_list = TEST_LIST_20
        #x_keys = [key for key in self.dataset[0][0]['scaled_statistics'].keys() if '_ratio_' in key or 'relative_' in key]

        #if mode == 'valid':
        #    list_name = VALID_LIST
        #el
        if mode == 'test':
            list_name = test_list
        else:
            list_name = None
        
        dataset_list = []
        found_nan = False
        
        for eN_dataset in self.dataset:
            set_name = eN_dataset[0]['set_name']
            if mode == 'train':
                #if (set_name not in VALID_LIST) and (set_name not in TEST_LIST):
                if set_name not in test_list:
                    dataset_list.append(eN_dataset)
            else:
                if set_name in list_name:
                    dataset_list.append(eN_dataset)
        
        names, measures, X, Y = [], [], [], []
        for eN_dataset in dataset_list:
            eN_list = []
            eN_measures = []
            for dataset in eN_dataset:
                data = []
                for key in x_keys:
                    if key in dataset['scaled_statistics'].keys():
                        if math.isnan(dataset['scaled_statistics'][key]):
                            found_nan = True
                            break
                        data.append(dataset['scaled_statistics'][key])
                    else:
                        print("ERROR : No key named " + key)
                if found_nan:
                    found_nan = False
                    continue
                eN_list.append(data)
                eN_measures.append((dataset['start_measure'], dataset['end_measure']))
            
            eN_list = np.asarray(eN_list)
            
            X.append(eN_list)
            Y.append(dataset['emotion_number'])
            names.append(dataset['set_name'])
            measures.append(eN_measures)
        
        return np.array(X), np.array(Y), names, measures


class EmotionDataset(Dataset):
    def __init__(self, x, y, names, measures):
        self.x = x
        self.y = y
        self.names = names
        self.measures = measures
    
    def __getitem__(self, index):
        return self.x[index], self.y[index] - 1, self.names[index], self.measures[index]
    
    def __len__(self):
        return self.x.shape[0]
            

def get_dataloader(data_path, data_name, feature_keys, batch_size):
    DL = RawDataLoader(data_path, data_name)
    x_train, y_train, names_train, measures_train = DL.load_dataset('train', feature_keys)
    #x_valid, y_valid, names_valid, measures_valid = DL.load_dataset('valid', feature_keys)
    x_test, y_test, names_test, measures_test = DL.load_dataset('test', feature_keys)

    train_set = EmotionDataset(x_train, y_train, names_train, measures_train)
    #valid_set = EmotionDataset(x_valid, y_valid, names_valid, measures_valid)
    test_set = EmotionDataset(x_test, y_test, names_test, measures_test)

    train_loader = DataLoader(train_set, batch_size=batch_size,  shuffle=True, drop_last=False)
    #valid_loader = DataLoader(valid_set, batch_size=batch_size,  shuffle=False, drop_last=False)
    test_loader = DataLoader(test_set, batch_size=batch_size,  shuffle=False, drop_last=False)

    #return train_loader, valid_loader, test_loader
    return train_loader, test_loader
