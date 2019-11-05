# DeepGlobe Land Cover Classification Challenge 土地利用分类竞赛
 [English](https://github.com/GeneralLi95/deepglobe_land_cover_classification_with_deeplabv3plus/blob/master/readme.md) | 简体中文
## 数据集
### 数据
* 训练数据集包括803张卫星图片，RGB格式，尺寸2448 * 2448
* 图像分辨率为50cm，由 DigitalGlobe's 卫星提供
* 可通过下载页点击"Starting Kit"下载数据。(根据主办方的版权声明，下载数据请到原竞赛网页，即使竞赛已经结束，仍然可以参加)

### 标注

* 每张卫星图片有一张与之对应的标注图片。这张标注图片也是RGB格式，一共分为7类，每类对应的图像(R,G,B)编码对应关系如下：
    * 城市土地： 0，255，255，浅蓝色，人造建筑（可以忽略道路）
    * 农业用地： 255，255，0，黄色，农田，任何计划中（定期）的种植、农田、果园、葡萄园、苗圃、观赏性园艺以及养殖区
    * 牧场： 255，0，255，紫色，除了森林，农田之外的绿色土地，草地
    * 森林：0，255，0，绿色，任何土地上有x%的树冠密度。
    * 水系：0，0，255，深蓝色，江河湖海湿地
    * 荒地：255，255，255, 白色，山地，沙漠，戈壁，沙滩，没有植被的地方
    * 未知土地： 0，0，0，黑色，云层遮盖或其他因素
* 卫星图片和与其对应的标注图片的命名格式为 id_sat.jpg和id_mask.png,id 是一个随机的整数。
* 需要注意：
    * 由于压缩，标注图像的值可能不是准确的目标颜色值。当转换到标签时，请将每个R/G/B通道按128阈值二值化。
    * 高分辨率卫星图像的土地覆被分割仍然是一个探索性的任务，由于标注多类分割的代价很大，标签还远远不够完善。此外，我们故意不标注道路，因为它已经包含在一个单独的道路提取挑战赛中。

### 评价指标
* 我们将采用像素级别的平均IoU分数作为评价指标。
    * IoU的定义是：交集/并集，公式：  预测准确的面积/(预测准确面积 + 没有预测出来的面积 + 预测错误的面积)
    * 平均IoU由各个类别的IoU取均值得到
* 需要注意的是"未知土地"(0,0,0)并不是一个真实的类别，在这个计算中也没有起到作用。所以有效的mIoU是前6个类别IoU的均值。

## 结果展示
<table border=0>
<tr>
    <td>
        <img src="/img/6399_sat.jpg" border=0 margin=1 width=512>
    </td>
    <td>
        <img src="/img/6399_mask.png" border=0 margin=1 width=512>
    </td>
</tr>
</table>

## 致谢
- [rishizek's repo tensorflow-deeplab-v3-plus](https://github.com/rishizek/tensorflow-deeplab-v3-plus)
- [DeepGlobe_2018_A_CVPR_2018_paper](http://openaccess.thecvf.com/content_cvpr_2018_workshops/w4/html/Demir_DeepGlobe_2018_A_CVPR_2018_paper.html)
- [deepglobe](http://deepglobe.org/).

---
## 如何复现此工作

### 文件结构组织


* deepglobe_land
  * dataset
    * land_train  (存放下载下来的数据 )
    * onechannel_label (运行 rgb2label.py 生成)
    * voc_train_all.record (运行 create_tf_record_all.py 生成 )
  * ini_checkpoints
      * resnet_v2_101  (resnet_v2_101.ckpt and train.graph)
  * rgb2label.py
  * create_tf_record_all.py




### 各段代码功能

1. rgb2label.py 数据标注文件 id_mask.png 是 RGB 三通道图像，输入训练集的时候必须首先转为单通道图像，故该代码用于执行，图像到单通道图像的转换，此处原始卫星图像 id_sat.jpg, 标注图像 id_mask.png，单通道标注图像 id_label.png 。  这段代码可以作为一段工具代码在其他地方使用。


2. create_tf_record_all.py  建立 tfrecord 文件，该代码执行后，直接将 land_train文件夹里的所有 id_sat.jpg 文件与 onechannel_label 里的 id_label 文件打包生成一个 voc_train_all.record文件，该文件中包含了数据集和验证集，不需要手动区分数据集验证集，训练过程中会随机选择一部分作为数据集，另一部分作为验证集。

3. deeplab_model.py  deeplab模型基本不用动

4. train.py 需要在里面进行一些参数设置，类别，训练集合验证集的数据比，这里我们设置训练集723张图片，验证集80张。
