import bluetooth

# Scan for nearby Bluetooth devices
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

# Display nearby devices
print("Nearby Bluetooth Devices:")
for addr, name in nearby_devices:
    print(f"{name}: {addr}")

# Check if your speaker is in the list of nearby devices
speaker_name = "Arin's WH-1000XM4"  # Replace with the name of your speaker
speaker_addr = None
for addr, name in nearby_devices:
    if name == speaker_name:
        speaker_addr = addr
        break

# Connect to the speaker if found
if speaker_addr:
    print(f"Connecting to {speaker_name}...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1  # Default RFCOMM port
    try:
        sock.connect((speaker_addr, port))
        print("Connected to speaker successfully.")
        
        # Now you can send commands to control the speaker using sock.send()
        # Example: sock.send(b"play")
        # Make sure to refer to the speaker's documentation for the correct commands
        
    except bluetooth.BluetoothError as e:
        print(f"Failed to connect to {speaker_name}: {e}")
        sock.close()
else:
    print(f"Speaker '{speaker_name}' not found.")