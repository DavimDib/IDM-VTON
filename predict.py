import os
from pathlib import Path
from demo import main as run_inference  # demo.py must exist and run IDM-VTON logic

class Predictor:
    def predict(self, person_image, cloth_image):
        input_dir = "inputs"
        output_dir = "results"
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        person_path = os.path.join(input_dir, "person.jpg")
        cloth_path = os.path.join(input_dir, "cloth.jpg")

        with open(person_path, "wb") as f:
            f.write(person_image.read())
        with open(cloth_path, "wb") as f:
            f.write(cloth_image.read())

        run_inference(input_dir=input_dir, output_dir=output_dir)

        return Path(os.path.join(output_dir, "output.jpg"))
