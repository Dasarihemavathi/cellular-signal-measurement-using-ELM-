Cellular Signal Measurement and Classification Using Extreme Learning Machine (ELM)

🌐 Project Overview
A machine learning project that measures and classifies cellular signals from real-world spectrum data using the Extreme Learning Machine (ELM) algorithm. The system predicts the type of signal present in the spectrum such as WiFi, LTE and other cellular signals.
This project was developed as a college final year project using real spectrum data collected from cellular environments — making it highly relevant to practical telecom applications.

✨ What This Project Does

📥 Takes real cellular spectrum measurement data as input
⚙️ Preprocesses and extracts features from signal data
🤖 Uses ELM algorithm to classify the signal type
📊 Predicts whether the signal is WiFi, LTE or other cellular type
📈 Achieves 76.5% classification accuracy on real world data


🛠️ Technologies Used
TechnologyPurposePythonCore programming languageExtreme Learning Machine (ELM)Signal classification algorithmNumPyNumerical operations and array handlingPandasData loading and preprocessingMatplotlibVisualizing signal data and resultsScikit-learnData splitting, preprocessing, metrics

📊 Model Performance
MetricResultAlgorithmExtreme Learning Machine (ELM)Accuracy76.5%Data TypeReal world cellular spectrum dataSignal Types ClassifiedWiFi, LTE and other cellular signals

Achieved 76.5% classification accuracy on real world cellular spectrum data. Since real spectrum data contains natural noise and interference, this accuracy demonstrates the model's robustness in practical environments.


📡 About the Dataset

Type: Real spectrum data collected from cellular environments
Signal Types: WiFi, LTE and other cellular signals
Data: Actual signal measurements — not simulated or synthetic
Real world data makes this project significantly more challenging and valuable than lab datasets!


🧠 How It Works
Real spectrum data collected from cellular environment
                    ↓
Data loaded and preprocessed (cleaning, normalization)
                    ↓
Feature extraction from signal measurements
                    ↓
ELM model trained on extracted features
                    ↓
Model predicts signal type (WiFi / LTE / other)
                    ↓
Accuracy evaluated and results displayed

💡 Why ELM over Traditional Neural Networks?
FeatureTraditional Neural NetworkELMTraining SpeedSlow⚡ Very FastAccuracyHighHighComplexityHighLowOverfittingCommonLess proneTuning RequiredHighMinimal
ELM was chosen because it trains significantly faster than traditional neural networks while maintaining high classification accuracy — making it ideal for real-time signal classification!

🚀 How to Run This Project
1. Clone the Repository
bashgit clone https://github.com/Dasarihemavathi/cellular-signal-measurement-using-ELM-.git
cd cellular-signal-measurement-using-ELM-
2. Create Virtual Environment
bashpython -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
3. Install Dependencies
bashpip install -r requirements.txt
4. Run the Project
bashpython main.py



📈 Results

Successfully classified cellular signal types from real spectrum data
Achieved 76.5% accuracy using ELM algorithm
ELM showed significantly faster training compared to traditional neural networks
Model performs well despite natural noise present in real world spectrum data

Team Lead: Dasari Hemavathi 

📧 dasarihemavathi8541@gmail.com
🔗 linkedin.com/in/dasarihemavathi
🐙 github.com/Dasarihemavathi

🎓 Academic Details

Project Type: College Final Year Project
Institution: Krishna Chaitanya Institute of Technology and Sciences (KCITS)
Department: Computer Science and Engineering
Year: 2026

