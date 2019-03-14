# DeepGlobe Land Cover Classification Challenge 
 
## DATASET
### DATA 
* The training data for Land Cover Challenge contains 803 satellite imagery in RGB, size 2448x2448.
* The imagery has 50cm pixel resolution, collected by DigitalGlobe's satellite.
* You can download the training data in the download page with filetype of “Starting Kit”. Testing satellite images will be will be uploaded later.
* You can also download the data by click this [baiduyun link](https://pan.baidu.com/s/1kRSHGxmaeuBqACGcFaqhvw).
 ### Label 
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
    
### Evaluation Metric 
* We will use pixel-wise mean Intersection over Union (mIoU) score as our evaluation metric.
    * IoU is defined as: True Positive / (True Positive + False Positive + False Negative).
    * mean IoU is calculated by averaging over all classes.
* Please note the Unknown class (0,0,0) is not an active class used in evaluation. Pixels marked as Unknown will simply be ignored. So effectively mIoU is averaging over 6 classes in total.


## Result 


![](./img/6399_sat.jpg)
![](./img/6399_mask.png)

## Acknowledgment
This repo borrows code heavily from
- [rishizek's repo tensorflow-deeplab-v3-plus](https://github.com/rishizek/tensorflow-deeplab-v3-plus)


