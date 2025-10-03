# 🏠 Indoor Air Quality Predictions & Smart Automation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A smart home project that predicts indoor air quality using deep learning models and manages automation systems with a user-friendly web interface.

> **📄 Publication:** This study has been published in the [Journal of Artificial Intelligence and Human Sciences](https://dergipark.org.tr/tr/pub/jaihs).

## 🎬 Demo

<p align="center">
  <img src="assets/animation.gif" alt="Application Demo" width="700"/>
</p>

*Interactive demo showing room selection, data visualization, and automation control*

## 🎯 Project Objective

Modern home automation systems face three fundamental challenges:
- ❌ Incorrect data readings due to sensor malfunctions
- ❌ Difficulty adapting to short-term user preferences
- ❌ Lack of foresight for potential issues

This project aims to solve these problems by forecasting future air quality using **deep neural networks**.

## ✨ Features

### 🤖 Prediction Models
- **GRU (Gated Recurrent Unit)** - Superior performance in temperature and pressure
- **LSTM (Long Short-Term Memory)** - Strong in complex patterns
- **BiGRU (Bidirectional GRU)** - Leader in air pressure predictions

### 📊 Prediction Parameters
- 🌡️ **Temperature** (°C)
- 💧 **Relative Humidity** (%)
- 📈 **Air Pressure** (Pa)

### 🖥️ Air-Smart Controller
- 44-day future predictions
- 10-minute data intervals
- Separate monitoring for 5 different rooms
- Automation mode control (Stop/Schedule)
- Real-time data visualization

## 📦 Dataset

**CN-OBEE Dataset** - 1 year of data collected from a residential unit in Beijing
- 📅 Period: May 31, 2021 - May 31, 2022
- ⏱️ Frequency: Minute-by-minute recording
- 🏠 Rooms: Cloakroom, Home Office, Kitchen, Living Room, Secondary Bedroom
- 🌦️ Includes outdoor weather data and energy consumption records

## 🛠️ Technologies

```
Python 3.8+
├── Streamlit          # Web interface
├── TensorFlow/Keras   # Deep learning models
├── Pandas             # Data processing
├── NumPy              # Numerical computations
├── Altair             # Data visualization
└── Scikit-learn       # Preprocessing and metrics
```

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/indoor-air-quality-prediction.git
cd indoor-air-quality-prediction

# Install required packages
pip install -r requirements.txt

# Generate prediction data (optional)
jupyter notebook Air_Quality_Prediction.ipynb

# Run the application
streamlit run Smart-Air.py
```

## 📈 Model Performance

### Temperature Prediction (Average)
| Model  | MAE (°C) | MSE | RMSE (°C) |
|--------|----------|-----|-----------|
| GRU    | 0.57     | 0.56| 2.98      |
| BiGRU  | 0.60     | 0.58| 2.96      |
| LSTM   | 0.93     | 1.54| 3.12      |

### Relative Humidity Prediction (Average)
| Model  | MAE (%)  | MSE    | RMSE (%) |
|--------|----------|--------|----------|
| GRU    | 5.41     | 61.98  | 9.21     |
| LSTM   | 6.14     | 60.24  | 9.02     |
| BiGRU  | 6.98     | 79.13  | 10.01    |

### Air Pressure Prediction (Average)
| Model  | MAE (hPa) | RMSE (hPa) |
|--------|-----------|------------|
| BiGRU  | 578.48    | 1,057.83   |
| GRU    | 604.49    | 1,089.11   |
| LSTM   | 609.26    | 1,089.06   |

## 💡 Key Findings

1. **GRU model** is overall the most balanced and high-performing model
2. **Room occupancy frequency** significantly affects prediction accuracy
3. High-occupancy rooms (kitchen, living room) yield better prediction results
4. **BiGRU** excels in air pressure predictions

## 📖 Usage

```python
# Start the Air-Smart Controller
streamlit run Smart-Air.py
```

1. Select a room from the interface that opens in your browser
2. Choose the parameter you want to monitor (Temperature/Humidity/Pressure)
3. Set the date and time range
4. Control automation mode (Get Stable/Schedule)
5. Save changes

## 📄 Documentation

- `demo.pdf` - Application usage demonstration
- `Air-Smart-Controller-Report.pdf` - Detailed technical report
- `Air_Quality_Prediction.ipynb` - Model training notebook

## 🔬 Citation

If you use this work, please cite as follows:

```bibtex
@article{gokdeniz2024indoor,
  title={Indoor Air Quality Predictions For Automation},
  author={Gokdeniz, Kadir and Bostanci, Erkan},
  journal={Journal of Artificial Intelligence and Human Sciences},
  volume={1},
  number={1},
  pages={56--66},
  year={2024}
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📧 Contact

**Kadir Gökdeniz** - kadirqokdeniz@hotmail.com  
**Erkan Bostancı** - Ankara University, Computer Engineering Department

## 📝 License

This project is licensed under the MIT License.

---

⭐ If you like this project, don't forget to give it a star!
