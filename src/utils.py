from plyer import notification

def ms_notify(title: str, message: str) -> None:
    notification.notify(
        title=title,
        message=message,
        app_name="Kailand V",
    )

# ms_notify("Alerta de error.", "Hello, World!")