# Planet Hunter

🪐 A Python-based space probe for your Kubernetes cluster that hunts NASA's Exoplanet Archive for potential Earth-like worlds.

---

## 🚀 Overview
Planet Hunter queries NASA's exoplanet database using their TAP API, applies configurable filters to identify Earth-like candidates, and prints matches to the terminal. It’s designed to be containerized and deployed to a Raspberry Pi cluster running K3s.

## 🧪 Features
- Full dataset scan of confirmed exoplanets
- Modular, configurable filters (radius, orbital period, equilibrium temp, star temp, radius)
- Partial match logic to broaden discovery scope
- Built-in retry + timeout logic for robust requests
- Docker + Kubernetes ready

## 🧰 Requirements
- Python 3.7+
- `requests` library
- Optional: Docker, K3s, kubectl, Helm

---

## 🔧 Usage
### Run locally
```bash
pip install requests
python planet_hunter.py
```

### Set stricter matching
```bash
REQUIRE_ALL_CRITERIA=true python planet_hunter.py
```

---

## 🐳 Container Build
```bash
docker build -t youruser/planet-hunter:latest .
docker push youruser/planet-hunter:latest
```

## ☁️ Kubernetes Deployment
```bash
kubectl apply -f k8s_job.yaml
```

---

## 📂 Project Structure
```
planet-hunter/
├── planet_hunter.py         # Main logic
├── planet_filters.py        # Modular filtering logic
├── Dockerfile               # Container definition
├── k8s_deployment.yaml      # K8s manifest (not currently in use!)
├── k8s_job.yaml      # K8s manifest (use this one!)
├── k8s_cronjob.yaml      # K8s manifest (or this one!)
└── README.md
```

---

## 🧙 Author
Built by space-coding pirates on a mission to map the cosmos — byte by byte 🌌💾
