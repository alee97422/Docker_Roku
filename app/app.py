import streamlit as st
import requests

roku_devices = {
    "Bedroom": "192.168.1.XXX",
    "Kids room": "192.168.1.XXX"
}

def send_roku_command(roku_ip, command):
    try:
        url = f"http://{roku_ip}:8060/keypress/{command}"
        response = requests.post(url)
        if response.status_code == 200:
            st.success(f"Sent command: {command}")
        else:
            st.error(f"Error sending command. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error sending command: {e}")

def main():
    st.title("Roku Remote Control")

    st.write("## Select Roku Device")
    selected_device = st.selectbox("Select a Roku device:", list(roku_devices.keys()))

    roku_ip = roku_devices[selected_device]

    # Remote control buttons
    st.write("## Roku Remote")
    buttons = {
        "Home": "Home",
        "Back": "Back",
        "Up": "Up",
        "Down": "Down",
        "Left": "Left",
        "Right": "Right",
        "Select": "Select",
        "Volume Up": "VolumeUp",
        "Volume Down": "VolumeDown",
        "Mute": "VolumeMute",
        "Play": "Play",
        "Pause": "Play",
        "Rewind": "Rev",
        "Fast Forward": "Fwd",
        "Power Off": "PowerOff"
    }

    selected_button = st.selectbox("Select a command:", list(buttons.keys()))

    if st.button("Send Command"):
        send_roku_command(roku_ip, buttons[selected_button])

if __name__ == "__main__":
    main()
