import weather_module
import email_module
   
def main():
    emails = email_module.get_emails()
    forecast = weather_module.get_weather_forecast()
    print("You are about to send the following message to the following recipients:")
    print(forecast)
    print(emails)

    email_module.send_emails(emails, forecast)

    
main()

