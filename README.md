# Data_Compress
## 資料壓縮期末實作
參考之網站：https://officeguide.cc/steganography-hide-secret-data-in-pytorch-model-file-tutorial-examples/

流程：
1. 產生亂數資料（模擬機敏資料）
2. 讀取資料至 Python
3. 使用 LZMA 演算法執行資料壓縮
4. AES-128 加密
5. 將 Payload Data 放入 Pytorch ResNet18 模型
6. 
