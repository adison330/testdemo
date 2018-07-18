#! /usr/bin/env python
fram imageai.Detection import ObjectDetection
import OS

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinNet()
detector.setModelPath( os.path.join(execution_path , "resent50_coco_best_v2.0.1.h5"))
detector.loadModel()
custom_objects = detector.CustomObjects(person = True car = False)
detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path , "image.png"),
                                                   output_image_path=os.path.join(execution_path , "image_new.png"),
                                                   custom_objects=custom_objects , minimum_percentage_probability=65)

for eachObject in detections:
    print(eachObject["name"] + ":" eachObject["percentage_probability"])
    print("-" * 50)

