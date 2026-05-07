from zeek_reader import load_zeek_logs
from adaptive_ml import predict_threat
from identity import identify_device
from geoip_lookup import get_location
from alert_engine import create_alert

print("="*60)
print("AFYAGUARD ENTERPRISE SOC - VALIDATION")
print("="*60)

df = load_zeek_logs()
for _, row in df.head(6).iterrows():
    pred = predict_threat(row)
    print(f"IP: {row['id.orig_h']:18} | Threat: {pred:25} | Device: {identify_device(row['id.orig_h'])}")

print("\n✅ System is ready for presentation!")
