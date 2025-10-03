# Indoor Air Quality Predictions & Smart Automation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A smart home project that predicts indoor air quality using deep learning models and manages automation systems with a user-friendly web interface.

> **Publication:** This study has been published in the [Journal of Artificial Intelligence and Human Sciences](https://dergipark.org.tr/tr/pub/jaihs).

## Demo

<p align="center">
  <img src="assets/animation.gif" alt="Application Demo" width="700"/>
</p>

## Project Objective

Modern home automation systems face three fundamental challenges: incorrect data readings due to sensor malfunctions, difficulty adapting to short-term user preferences, and lack of foresight for potential issues. This project solves these problems by forecasting future air quality using **deep neural networks**.

## 🎯 Project Objective

## Features

**Prediction Models:** GRU (Gated Recurrent Unit), LSTM (Long Short-Term Memory), and BiGRU (Bidirectional GRU) for temperature, relative humidity, and air pressure predictions.

## Dataset

**CN-OBEE Dataset** - 1 year of minute-by-minute data from a residential unit in Beijing (May 31, 2021 - May 31, 2022). Includes temperature, humidity, pressure, occupancy data from 5 rooms, plus outdoor weather and energy consumption records.

## Installation

```bash
git clone https://github.com/KadirGokdeniz/Indoor-AirQ-Predicitons.git
cd Indoor-AirQ-Predicitons
pip install -r requirements.txt
streamlit run src/Smart-Air.py
```

## Model Performance

### Temperature (Average)
| Model  | MAE (°C) | RMSE (°C) |
|--------|----------|-----------|
| GRU    | 0.57     | 2.98      |
| BiGRU  | 0.60     | 2.96      |
| LSTM   | 0.93     | 3.12      |

### Relative Humidity (Average)
| Model  | MAE (%)  | RMSE (%) |
|--------|----------|----------|
| GRU    | 5.41     | 9.21     |
| LSTM   | 6.14     | 9.02     |
| BiGRU  | 6.98     | 10.01    |

### Air Pressure (Average)
| Model  | MAE (hPa) | RMSE (hPa) |
|--------|-----------|------------|
| BiGRU  | 578.48    | 1,057.83   |
| GRU    | 604.49    | 1,089.11   |
| LSTM   | 609.26    | 1,089.06   |

## Key Findings

1. GRU model provides the most balanced and high-performing results across parameters
2. Room occupancy frequency significantly affects prediction accuracy
3. High-occupancy rooms (kitchen, living room) yield better predictions
4. BiGRU excels specifically in air pressure predictions

## Usage

```bash
streamlit run src/Smart-Air.py
```

1. Select a room from the interface
2. Choose the parameter to monitor (Temperature/Humidity/Pressure)
3. Set date and time range
4. Control automation mode (Get Stable/Schedule)
5. Save changes

## Technologies

Python 3.8+, Streamlit, TensorFlow/Keras, Pandas, NumPy, Altair, Scikit-learn

## Documentation

- `docs/Demo.pdf` - Application usage demonstration
- `docs/Air-Smart-Report.pdf` - Detailed technical report
- `notebooks/air_quality_predictions.ipynb` - Model training notebook

## Citation

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

## Contributing

Fork the repository, create a feature branch, commit changes, push to the branch, and open a Pull Request.

## Contact

**Kadir Gokdeniz** - kadirqokdeniz@hotmail.com  
**Erkan Bostanci** - Ankara University, Computer Engineering Department

## License

This project is licensed under the MIT License.

---

If you like this project, give it a star!