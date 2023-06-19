import pickle
import numpy as np
from multi_layer_extend import MultiLayerNetExtend

network = MultiLayerNetExtend(input_size=784,hidden_size_list=[100,50,30],output_size=10,use_batchnorm=True)
f = open('sc_09011.binaryfile','rb')
data_saved_weight = pickle.load(f)
network.params = data_saved_weight
network.load_param()

def hand_write_img_to_num(img_data):
    #img_dataを正規化
    x_data = img_data.reshape(1,784)

    #モデルを使用し分類
    ans_list = network.predict(x_data)
    ans = np.argmax(ans_list)

    return ans