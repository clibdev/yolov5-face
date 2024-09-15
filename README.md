# Fork of [deepcam-cn/yolov5-face](https://github.com/deepcam-cn/yolov5-face)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/yolov5-face/releases). (🔥)
* Installation with [requirements.txt](requirements.txt) file.
* The [wider_val.txt](data/widerface/val/wider_val.txt) file for WIDERFace evaluation. 
* The following deprecations and errors has been fixed:
  * UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument.
  * DeprecationWarning: 'np.float' is a deprecated alias for builtin 'float'.
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.
  * FutureWarning: Cython directive 'language_level' not set.
  * Cython Warning: Using deprecated NumPy API.
  * AttributeError: module 'numpy' has no attribute 'int'.
  * RuntimeError: result type Float can't be cast to the desired output type long int.
  * Fixed face bounding box drawing problem in the TensorRT example.
  * NameError: name 'warnings' is not defined.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Name                        | Model Size (MB) | Link                                                                                                                                                                                                | SHA-256                                                                                                                              |
|-----------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv5-BlazeFace            | 0.5<br>4.4      | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5-blazeface.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5-blazeface.onnx)       | 942997451c57981608d9e7eb7b0e964f2a83583b8add2409a2c5254a1f36f2d9<br>071cbb36cdb8d0d3dfb9305ba30f96c08a24342a4e835f48b4cc6bf1b185a564 |
| YOLOv5n-0.5-Face            | 1.1<br>5.7      | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5n-0.5-face.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5n-0.5-face.onnx)       | 9f7cdbcf5cd63f454c47b18e7400a69630b96a01efb7559367e91b6e962ad3bd<br>269eb1e54313f9d1f7941ed9939fa247767539bca5801fc7aa7895960e93ca43 |
| YOLOv5n-Face                | 13.7<br>10.5    | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5n-face.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5n-face.onnx)               | 794c94da54630f2ca66167fea25530c68133c61a2b14131b073c0d4064934e50<br>ee6ba4ccdc3c075d205c9703aec53a2aa3010c8d7fa08b0eff078e33a4b4fe6c |
| YOLOv5s-Face                | 54.4<br>30.9    | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5s-face.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5s-face.onnx)               | a594ade0f5e80f5cf15aef8997d285a3fb4b372a2af5262fbc6837d30318cda7<br>9083776982185402cfb3bd3cba8d453823068e72a0f9b0a6c6060439a850d9c5 |
| YOLOv5m-Face                | 161.2<br>84.2   | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5m-face.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5m-face.onnx)               | ca90ccc1b76c06d330a501bdb2cba63d3740fd3ef39baea89c7acc602557a4a2<br>c7ea51072e5f5c1ead34be14b3f4a23f44477448c271bc161b99d122fa0d8f10 |
| YOLOv5l-Face                | 356.4<br>181.7  | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5l-face.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5l-face.onnx)               | adfa3fbee5ba97ca86237cf8b45992aaea891ea481d59722da89bbd871a6a546<br>b8b13132e7dd609b82a7cf8ea76d7c6f7695cbd909dc77063e37166af0a12622 |
| YOLOv5l-Face (non-original) | 89.3<br>181.7   | [PyTorch](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5l-face-custom.pt), [ONNX](https://github.com/clibdev/yolov5-face/releases/latest/download/yolov5l-face-custom.onnx) | 7e20bf0c79888b230264e2b5d812a12a69c68bcf1a234b469f86c30d82bd6c2a<br>5340f05f54f3e22ca63234aa4f2622975fd23a62ccd656158f78c94dbeaa33f2 |

* Evaluation results on WIDERFace dataset:

| Name                        | Easy  | Medium | Hard  | GFLOPS | Params(M) |
|-----------------------------|-------|--------|-------|--------|-----------|
| YOLOv5-BlazeFace            | 90.4  | 88.7   | 78.0  | 2.6    | 0.182     |
| YOLOv5n-0.5-Face            | 90.76 | 88.12  | 73.82 | 1.5    | 0.447     |
| YOLOv5n-Face                | 93.61 | 91.52  | 80.53 | 5.6    | 1.726     |
| YOLOv5s-Face                | 94.33 | 92.61  | 83.15 | 15.2   | 7.075     |
| YOLOv5m-Face                | 95.30 | 93.76  | 85.28 | 48.2   | 21.063    |
| YOLOv5l-Face                | 95.78 | 94.30  | 86.13 | 110.6  | 46.627    |
| YOLOv5l-Face (non-original) | 95.63 | 94.06  | 85.49 | 110.6  | 46.627    |

YOLOv5l-Face (non-original) model training took about 10.57 hours using NVIDIA RTX 4090.
Results can be found in the [yolov5l-face.txt](result/train/yolov5l-face.txt) file

# Inference

```shell
python detect_face.py --weights weights/yolov5s-face.pt --source data/images/bus.jpg --save-img
```

# WIDERFace evaluation

* Download WIDERFace [validation dataset](https://drive.google.com/file/d/1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q/view).
* Move dataset to `data/widerface/val` directory.

```shell
python test_widerface.py --weights weights/yolov5s-face.pt --dataset_folder data/widerface/val/images
```
```shell
cd widerface_evaluate
```
```shell
python setup.py build_ext --inplace
```
```shell
python evaluation.py
```

# Export to ONNX format

```shell
pip install onnx onnxruntime
```
```shell
python export.py --weights weights/yolov5s-face.pt
```

# Export to TensorRT format

```shell
pip install tensorrt pycuda
```
```shell
python export.py --weights weights/yolov5s-face.pt --onnx2trt
```

# TensorRT Inference

```shell
python torch2trt/main.py --trt_path weights/yolov5s-face.trt --img_path data/images/bus.jpg
```

# PyTorch vs TensorRT speed comparison

```shell
python torch2trt/speed.py --torch_path weights/yolov5s-face.pt --trt_path weights/yolov5s-face.trt
```

# Training

* Download WIDERFace [training dataset](https://drive.google.com/file/d/15hGDLhsx8bLgLcIRD5DhYt5iBxnjNF1M/view).
* Download WIDERFace [validation dataset](https://drive.google.com/file/d/1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q/view).
* Download [annotation files](https://drive.google.com/file/d/1tU_IjyOwGQfGNUvZGwWWM4SwxKp2PUQ8/view).
* Move WIDERFace training images `WIDER_train/images` to `data/widerface/tmp/train/images`.
* Move WIDERFace validation images `WIDER_val/images` to `data/widerface/tmp/val/images`.
* Move training annotation file `train/label.txt` to `data/widerface/tmp/train/label.txt`.
* Move validation annotation file `val/label.txt` to `data/widerface/tmp/val/label.txt`.

```shell
python data/train2yolo.py data/widerface/tmp/train data/widerface/train
```
```shell
python data/val2yolo.py data/widerface/tmp data/widerface/val
```
```shell
pip install tensorboard
```

* Start training:

```shell
python train.py --data data/widerface.yaml --cfg models/yolov5n-0.5.yaml
```
```shell
python train.py --data data/widerface.yaml --cfg models/yolov5l.yaml --weights weights/yolov5l.pt
```

* Resume training:

```shell
python train.py --data data/widerface.yaml --cfg models/yolov5n-0.5.yaml --resume
```
```shell
python train.py --data data/widerface.yaml --cfg models/yolov5l.yaml --resume
```
