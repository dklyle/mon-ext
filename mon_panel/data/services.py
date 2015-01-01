MOCK_SERVICE_DATA = [
    {
        "id": 1,
        "service": "Compute",
        "status": "green",
        "alarms": "0"
    },
    {
        "id": 2,
        "service": "Volume",
        "status": "green",
        "alarms": "0"
    },
    {
        "id": 3,
        "service": "Image",
        "status": "green",
        "alarms": "0"
    },
    {
        "id": 4,
        "service": "Identity",
        "status": "yellow",
        "alarms": "1"
    },
    {
        "id": 5,
        "service": "Orchestration",
        "status": "green",
        "alarms": "2"
    },
    {
        "id": 6,
        "service": "Object Store",
        "status": "green",
        "alarms": "0"
    },
    {
        "id": 7,
        "service": "Database",
        "status": "green",
        "alarms": "0"
    },
    {
        "id": 8,
        "service": "Metering",
        "status": "red",
        "alarms": "10"
    },
    {
        "id": 9,
        "service": "Data_Processing",
        "status": "green",
        "alarms": "1"
    },
]

def get_mock_data():
    return MOCK_SERVICE_DATA
