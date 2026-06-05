import requests
import random
import time

API_URL = "https://educart-give-away-referral.educart.workers.dev/referral/track"
REF_CODE = "7zxx4502"

def generate_random_mobile():
    """Generate a random 10-digit Indian mobile number."""
    first_digit = random.choice(['6','7','8','9'])
    rest = ''.join(str(random.randint(0,9)) for _ in range(9))
    return first_digit + rest

def send_referral(mobile_number):
    """Send POST request and print result."""
    payload = {"ref_code": REF_CODE, "new_mobile": mobile_number}
    headers = {"Content-Type": "application/json"}
    try:
        resp = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            print(f"[✓] {mobile_number} -> {resp.json()}")
        else:
            print(f"[✗] {mobile_number} -> HTTP {resp.status_code}")
    except Exception as e:
        print(f"[!] Error for {mobile_number}: {e}")

if __name__ == "__main__":
    print("Starting unlimited referral submissions (Ctrl+C to stop)\n")
    try:
        while True:
            mobile = generate_random_mobile()
            send_referral(mobile)
            time.sleep(1)  # 1 second delay to be polite
    except KeyboardInterrupt:
        print("\nStopped by user.")