# Deep Learning for Indoor Air Quality Forecasting

[![Paper](https://img.shields.io/badge/Paper-JAIHS%202024-blue)](https://dergipark.org.tr/tr/pub/jaihs)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)](https://tensorflow.org/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://indoor-airq-predictions-42.streamlit.app/)

**Predicting temperature, humidity, and air pressure in smart buildings using GRU/LSTM networks - enabling proactive HVAC automation instead of reactive control.**

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

| Parameter (Renormalized) | Best Model | MAE | RMSE |
|-----------|------------|-----|------|
| Temperature | GRU | **0.57°C** | 2.98°C |
| Humidity | GRU | **5.41%** | 9.21% |
| Pressure | BiGRU | **578 Pa** | 1058 Pa |

**Key insight:** Room occupancy patterns significantly impact prediction accuracy. High-traffic rooms (kitchen, living room) yield better predictions due to more consistent temporal patterns.

---

## Approach

```mermaid
flowchart LR
    A["🗂️ CN-OBEE Dataset"] --> B["⚙️ Preprocess Normalize + Resample"]
    B --> C["🧠 GRU/LSTM/BiGRU Seq-to-One"]
    C --> D["📈 10 mins Ahead Forecast"]
    D --> E["🏠 HVAC Automation"]

    style A fill:#4f46e5,stroke:#3730a3,color:#fff,stroke-width:2px
    style B fill:#7c3aed,stroke:#5b21b6,color:#fff,stroke-width:2px
    style C fill:#0ea5e9,stroke:#0369a1,color:#fff,stroke-width:2px
    style D fill:#10b981,stroke:#047857,color:#fff,stroke-width:2px
    style E fill:#f59e0b,stroke:#d97706,color:#fff,stroke-width:2px
```

**Model comparison insight:** GRU consistently outperformed LSTM across temperature and humidity predictions while requiring fewer parameters — the simpler gating mechanism proves sufficient for this temporal granularity. BiGRU excels specifically in pressure forecasting where bidirectional context captures atmospheric patterns.

---

## Quick Start

```bash
git clone https://github.com/KadirGokdeniz/Indoor-AirQ-Predicitons.git
cd Indoor-AirQ-Predicitons

# Run interactive demo
streamlit run src/Smart-Air.py
```

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
