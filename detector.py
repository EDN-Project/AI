import app as a

@a.app.route('/detect', methods=['POST'])
def detect_strawberries():
    if 'image' not in a.request.files:
        return a.jsonify({'error': 'No image file provided'}), 400

    file = a.request.files['image']
    npimg = a.np.frombuffer(file.read(), a.np.uint8)
    img = a.cv2.imdecode(npimg, a.cv2.IMREAD_COLOR)

    results = a.model(img)
    count = 0

    for box in results[0].boxes:
        class_id = int(box.cls[0].item())
        class_name = results[0].names[class_id]
        if class_name.lower().startswith("strawberry"):
            count += 1

    # حساب الوزن المتوقع
    total_weight_grams = count * a.AVERAGE_STRAWBERRY_WEIGHT
    total_weight_kg = total_weight_grams / 1000

    return a.jsonify({
        "count": count,
        "estimated_weight_grams": total_weight_grams,
        "estimated_weight_kg": total_weight_kg,
    })
    

if __name__ == "__main__":
    a.app.run(host="0.0.0.0", port=3000, debug=True)    
