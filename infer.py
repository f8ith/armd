from inference_sdk import InferenceHTTPClient
import supervision as sv
import cv2

image_file = "my_image.jpg"
image = cv2.imread(image_file)

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="fxyEFnYrVNPPp1gFdn6k"
)

result = CLIENT.infer("my_image.jpg", model_id="mahjong-baq4s/41")

detections = sv.Detections.from_inference(result)

# create supervision annotators
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# annotate the image with our inference results
annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections)

cv2.imwrite("annotated.jpg", annotated_image)
# display the image
# sv.plot_image(annotated_image)
