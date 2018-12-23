# DeepGlobe Land Cover Classification Challenge 土地利用分类竞赛
## Timeline 工作时间线
-[ ] Dataset 数据集准备
    -[x] Load file path文件目录导入
    -[x] 底图与标注文件的对应关系
    -[ ] 标注文件的格式化
    -[ ] 
-[ ] DeepLab 模型准备
    -[ ] 迁移学习
-[ ] Test   测试
-[ ] Result 结果展示
 ## DATASET 数据集
### DATA 数据
* The training data for Land Cover Challenge contains 803 satellite imagery in RGB, size 2448x2448.
* The imagery has 50cm pixel resolution, collected by DigitalGlobe's satellite.
* You can download the training data in the download page with filetype of “Starting Kit”. Testing satellite images will be will be uploaded later.
* 训练数据集包括803张卫星图片，RGB格式，尺寸2448 * 2448
* 图像分辨率为50cm，由 DigitalGlobe's 卫星提供
* 可通过下载页点击"Starting Kit"下载数据。
 ### Label 标注
* Each satellite image is paired with a mask image for land cover annotation. The mask is a RGB image with 7 classes of labels, using color-coding (R, G, B) as follows.
    * Urban land: 0,255,255 - Man-made, built up areas with human artifacts (can ignore roads for now which is hard to label)
    * Agriculture land: 255,255,0 - Farms, any planned (i.e. regular) plantation, cropland, orchards, vineyards, nurseries, and ornamental horticultural areas; confined feeding operations.
    * Rangeland: 255,0,255 - Any non-forest, non-farm, green land, grass
    * Forest land: 0,255,0 - Any land with x% tree crown density plus clearcuts.
    * Water: 0,0,255 - Rivers, oceans, lakes, wetland, ponds.
    * Barren land: 255,255,255 - Mountain, land, rock, dessert, beach, no vegetation
    * Unknown: 0,0,0 - Clouds and others
* File names for satellite images and the corresponding mask image are <id>_sat.jpg and <id>_mask.png. <id> is a randomized integer.
* Please note:
    * The values of the mask image may not be the exact target color values due to compression. When converting to labels, please binarize each R/G/B channel at threshold 128.
    * Land cover segmentation from high-resolution satellite imagery is still an exploratory task, and the labels are far from perfect due to the cost for annotating multi-class segmentation mask. In addition, we intentionally didn't annotate roads because it's already covered in a separate road challenge.
    
* 每张卫星图片有一张与之对应的标注图片。这张标注图片也是RGB格式，一共分为7类，每类对应的图像(R,G,B)编码对应关系如下：
    * 城市土地： 0，255，255，浅蓝色，人造建筑（可以忽略道路）
    * 农业用地： 255，255，0，黄色，农田，任何计划中（定期）的种植、农田、果园、葡萄园、苗圃、观赏性园艺以及养殖区
    * 牧场： 255，0，255，紫色，除了森林，农田之外的绿色土地，草地
    * 森林：0，255，0，绿色，任何土地上有x%的树冠密度。
    * 水系：0，0，255，深蓝色，江河湖海湿地
    * 荒地：255，255，255, 白色，山地，沙漠，戈壁，沙滩，没有植被的地方
    * 未知土地： 0，0，0，黑色，云层遮盖或其他因素
* 卫星图片和与其对应的标注图片的命名格式为\<id>_sat.jpg和\<id>_mask.png,\<id>是一个随机的整数。
* 需要注意：
    * 由于压缩，标注图像的值可能不是准确的目标颜色值。当转换到标签时，请将每个R/G/B通道按128阈值二值化。
    * 高分辨率卫星图像的土地覆被分割仍然是一个探索性的任务，由于标注多类分割的代价很大，标签还远远不够完善。此外，我们故意不标注道路，因为它已经包含在一个单独的道路提取挑战赛中。
### Evaluation Metric 评价指标
* We will use pixel-wise mean Intersection over Union (mIoU) score as our evaluation metric.
    * IoU is defined as: True Positive / (True Positive + False Positive + False Negative).
    * mean IoU is calculated by averaging over all classes.
* Please note the Unknown class (0,0,0) is not an active class used in evaluation. Pixels marked as Unknown will simply be ignored. So effectively mIoU is averaging over 6 classes in total.
* 我们将采用像素级别的平均IoU分数作为评价指标。
    * IoU的定义是：交集/并集，公式：  预测准确的面积/(预测准确面积 + 没有预测出来的面积 + 预测错误的面积)
    * 平均IoU由各个类别的IoU取均值得到
* 需要注意的是"未知土地"(0,0,0)并不是一个真实的类别，在这个计算中也没有起到作用。所以有效的mIoU是前6个类别IoU的均值。

## Result 结果展示


