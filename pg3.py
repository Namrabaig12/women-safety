from deepface import DeepFace

# Analyze detected face
result = DeepFace.analyze(img_path=face_img, actions=['gender'])
gender = result[0]['gender']
