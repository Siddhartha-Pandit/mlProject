import sys
import logging

# Error message generation function
def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class
class CustomeExceptions(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# Set up logging configuration
LOG_FILE = "error_log.log"
logging.basicConfig(
    filename=LOG_FILE,  # Log file name
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR  # Set to ERROR to capture error-level logs and above
)

# Main function to raise exception
if __name__ == "__main__":
    try:
        # Example: This will raise a ZeroDivisionError
        a = 1 / 0
    
    except ZeroDivisionError as e:  # Catching the specific error
        logging.error("An error occurred: %s", str(e))  # Logging the error details
        # Raise custom exception with error message and details
        raise CustomeExceptions("Divide by 0 error", sys)
