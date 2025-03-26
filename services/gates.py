import requests


def open_gate(number, gate):
    try:
        if gate == "entry":
            response = requests.post(
                f"http://localhost:8000/api/v1/sessions/entry", json={"plate_number": number})
        elif gate == "exit":
            response = requests.put(
                f"http://localhost:8000/api/v1/sessions/exit", json={"plate_number": number})
        return response.json()
    except Exception as e:
        raise Exception(f"[GATE] Failed to open gate: {e}")
