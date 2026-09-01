import streamlit as st
import pandas as pd
import requests
from io import BytesIO


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MDC Configuration & BOM Generator",
    page_icon="🏭",
    layout="wide"
)
# ============================================================
# CURRENCY FUNCTIONS
# ============================================================

@st.cache_data(ttl=3600)
def get_live_exchange_rate(from_currency, to_currency):

    if from_currency == to_currency:
        return 1.0

    try:

        url = (
            f"https://api.frankfurter.dev/v2/rate/"
            f"{from_currency}/{to_currency}"
        )

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return float(data["rate"])

    except Exception as e:

        st.warning(
            f"Unable to fetch live exchange rate: {e}"
        )

        return None


def convert_currency(amount, rate):

    if amount is None:
        return None

    return float(amount) * float(rate)


def currency_symbol(currency):

    if currency == "INR":
        return "₹"

    if currency == "USD":
        return "$"

    return ""
# ============================================================
# CURRENCY SELECTION
# ============================================================

st.header("💱 Currency Settings")

col1, col2 = st.columns([2, 2])

with col1:

    selected_currency = st.radio(
        "Display Currency",
        ["INR", "USD"],
        horizontal=True
    )

with col2:

    st.write("")
    st.write("")


# ------------------------------------------------------------
# GET LIVE RATE
# ------------------------------------------------------------

if selected_currency == "INR":

    exchange_rate = 1.0
    base_currency = "INR"
    target_currency = "INR"

else:

    base_currency = "INR"
    target_currency = "USD"

    exchange_rate = get_live_exchange_rate(
        base_currency,
        target_currency
    )


if exchange_rate is None:

    st.error(
        "Unable to fetch live exchange rate. "
        "Please check your internet connection."
    )

    exchange_rate = 1.0

    st.stop()


# ------------------------------------------------------------
# DISPLAY RATE
# ------------------------------------------------------------

if selected_currency == "USD":

    st.success(
        f"Live Exchange Rate: "
        f"₹1 = ${exchange_rate:.4f}"
    )

else:

    st.info(
        "Displaying all values in Indian Rupees (INR)"
    )

st.divider()
# ============================================================
# PRICE MASTER — EDIT ONLY IN CODE
#
# IMPORTANT:
# Keep "XXX" until the actual official price is available.
#
# Example:
# "Config 1": XXX
#
# MUST be changed to:
# "Config 1": 250000
#
# when the actual price is known.
# ============================================================

# ============================================================
# PART NUMBER MASTER — EDIT ONLY IN CODE
# ============================================================

# ============================================================
# SINGLE RACK STANDARD PART NUMBERS
# ============================================================

SINGLE_STANDARD_PART_NUMBERS = {

    "Rack": "721",
    "Cooling System": "XXX",
    "Environment Monitoring": "XXX",
    "Front Access Control": "XXX",
    "Rear Emergency Electronic Lock": "XXX",
    "Automatic Emergency Rear Door Opening": "XXX",
    "Front / Rear Door Open Status Monitoring": "XXX",
    "Power Distribution Module (PDM)": "XXX",
    "Local/Remote Monitoring": "XXX"

}


# ============================================================
# MULTI RACK STANDARD PART NUMBERS
# ============================================================

MULTI_STANDARD_PART_NUMBERS = {

    "Rack (42U 600W 1400D)": "XXX",
    "Rack (42U 800W 1400D)": "XXX",
    "Utility Rack (42U 1400D)": "XXX",
    "In-Row Cooling System": "XXX",
    "Environment Monitoring": "XXX",
    "Front Access Control": "XXX",
    "Rear Emergency Electronic Lock": "XXX",
    "Automatic Emergency Rear Door Opening": "XXX",
    "Front / Rear Door Open Status Monitoring": "XXX",
    "Power Distribution Module (PDM)": "XXX",
    "Local/Remote Monitoring": "XXX"

}


# ============================================================
# SINGLE RACK OPTIONAL PART NUMBERS
# ============================================================

SINGLE_OPTIONAL_PART_NUMBERS = {

    "Fire Suppression - In-Rack": "XXX",
    "Fire Suppression - External": "XXX",
    "PDU - Basic": "XXX",
    "PDU - Metered": "XXX",
    "PDU - Managed": "XXX",
    "CCTV Kit": "XXX",
    "UPS": "XXX",
    "DCIM Integration": "XXX"

}


# ============================================================
# MULTI RACK OPTIONAL PART NUMBERS
# ============================================================

MULTI_OPTIONAL_PART_NUMBERS = {

    "Fire Suppression - External": "XXX",
    "UPS": "XXX",
    "PDU - Basic": "XXX",
    "PDU - Metered": "XXX",
    "PDU - Managed": "XXX",
    "CCTV Kit": "XXX",
    "DCIM": "XXX",
    "VESDA": "XXX",
    "Branch Circuit Monitoring": "XXX"

}
# ============================================================
# SINGLE RACK STANDARD PRICES
# ============================================================

SINGLE_RACK_PRICES = {

    "Config 1": 20000,
    "Config 2": 30000,
    "Config 3": 27000,
    "Config 4": 32000

}


