# Deep Learning for Indoor Air Quality Forecasting

**Predicting temperature, humidity, and air pressure in smart buildings using GRU/LSTM networks - enabling proactive HVAC automation instead of reactive control.**

[![Paper](https://img.shields.io/badge/Paper-JAIHS%202024-blue)](https://dergipark.org.tr/tr/pub/jaihs)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)](https://tensorflow.org/)

---

## Why This Matters

Traditional HVAC systems are **reactive** — they respond after conditions become uncomfortable. This wastes energy and degrades occupant comfort. 

This project demonstrates that **10-minute ahead forecasting** with deep learning enables:
- **Proactive climate control** — adjust before discomfort occurs
- **Energy optimization** — reduce unnecessary heating/cooling cycles
- **Predictive maintenance** — detect sensor anomalies before they cause problems

---

## Results

Evaluated on **CN-OBEE dataset** (1 year, minute-level data, 5 rooms, Beijing residential unit):

| Parameter | Best Model | MAE | RMSE |
|-----------|------------|-----|------|
| Temperature | GRU | **0.57°C** | 2.98°C |
| Humidity | GRU | **5.41%** | 9.21% |
| Pressure | BiGRU | **578 hPa** | 1058 hPa |

**Key insight:** Room occupancy patterns significantly impact prediction accuracy. High-traffic rooms (kitchen, living room) yield better predictions due to more consistent temporal patterns.

---

## Approach

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           MACHINE LEARNING PIPELINE                                 │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │   DATA       │    │   DATA           │    │   MODEL      │    │   OUTPUT     │   │
│  │  ACQUISITION │    │   PREPROCESSING  │    │   TRAINING   │    │   &          │   │
│  ├──────────────┤    ├──────────────────┤    ├──────────────┤    │   DEPLOYMENT │   │
│  │ • Temperature│    │ • Missing value  │    │ • GRU        │    ├──────────────┤   │
│  │ • Humidity   │    │   imputation     │    │ • LSTM       │    │ • 1-day ahead│   │
│  │ • Pressure   │    │   (median, <5.5%)│    │ • BiGRU      │    │   forecast   │   │
│  │ • Occupancy  │────▶ • MinMaxScaler   │────▶ • Lookback: │────▶ • HVAC      │   │
│  │ • Window     │    │   (0-1)          │    │   10 days    │    │   control    │   │
│  │   state      │    │ • 10-min         │    │ • Step:      │    │   signals    │   │
│  │ • Weather    │    │   resampling     │    │   30 min     │    │              │   │
│  │              │    │                  │    │              │    │              │   │
│  │ Frequency:   │    │                  │    │ Architecture:│    │              │   │
│  │ 1-min        │    │                  │    │ Seq-to-One   │    │              │   │
│  └──────────────┘    └──────────────────┘    └──────────────┘    └──────────────┘   │
│                                                                                     │
│  Dataset: CN-OBEE (Beijing, China)                    Period: May 2021 - May 2022   │
│  8 features | Indoor environmental monitoring | Regression task                     │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

**Model comparison insight:** GRU consistently outperformed LSTM across temperature and humidity predictions while requiring fewer parameters — the simpler gating mechanism proves sufficient for this temporal granularity. BiGRU excels specifically in pressure forecasting where bidirectional context captures atmospheric patterns.

---

## Quick Start

```bash
git clone https://github.com/KadirGokdeniz/Indoor-AirQ-Predicitons.git
cd Indoor-AirQ-Predicitons
pip install -r requirements.txt

# Run interactive demo
streamlit run src/Smart-Air.py
```

<p align="center">
  <img src="assets/animation.gif" alt="Demo" width="600"/>
</p>

---

## Repository Structure

```
├── notebooks/
│   └── air_quality_predictions.ipynb   # Full training pipeline
├── src/
│   └── Smart-Air.py                    # Streamlit dashboard
├── data/
│   ├── raw/                            # Original CN-OBEE data
│   └── processed/                      # Model predictions
└── docs/
    └── Air-Smart-Report.pdf            # Technical report
```

---

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

---

## Author

**Kadir Gokdeniz && Erkan Bostanci**  
[LinkedIn](https://www.linkedin.com/in/kadir-g%C3%B6kdeniz-16573127a/) • [Google Scholar](https://yzib.com.tr/index.php/yzib/article/view/6) • kadirqokdeniz@hotmail.com

*Research conducted in collaboration with Ankara University, Computer Engineering Department.*
