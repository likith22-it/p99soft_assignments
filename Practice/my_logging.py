import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def process_purchase(email,item_id):
    logging.debug(f"fetching item details for item_id: {item_id}")

    logging.info(f"user email {email} is purchasing item {item_id}")

    logging.warning("primary payment gateway is slow to respond")

    try:
        tax_calculation = 1 / 0
    except ZeroDivisionError as e:
        logging.error(f"error calculating tax: {e}")
        tax_calculation = 0

    logging.critical("purchase process completed with critical issues")

if __name__ == "__main__":
    process_purchase("user@example.com", "item123")