# ============================================================
# MULTI RACK STANDARD PRICES
# ============================================================

MULTI_RACK_PRICES = {

    "Config 1": "XXX",
    "Config 2": "XXX",
    "Config 3": "XXX",
    "Config 4": "XXX",
    "Config 5": "XXX",
    "Config 6": "XXX",
    "Config 7": "XXX",
    "Config 8": "XXX",
    "Config 9": "XXX"

}


# ============================================================
# SINGLE RACK OPTIONAL COMPONENT PRICES
# ============================================================

SINGLE_OPTIONAL_PRICES = {

    "Fire Suppression - In-Rack": 30000,
    "Fire Suppression - External": 35000,
    "PDU - Basic": 21000,
    "PDU - Metered": 1212,
    "PDU - Managed": 2121,
    "CCTV Kit": 34000,
    "UPS": 2000,
    "DCIM Integration":32000

}


# ============================================================
# MULTI RACK OPTIONAL COMPONENT PRICES
# ============================================================

MULTI_OPTIONAL_PRICES = {

    "Fire Suppression - External": "XXX",
    "UPS": "XXX",
    "PDU - Basic": "XXX",
    "PDU - Metered": "XXX",
    "PDU - Managed": "XXX",
    "CCTV Kit": "XXX",
    "DCIM": "XXX",
    "VESDA": "XXX",
    "Branch Circuit Monitoring": "XXX"

}

# ============================================================
# SINGLE RACK CONFIGURATION SPECIFICATIONS
# ============================================================

SINGLE_RACK = {

    "Config 1": {

        "Rack Configuration":
            "42U × 800W × 1200D",

        "Cooling Capacity":
            "3.5 KW (W/o Dehumidifier)",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control":
            "Biometric Lock",

        "Rear Emergency Electronic Lock":
            "Included",

        "Automatic Emergency Rear Door Opening":
            "Yes",

        "Front / Rear Door Open Status Monitoring":
            "Yes",

        "Power Distribution Module (PDM)":
            "Included",

        "Fire Suppression System":
            "Optional (In-Rack / External)",

        "PDU (Basic / Metered / Managed)":
            "Optional",

        "CCTV Kit":
            "Optional",

        "UPS (Based on Capacity & Redundancy)":
            "Optional",

        "Local/Remote Monitoring":
            "Available",

        "DCIM Integration":
            "Optional"
    },


    "Config 2": {

        "Rack Configuration":
            "42U × 800W × 1200D",

        "Cooling Capacity":
            "3.5 KW (Dehumidifier)",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control":
            "Biometric Lock",

        "Rear Emergency Electronic Lock":
            "Included",

        "Automatic Emergency Rear Door Opening":
            "Yes",

        "Front / Rear Door Open Status Monitoring":
            "Yes",

        "Power Distribution Module (PDM)":
            "Included",

        "Fire Suppression System":
            "Optional (In-Rack / External)",

        "PDU (Basic / Metered / Managed)":
            "Optional",

        "CCTV Kit":
            "Optional",

        "UPS (Based on Capacity & Redundancy)":
            "Optional",

        "Local/Remote Monitoring":
            "Available",

        "DCIM Integration":
            "Optional"
    },


    "Config 3": {

        "Rack Configuration":
            "42U × 800W × 1200D",

        "Cooling Capacity":
            "7 KW (W/o Dehumidifier)",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control":
            "Biometric Lock",

        "Rear Emergency Electronic Lock":
            "Included",

        "Automatic Emergency Rear Door Opening":
            "Yes",

        "Front / Rear Door Open Status Monitoring":
            "Yes",

        "Power Distribution Module (PDM)":
            "Included",

        "Fire Suppression System":
            "Optional (In-Rack / External)",

        "PDU (Basic / Metered / Managed)":
            "Optional",

        "CCTV Kit":
            "Optional",

        "UPS (Based on Capacity & Redundancy)":
            "Optional",

        "Local/Remote Monitoring":
            "Available",

        "DCIM Integration":
            "Optional"
    },


    "Config 4": {

        "Rack Configuration":
            "42U × 800W × 1200D",

        "Cooling Capacity":
            "7 KW (Dehumidifier)",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control":
            "Biometric Lock",

        "Rear Emergency Electronic Lock":
            "Included",

        "Automatic Emergency Rear Door Opening":
            "Yes",

        "Front / Rear Door Open Status Monitoring":
            "Yes",

        "Power Distribution Module (PDM)":
            "Included",

        "Fire Suppression System":
            "Optional (In-Rack / External)",

        "PDU (Basic / Metered / Managed)":
            "Optional",

        "CCTV Kit":
            "Optional",

        "UPS (Based on Capacity & Redundancy)":
            "Optional",

        "Local/Remote Monitoring":
            "Available",

        "DCIM Integration":
            "Optional"
    }

}


# ============================================================
# MULTI RACK CONFIGURATION SPECIFICATIONS
# ============================================================

