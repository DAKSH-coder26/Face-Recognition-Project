# 🎯 Face Recognition with OpenCV

This is a simple and modular face recognition project using **OpenCV** and **Local Binary Patterns Histogram (LBPH)**. It allows you to:

- 📸 Collect face data using your webcam  
- 🧠 Train an LBPH face recognizer on the collected dataset  
- 👁️‍🗨️ Run real-time face recognition on webcam feed  

---

## 📁 Project Structure

```
Face Recognition/
├── Dataset_creation.py    # Capture and save face images
├── Training.py            # Train LBPH face recognizer
├── Recognition.py         # Perform real-time face recognition
├── main.py                # Orchestrates the full 

---

## 🔧 Requirements

Install Python packages via pip:

```bash
pip install -r requirements.txt
```

You mainly need:
- `opencv-python`

---

## 🚀 How to Use

### 1. Run the main controller
```bash
python main.py
```
Follow the CLI prompts to:
- Add the number of users
- Enter name & ID
- Capture 40 face images per person
- Train the model
- Start live recognition

---

## 📝 Notes

- Captured images are saved in `face_dataset/<name>/`
- Trained model is stored in `trainer.yml`
- You can adjust face recognition sensitivity by tweaking the confidence threshold in `Recognition.py`

---

## 📦 To-Do / Improvements

- Add GUI for easy usability  
- Replace Haar cascades with DNN or Mediapipe  
- Auto-save ID-name mapping for future reuse  
- Add tests and evaluation metrics  
- Deploy as a desktop or web app  

---

Feel free to fork and contribute!