MULTI_RACK = {

    "Config 1": {

        "Rack (42U 600W 1400D)": "1",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "600W",
        "In-Row Cooling Capacity": "10kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "Optional with Basic PDU",
        "VESDA": "Optional"
    },


    "Config 2": {

        "Rack (42U 600W 1400D)": "1",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "600W",
        "In-Row Cooling Capacity": "10kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "Optional with Basic PDU",
        "VESDA": "Optional"
    },


    "Config 3": {

        "Rack (42U 600W 1400D)": "2",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "600W",
        "In-Row Cooling Capacity": "10kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "Optional with Basic PDU",
        "VESDA": "Optional"
    },


    "Config 4": {

        "Rack (42U 600W 1400D)": "1",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "600W",
        "In-Row Cooling Capacity": "20kW - 40kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "NA",
        "VESDA": "Optional"
    },


    "Config 5": {

        "Rack (42U 600W 1400D)": "2",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "800W",
        "In-Row Cooling Capacity": "10kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "NA",
        "VESDA": "Optional"
    },


    "Config 6": {

        "Rack (42U 600W 1400D)": "2",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "800W",
        "In-Row Cooling Capacity": "20kW - 40kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "NA",
        "VESDA": "Optional"
    },


    "Config 7": {

        "Rack (42U 600W 1400D)": "3",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "800W",
        "In-Row Cooling Capacity": "20kW - 40kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "NA",
        "VESDA": "Optional"
    },


    "Config 8": {

        "Rack (42U 600W 1400D)": "4",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "800W",
        "In-Row Cooling Capacity": "20kW - 50kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "NA",
        "VESDA": "Optional"
    },


    "Config 9": {

        "Rack (42U 600W 1400D)": "5",
        "Rack (42U 800W 1400D)": "1",
        "Utility Rack (42U 1400D) - Each": "800W",
        "In-Row Cooling Capacity": "25kW - 60kW",

        "Environment Monitoring":
            "Temperature, Humidity, Smoke, Water Leakage Detection (WLD), "
            "Rodent Detection, Beacon Alarm",

        "Front Access Control": "Biometric Lock",
        "Rear Emergency Electronic Lock": "Included",
        "Automatic Emergency Rear Door Opening": "Yes",
        "Front / Rear Door Open Status Monitoring": "Yes",
        "Power Distribution Module (PDM)": "Included",
        "Local/Remote Monitoring": "Available",
        "Fire Suppression (External)": "Optional",
        "UPS (As per Capacity & Required Redundancy)": "Optional",
        "PDU (Basic / Metered / Managed)": "Optional",
        "CCTV Kit": "Optional",
        "DCIM": "Optional",
        "Branch Circuit Monitoring": "NA",
        "VESDA": "Optional"
    }

}


# ============================================================
# OPTIONAL COMPONENT DEFINITIONS
# ============================================================

SINGLE_OPTIONAL_COMPONENTS = {

    "Fire Suppression - In-Rack":
        "Fire Suppression System - In-Rack",

    "Fire Suppression - External":
        "Fire Suppression System - External",

    "PDU - Basic":
        "PDU - Basic",

    "PDU - Metered":
        "PDU - Metered",

    "PDU - Managed":
        "PDU - Managed",

    "CCTV Kit":
        "CCTV Kit",

    "UPS":
        "UPS",

    "DCIM Integration":
        "DCIM Integration"
}


MULTI_OPTIONAL_COMPONENTS = {

    "Fire Suppression - External":
        "Fire Suppression - External",

    "UPS":
        "UPS",

    "PDU - Basic":
        "PDU - Basic",

    "PDU - Metered":
        "PDU - Metered",

    "PDU - Managed":
        "PDU - Managed",

    "CCTV Kit":
        "CCTV Kit",

    "DCIM":
        "DCIM",

    "VESDA":
        "VESDA",

    "Branch Circuit Monitoring":
        "Branch Circuit Monitoring"
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def is_numeric_price(price):
    """Return True for numeric values and numeric strings, but not XXX."""
    if isinstance(price, bool):
        return False

    if isinstance(price, (int, float)):
        return True

    if isinstance(price, str):
        try:
            float(price.strip().replace(",", ""))
            return True
        except (ValueError, TypeError):
            return False

    return False


def numeric_price(price):
    """Convert a valid numeric price to float; return None for XXX."""
    if not is_numeric_price(price):
        return None

    return float(str(price).strip().replace(",", ""))


# ============================================================
# FORMAT PRICE WITH SELECTED CURRENCY
# ============================================================

def format_price(price):

    if not is_numeric_price(price):
        return "XXX"

    converted_price = convert_currency(
        float(price),
        exchange_rate
    )

    symbol = currency_symbol(
        selected_currency
    )

    return f"{symbol} {converted_price:,.2f}"


def calculate_optional_amount(price, quantity):
    """Optional amount = quantity × unit price. Returns None for XXX."""
    value = numeric_price(price)

    if value is None:
        return None

    return value * int(quantity)


def create_excel_file(dataframes):
    """Create an Excel workbook containing multiple sheets."""
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for sheet_name, dataframe in dataframes.items():
            dataframe.to_excel(
                writer,
                sheet_name=sheet_name[:31],
                index=False
            )

    output.seek(0)
    return output

# ============================================================
# LIVE CURRENCY CONVERSION
# ============================================================

@st.cache_data(ttl=3600)
def get_live_exchange_rate(from_currency, to_currency):

    if from_currency == to_currency:
        return 1.0

    try:

        url = (
            f"https://api.frankfurter.dev/v2/rate/"
            f"{from_currency}/{to_currency}"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        return float(data["rate"])

    except Exception:

        return None


def convert_currency(amount, rate):

    if amount is None:
        return None

    return float(amount) * float(rate)


def currency_symbol(currency):

    if currency == "INR":
        return "₹"

    elif currency == "USD":
        return "$"

    return ""
# ============================================================
# HEADER
# ============================================================


# ============================================================
# HEADER
# ============================================================

st.title("🏭 MDC Configuration & BOM Generator")

st.markdown(
    """
    Select the MDC type and configuration, review the complete
    configuration specifications, select optional components with
    quantities, and generate the final commercial BOM.
    """
)


# ============================================================
# STEP 1 — MDC TYPE
# ============================================================

st.header("1️⃣ Select MDC Type")

mdc_type = st.selectbox("MDC Type", ["Single Rack MDC", "Multi Rack MDC"])


# ============================================================
# STEP 2 — CUSTOMER & PROJECT DETAILS
# ============================================================

st.header("2️⃣ Customer & Project Details")
st.caption("Customer Name and Customer Place are compulsory fields.")

customer_col1, customer_col2 = st.columns(2)

with customer_col1:
    customer_name = st.text_input(
        "Customer Name *",
        placeholder="Enter customer / company name",
        key="customer_name"
    )

with customer_col2:
    customer_place = st.text_input(
        "Customer Place *",
        placeholder="Enter city / location",
        key="customer_place"
    )

problem_col, solution_col = st.columns(2)

with problem_col:
    problem_statement = st.text_area(
        "Problem / Requirement",
        placeholder="Describe the customer's requirement or problem...",
        height=120,
        key="problem_statement"
    )

with solution_col:
    proposed_solution = st.text_area(
        "Proposed Solution",
        placeholder="Describe the proposed MDC solution...",
        height=120,
        key="proposed_solution"
    )

customer_details_complete = bool(
    customer_name.strip() and customer_place.strip()
)

if not customer_details_complete:
    st.warning("Please enter Customer Name and Customer Place before proceeding.")
    st.stop()



# ============================================================
# LOAD CORRECT DATA
# ============================================================

if mdc_type == "Single Rack MDC":

    config_data = SINGLE_RACK
    standard_prices = SINGLE_RACK_PRICES
    optional_prices = SINGLE_OPTIONAL_PRICES
    optional_components = SINGLE_OPTIONAL_COMPONENTS
    standard_part_numbers = SINGLE_STANDARD_PART_NUMBERS
    optional_part_numbers = SINGLE_OPTIONAL_PART_NUMBERS

else:

    config_data = MULTI_RACK
    standard_prices = MULTI_RACK_PRICES
    optional_prices = MULTI_OPTIONAL_PRICES
    optional_components = MULTI_OPTIONAL_COMPONENTS
    standard_part_numbers = MULTI_STANDARD_PART_NUMBERS
    optional_part_numbers = MULTI_OPTIONAL_PART_NUMBERS


# ============================================================
# STEP 3 — CONFIGURATION
# ============================================================

st.header("3️⃣ Select Configuration")

selected_config = st.selectbox(
    "Configuration",
    list(config_data.keys())
)


# ============================================================
# CURRENT CONFIGURATION PRICE
# ============================================================

standard_price = standard_prices[selected_config]


# ============================================================
# STANDARD CONFIGURATION PRICE DISPLAY
# ============================================================

st.subheader("💵 Standard Configuration Cost")

price_col1, price_col2 = st.columns([2, 1])

with price_col1:

    st.metric(
        "Standard Cost",
        format_price(standard_price)
    )

with price_col2:

    st.caption(
        "Configuration costs are maintained only in the Python PRICE MASTER code."
    )


# ============================================================
# STEP 4 — COMPLETE CONFIGURATION SPECIFICATIONS
# ============================================================

st.header("4️⃣ Complete Configuration Specifications")

specifications = config_data[selected_config]

spec_rows = []

for parameter, value in specifications.items():

    spec_rows.append({
        "Parameter": parameter,
        "Specification": value
    })


spec_df = pd.DataFrame(spec_rows)


st.dataframe(
    spec_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# STEP 5 — OPTIONAL COMPONENTS
# ============================================================

st.header("5️⃣ Optional Components")

st.info(
    """
    Select the optional components required for this configuration
    and enter the required quantity for each selected component.

    Amount = Quantity × Unit Price

    Unit prices are maintained only in the Python code.
    """
)


selected_optional_items = []


# ------------------------------------------------------------
# Optional component UI
# ------------------------------------------------------------

for index, component_key in enumerate(optional_components.keys()):

    component_display_name = optional_components[component_key]

    unit_price = optional_prices[component_key]

    col1, col2, col3, col4 = st.columns(
        [0.8, 3.2, 1.3, 1.5]
    )

    with col1:

        selected = st.checkbox(
            "",
            key=f"optional_selected_{mdc_type}_{selected_config}_{component_key}"
        )

    with col2:

        st.write(
            f"**{component_display_name}**"
        )

    with col3:

        st.write(
            f"Unit Cost: **{format_price(unit_price)}**"
        )

    with col4:

        if selected:

            quantity = st.number_input(
                "Quantity",
                min_value=1,
                value=1,
                step=1,
                key=f"optional_qty_{mdc_type}_{selected_config}_{component_key}"
            )

        else:

            quantity = 0


    if selected:

        amount = calculate_optional_amount(
            unit_price,
            quantity
        )

        selected_optional_items.append({

            "component": component_display_name,
            "component_key": component_key,
            "quantity": quantity,
            "unit_price": unit_price,
            "amount": amount

        })


# ============================================================
# OPTIONAL COMPONENT SUMMARY
# ============================================================

st.subheader("📋 Selected Optional Components")


if selected_optional_items:

    optional_summary_rows = []

    for item in selected_optional_items:

        optional_summary_rows.append({

            "Part Number":
                optional_part_numbers.get(
                    item["component_key"],
                    "XXX"
                ),

            "Component":
                item["component"],

            "Quantity":
                item["quantity"],

            "Unit Cost":
                format_price(item["unit_price"]),

            "Amount":
                format_price(item["amount"])
                if item["amount"] is not None
                else "XXX"

        })


    optional_summary_df = pd.DataFrame(
        optional_summary_rows
    )


    st.dataframe(
        optional_summary_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No optional components selected."
    )


# ============================================================
# STEP 6 — COST SUMMARY & COST-TO-PRICE BUILD-UP
# ============================================================

st.header("6️⃣ Cost Summary & Cost-to-Price Build-up")

# ------------------------------------------------------------
# COST FIRST: STANDARD + OPTIONAL
# ------------------------------------------------------------

standard_numeric_price = numeric_price(standard_price)

optional_total = 0.0
has_unknown_optional_price = False

for item in selected_optional_items:
    if is_numeric_price(item["unit_price"]):
        optional_total += item["amount"]
    else:
        has_unknown_optional_price = True

if is_numeric_price(standard_price) and not has_unknown_optional_price:
    total_cost = standard_numeric_price + optional_total
else:
    total_cost = None

# ------------------------------------------------------------
# COST TABLE
# ------------------------------------------------------------

cost_rows = [
    {
        "Cost Item": "Standard Configuration",
        "Quantity": 1,
        "Unit Cost": format_price(standard_price),
        "Total Cost": format_price(standard_price)
    }
]

for item in selected_optional_items:
    cost_rows.append({
        "Cost Item": item["component"],
        "Quantity": item["quantity"],
        "Unit Cost": format_price(item["unit_price"]),
        "Total Cost": (
            format_price(item["amount"])
            if item["amount"] is not None else "XXX"
        )
    })

cost_df = pd.DataFrame(cost_rows)
st.subheader("💵 Cost Summary — Before Pricing Factors")
st.dataframe(cost_df, use_container_width=True, hide_index=True)

if total_cost is not None:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Standard Configuration Cost", format_price(standard_price))
    with c2:
        st.metric("Optional Components Cost", f"₹ {optional_total:,.2f}")
    with c3:
        st.metric("TOTAL COST", f"₹ {total_cost:,.2f}")
else:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Standard Configuration Cost", format_price(standard_price))
    with c2:
        st.metric("Optional Components Cost", "XXX")
    with c3:
        st.metric("TOTAL COST", "XXX")

# ------------------------------------------------------------
# EDITABLE COST-TO-PRICE FACTORS
# ------------------------------------------------------------

st.subheader("📈 Cost → Price Conversion")
st.info(
    "Enter the pricing factor name and percentage in the UI. "
    "Each percentage is applied to the original total cost and the "
    "resulting additions are accumulated to produce the selling price."
)

# Pricing factors are applied sequentially to the running cumulative amount.
# Example: 1000 + 15% = 1150; 1150 + 20% = 1380; etc.
# This keeps Previous Amount → Added Amount → Cumulative Price mathematically consistent.
# All factor names and percentages are editable in the UI.

DEFAULT_PRICING_FACTORS = [
    ("Factory Cost (COGS)", 0.0),
    ("Admin & R&D Overhead", 15.0),
    ("Marketing & Sales", 20.0),
    ("Manufacturer Profit", 15.0),
    ("Distribution & Retail", 45.0),
]

pricing_factor_rows = []

for factor_index, (default_name, default_percentage) in enumerate(DEFAULT_PRICING_FACTORS, start=1):

    factor_col1, factor_col2 = st.columns([3, 1])

    with factor_col1:
        factor_name = st.text_input(
            f"Layer {factor_index} — Name *",
            value=default_name,
            key=f"pricing_factor_name_{factor_index}"
        )

    with factor_col2:
        factor_percentage = st.number_input(
            f"Percentage *",
            min_value=0.0,
            max_value=1000.0,
            value=default_percentage,
            step=0.5,
            format="%.2f",
            key=f"pricing_factor_percentage_{factor_index}"
        )

    pricing_factor_rows.append({
        "Layer": factor_index,
        "Name": factor_name.strip(),
        "Percentage": float(factor_percentage)
    })

pricing_inputs_complete = all(
    row["Name"] and row["Percentage"] >= 0
    for row in pricing_factor_rows
)

if not pricing_inputs_complete:
    st.error("Every pricing layer must have a Name and Percentage.")
    st.stop()

# ------------------------------------------------------------
# CALCULATE COST → PRICE TABLE
# ------------------------------------------------------------

pricing_build_up_rows = []

running_amount = total_cost

for row in pricing_factor_rows:

    layer = row["Layer"]
    name = row["Name"]
    percentage = row["Percentage"]

    if layer == 1:
        previous_amount_display = format_price(total_cost) if total_cost is not None else "XXX"
        added_amount_display = "—"
        cumulative_display = format_price(total_cost) if total_cost is not None else "XXX"

        if total_cost is not None:
            running_amount = total_cost

    else:
        previous_amount = running_amount

        if running_amount is not None:
            added_amount = running_amount * (percentage / 100.0)
            running_amount = running_amount + added_amount
            previous_amount_display = format_price(previous_amount)
            added_amount_display = f"+{percentage:.2f}% = {format_price(added_amount)}"
            cumulative_display = format_price(running_amount)
        else:
            previous_amount_display = "XXX"
            added_amount_display = f"+{percentage:.2f}% = XXX"
            cumulative_display = "XXX"

    pricing_build_up_rows.append({
        "Layer": layer,
        "Name": name,
        "Percentage Added": "Baseline" if layer == 1 else f"{percentage:.2f}%",
        "Previous Amount": previous_amount_display,
        "Added Amount": added_amount_display,
        "Cumulative Price": cumulative_display
    })

pricing_build_up_df = pd.DataFrame(pricing_build_up_rows)

st.dataframe(
    pricing_build_up_df,
    use_container_width=True,
    hide_index=True
)

# Final selling price is the last cumulative amount.
if total_cost is not None and pricing_inputs_complete:
    selling_price = running_amount
    selling_price_display = format_price(selling_price)
else:
    selling_price = None
    selling_price_display = "XXX"

st.subheader("🏷️ Final Selling Price")
st.success(f"### {selling_price_display}")

# ------------------------------------------------------------
# WARNINGS
# ------------------------------------------------------------

if not customer_details_complete:
    st.warning("Customer Name and Customer Place are compulsory.")

if not is_numeric_price(standard_price):
    st.warning("Standard configuration cost is XXX. Enter the actual cost in the Python PRICE MASTER.")

if has_unknown_optional_price:
    st.warning("One or more selected optional component costs are XXX. Enter their actual costs in the Python PRICE MASTER.")


# ============================================================
# STEP 6 — FINAL BOM
# ============================================================

st.header("6️⃣ Final BOM")

bom_rows = []


# ============================================================
# BUILD STANDARD BOM FROM THE SELECTED CONFIGURATION
# ============================================================

if mdc_type == "Single Rack MDC":

    standard_bom = [
        ("Rack", "Rack Configuration", 1),
        ("Cooling System", "Cooling Capacity", 1),
        ("Environment Monitoring", "Environment Monitoring", 1),
        ("Front Access Control", "Front Access Control", 1),
        ("Rear Emergency Electronic Lock", "Rear Emergency Electronic Lock", 1),
        ("Automatic Emergency Rear Door Opening", "Automatic Emergency Rear Door Opening", 1),
        ("Front / Rear Door Open Status Monitoring", "Front / Rear Door Open Status Monitoring", 1),
        ("Power Distribution Module (PDM)", "Power Distribution Module (PDM)", 1),
        ("Local/Remote Monitoring", "Local/Remote Monitoring", 1),
    ]

else:

    standard_bom = [
        ("Rack (42U 600W 1400D)", "Rack (42U 600W 1400D)", None),
        ("Rack (42U 800W 1400D)", "Rack (42U 800W 1400D)", None),
        ("Utility Rack (42U 1400D)", "Utility Rack (42U 1400D) - Each", 1),
        ("In-Row Cooling System", "In-Row Cooling Capacity", 1),
        ("Environment Monitoring", "Environment Monitoring", 1),
        ("Front Access Control", "Front Access Control", 1),
        ("Rear Emergency Electronic Lock", "Rear Emergency Electronic Lock", 1),
        ("Automatic Emergency Rear Door Opening", "Automatic Emergency Rear Door Opening", 1),
        ("Front / Rear Door Open Status Monitoring", "Front / Rear Door Open Status Monitoring", 1),
        ("Power Distribution Module (PDM)", "Power Distribution Module (PDM)", 1),
        ("Local/Remote Monitoring", "Local/Remote Monitoring", 1),
    ]


# ============================================================
# ADD STANDARD COMPONENTS TO BOM
# ============================================================

# The standard_bom list contains tuples:
# (component_name, specification_key, quantity)
# Build the BOM from the selected configuration.

for component_name, specification_key, bom_quantity in standard_bom:

    # Get the actual specification/value from the selected configuration.
    specification = specifications.get(
        specification_key,
        "XXX"
    )

    # For multi-rack configurations, rack quantities are stored in the
    # selected configuration itself. For the other components the quantity
    # is normally 1.
    if bom_quantity is None:

        raw_quantity = specifications.get(
            specification_key,
            1
        )

        # Rack quantities are normally stored as strings such as "1", "2".
        try:
            quantity = int(float(str(raw_quantity).strip()))
        except (ValueError, TypeError):
            quantity = 1

    else:
        quantity = bom_quantity

    # Get the standard component Part Number from the code-only master.
    part_number = standard_part_numbers.get(
        component_name,
        "XXX"
    )

    bom_rows.append({

        "Category":
            "Standard",

        "Part Number":
            part_number,

        "Component":
            component_name,

        "Specification":
            specification,

        "Quantity":
            quantity,

        "Unit Price":
            "",

        "Amount":
            ""

    })


# ============================================================
# ADD SELECTED OPTIONAL COMPONENTS TO BOM
# ============================================================

for optional_item in selected_optional_items:

    component_key = optional_item.get(
        "component_key",
        optional_item.get("component", "")
    )

    component_name = optional_item.get(
        "component",
        "XXX"
    )

    quantity = optional_item.get(
        "quantity",
        1
    )

    unit_price = optional_item.get(
        "unit_price",
        "XXX"
    )

    # Use the already-calculated amount when available.
    # If a numeric price is present, calculate Quantity × Unit Price.
    if is_numeric_price(unit_price):
        amount = calculate_optional_amount(
            unit_price,
            quantity
        )
    else:
        amount = None

    part_number = optional_part_numbers.get(
        component_key,
        "XXX"
    )

    bom_rows.append({

        "Category":
            "Optional",

        "Part Number":
            part_number,

        "Component":
            component_name,

        "Specification":
            "Selected by User",

        "Quantity":
            quantity,

        "Unit Price":
            format_price(unit_price),

        "Amount":
            (
                format_price(amount)
                if amount is not None
                else "XXX"
            )

    })


# ============================================================
# CREATE FINAL BOM DATAFRAME
# ============================================================

bom_df = pd.DataFrame(
    bom_rows,
    columns=[
        "Category",
        "Part Number",
        "Component",
        "Specification",
        "Quantity",
        "Unit Price",
        "Amount"
    ]
)


# ============================================================
# DISPLAY FINAL BOM
# ============================================================

st.dataframe(
    bom_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# STEP 8 — FINAL BOM & COMMERCIAL SUMMARY
# ============================================================

st.header("8️⃣ Final BOM & Commercial Summary")


commercial_rows = [

    {
        "Part Number":
            "XXX",

        "Description":
            f"{mdc_type} - {selected_config}",

        "Quantity":
            1,

        "Unit Price":
            format_price(standard_price),

        "Amount":
            format_price(standard_price)
    }

]


for item in selected_optional_items:

    commercial_rows.append({

        "Part Number":
            optional_part_numbers.get(
                item["component_key"],
                "XXX"
            ),

        "Description":
            item["component"],

        "Quantity":
            item["quantity"],

        "Unit Cost":
            format_price(item["unit_price"]),

        "Amount":
            format_price(item["amount"])
            if item["amount"] is not None
            else "XXX"

    })


commercial_df = pd.DataFrame(
    commercial_rows
)


st.dataframe(
    commercial_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# COST / PRICE SUMMARY
# ============================================================

st.subheader("💰 Cost & Price Summary")

summary_rows_ui = [
    {"Metric": "Customer Name", "Value": customer_name or "—"},
    {"Metric": "Customer Place", "Value": customer_place or "—"},
    {"Metric": "Problem / Requirement", "Value": problem_statement or "—"},
    {"Metric": "Proposed Solution", "Value": proposed_solution or "—"},
    {"Metric": "Standard Configuration Cost", "Value": format_price(standard_price)},
    {"Metric": "Optional Components Cost", "Value": (f"₹ {optional_total:,.2f}" if not has_unknown_optional_price else "XXX")},
    {"Metric": "TOTAL COST", "Value": (format_price(total_cost) if total_cost is not None else "XXX")},
    {"Metric": "FINAL SELLING PRICE", "Value": selling_price_display},
]

st.dataframe(
    pd.DataFrame(summary_rows_ui),
    use_container_width=True,
    hide_index=True
)

# ============================================================
# STEP 9 — EXCEL EXPORT
# ============================================================

st.header("9️⃣ Excel Export")


# ============================================================
# CUSTOMER / PROJECT DETAILS FOR EXCEL
# ============================================================

customer_details_df = pd.DataFrame([
    {"Field": "Customer Name", "Value": customer_name},
    {"Field": "Customer Place", "Value": customer_place},
    {"Field": "MDC Type", "Value": mdc_type},
    {"Field": "Selected Configuration", "Value": selected_config},
    {"Field": "Problem / Requirement", "Value": problem_statement},
    {"Field": "Proposed Solution", "Value": proposed_solution},
])


# ============================================================
# EXCEL FILE 1 — BOM WITHOUT PRICE
# ============================================================

# Only BOM information. No Unit Price or Amount columns.
bom_without_price_df = bom_df[[
    "Category",
    "Part Number",
    "Component",
    "Specification",
    "Quantity"
]].copy()


# ============================================================
# EXCEL FILE 2 — BOM WITH PRICE
# ============================================================

# This contains the complete BOM plus pricing information and a
# separate Price Summary sheet. Standard configuration price is
# added to the selected optional component totals.
bom_with_price_df = bom_df.copy()


# Optional price details
if selected_optional_items:

    export_optional_df = pd.DataFrame([
        {
            "Part Number":
                optional_part_numbers.get(
                    item["component_key"],
                    "XXX"
                ),

            "Component":
                item["component"],

            "Quantity":
                item["quantity"],

            "Unit Cost":
                format_price(item["unit_price"]),

            "Amount":
                (
                    format_price(item["amount"])
                    if item["amount"] is not None
                    else "XXX"
                )
        }
        for item in selected_optional_items
    ])

else:

    export_optional_df = pd.DataFrame(
        columns=[
            "Part Number",
            "Component",
            "Quantity",
            "Unit Cost",
            "Amount"
        ]
    )


# ============================================================
# PRICE SUMMARY + COST-TO-PRICE BUILD-UP
# ============================================================

price_summary_rows = [
    {"Section": "Customer", "Item": "Customer Name", "Value": customer_name},
    {"Section": "Customer", "Item": "Customer Place", "Value": customer_place},
    {"Section": "Project", "Item": "Problem / Requirement", "Value": problem_statement},
    {"Section": "Project", "Item": "Proposed Solution", "Value": proposed_solution},
    {"Section": "Configuration", "Item": "MDC Type", "Value": mdc_type},
    {"Section": "Configuration", "Item": "Selected Configuration", "Value": selected_config},
    {"Section": "Cost", "Item": "Standard Configuration Cost", "Value": format_price(standard_price)},
    {"Section": "Cost", "Item": "Optional Components Cost", "Value": (f"₹ {optional_total:,.2f}" if not has_unknown_optional_price else "XXX")},
    {"Section": "Cost", "Item": "TOTAL COST", "Value": (format_price(total_cost) if total_cost is not None else "XXX")},
]

for row in pricing_build_up_rows:
    price_summary_rows.append({
        "Section": "Cost → Price",
        "Item": f"Layer {row['Layer']} — {row['Name']}",
        "Value": (
            f"{row['Percentage Added']} | Previous: {row['Previous Amount']} | "
            f"Added: {row['Added Amount']} | Cumulative: {row['Cumulative Price']}"
        )
    })

price_summary_rows.append({
    "Section": "Price",
    "Item": "FINAL SELLING PRICE",
    "Value": selling_price_display
})

price_summary_df = pd.DataFrame(price_summary_rows)

# Separate editable-factor table for the Excel workbook.
pricing_factors_export_df = pd.DataFrame(pricing_factor_rows)
pricing_factors_export_df["Percentage Added"] = pricing_factors_export_df["Percentage"].map(
    lambda x: "Baseline" if x == 0 else f"{x:.2f}%"
)
pricing_factors_export_df = pricing_factors_export_df[
    ["Layer", "Name", "Percentage Added"]
]

# ============================================================
# CREATE BOM WITHOUT PRICE EXCEL
# ============================================================

excel_bom_without_price = create_excel_file({
    "Customer Details":
        customer_details_df,

    "BOM":
        bom_without_price_df
})


# ============================================================
# CREATE BOM WITH PRICE EXCEL
# ============================================================

excel_bom_with_price = create_excel_file({

    "Customer Details":
        customer_details_df,

    "BOM With Price":
        bom_with_price_df,

    "Optional Prices":
        export_optional_df,

    "Cost Summary":
        cost_df,

    "Price Build-up":
        pricing_build_up_df,

    "Pricing Factors":
        pricing_factors_export_df,

    "Price Summary":
        price_summary_df

})


# ============================================================
# DOWNLOAD — BOM WITHOUT PRICE
# ============================================================

st.download_button(

    label="📥 Download BOM — Without Price",

    data=excel_bom_without_price,

    file_name=(
        f"{mdc_type.replace(' ', '_')}_"
        f"{selected_config.replace(' ', '_')}_"
        f"BOM_Without_Price.xlsx"
    ),

    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    ),

    key="download_bom_without_price"
)


# ============================================================
# DOWNLOAD — BOM WITH PRICE
# ============================================================

st.download_button(

    label="📥 Download BOM — With Price",

    data=excel_bom_with_price,

    file_name=(
        f"{mdc_type.replace(' ', '_')}_"
        f"{selected_config.replace(' ', '_')}_"
        f"BOM_With_Price.xlsx"
    ),

    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    ),

    key="download_bom_with_price"
)


# FOOTER
# ============================================================

st.divider()

st.caption(
    "MDC Configuration & BOM Generator | "
    "Configuration costs and part numbers are maintained in Python code; pricing factors are editable in the UI."
)
