import streamlit as st
import pandas as pd
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

    "Rack": "XXX",
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

    "Config 1": 2,
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


def format_price(price):
    """Display a price. XXX stays XXX."""
    value = numeric_price(price)

    if value is None:
        return "XXX"

    return f"₹ {value:,.2f}"


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

mdc_type = st.radio(
    "MDC Type",
    [
        "Single Rack MDC",
        "Multi Rack MDC"
    ],
    horizontal=True
)


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
# STEP 2 — CONFIGURATION
# ============================================================

st.header("2️⃣ Select Configuration")

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

st.subheader("💰 Standard Configuration Price")

price_col1, price_col2 = st.columns([2, 1])

with price_col1:

    st.metric(
        "Standard Price",
        format_price(standard_price)
    )

with price_col2:

    st.caption(
        "Price is maintained only in the Python code."
    )


# ============================================================
# STEP 3 — COMPLETE CONFIGURATION SPECIFICATIONS
# ============================================================

st.header("3️⃣ Complete Configuration Specifications")

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
# STEP 4 — OPTIONAL COMPONENTS
# ============================================================

st.header("4️⃣ Optional Components")

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
            f"Unit Price: **{format_price(unit_price)}**"
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

            "Unit Price":
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
# PRICE CALCULATION
# ============================================================

standard_numeric_price = numeric_price(
    standard_price
)

if standard_numeric_price is None:
    standard_numeric_price = 0.0


optional_total = 0.0

has_unknown_optional_price = False


for item in selected_optional_items:

    if is_numeric_price(item["unit_price"]):

        optional_total += item["amount"]

    else:

        has_unknown_optional_price = True


# ============================================================
# FINAL PRICE
# ============================================================

if (
    is_numeric_price(standard_price)
    and not has_unknown_optional_price
):

    final_total = (
        standard_numeric_price
        + optional_total
    )

    final_total_display = format_price(
        final_total
    )

else:

    final_total = None

    final_total_display = "XXX"


# ============================================================
# PRICE BREAKDOWN
# ============================================================

st.header("5️⃣ Price Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)


with summary_col1:

    st.metric(
        "Standard Configuration",
        format_price(standard_price)
    )


with summary_col2:

    if has_unknown_optional_price:

        st.metric(
            "Optional Components",
            "XXX"
        )

    else:

        st.metric(
            "Optional Components",
            f"₹ {optional_total:,.2f}"
        )


with summary_col3:

    st.metric(
        "FINAL PRICE",
        final_total_display
    )


# ============================================================
# PRICE FORMULA
# ============================================================

st.subheader("🧮 Price Calculation")


st.markdown(
    """
    **Final Price = Standard Configuration Price
    + Sum of (Optional Component Quantity × Optional Component Unit Price)**
    """
)


# ============================================================
# SHOW CALCULATION DETAILS
# ============================================================

calculation_rows = []


calculation_rows.append({

    "Item":
        f"{selected_config} - Standard Configuration",

    "Quantity":
        1,

    "Unit Price":
        format_price(standard_price),

    "Amount":
        format_price(standard_price)

})


for item in selected_optional_items:

    calculation_rows.append({

        "Item":
            item["component"],

        "Quantity":
            item["quantity"],

        "Unit Price":
            format_price(item["unit_price"]),

        "Amount":
            format_price(item["amount"])
            if item["amount"] is not None
            else "XXX"

    })


if calculation_rows:

    calculation_df = pd.DataFrame(
        calculation_rows
    )

    st.dataframe(
        calculation_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PRICE WARNING
# ============================================================

if not is_numeric_price(standard_price):

    st.warning(
        """
        ⚠️ The standard configuration price is still XXX.

        Enter the actual standard price in the PRICE MASTER section
        at the top of this Python file.
        """
    )


if has_unknown_optional_price:

    st.warning(
        """
        ⚠️ One or more selected optional components still have
        XXX as their price.

        Enter their actual prices in the PRICE MASTER section
        at the top of this Python file.
        """
    )


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
# ADD STANDARD COMPONENTS
# ============================================================

for component_name, specification_key, fixed_quantity in standard_bom:

    specification = specifications.get(
        specification_key,
        "XXX"
    )

    if fixed_quantity is None:
        try:
            quantity = int(float(specification))
        except (ValueError, TypeError):
            quantity = 1
    else:
        quantity = fixed_quantity

    bom_rows.append({

        "Category":
            "Standard",

        "Part Number":
            standard_part_numbers.get(
                component_name,
                "XXX"
            ),

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
# ADD SELECTED OPTIONAL COMPONENTS
# ============================================================

for item in selected_optional_items:

    bom_rows.append({

        "Category":
            "Optional",

        "Part Number":
            optional_part_numbers.get(
                item["component_key"],
                "XXX"
            ),

        "Component":
            item["component"],

        "Specification":
            "Selected by User",

        "Quantity":
            item["quantity"],

        "Unit Price":
            format_price(item["unit_price"]),

        "Amount":
            format_price(item["amount"])
            if item["amount"] is not None
            else "XXX"

    })


# ============================================================
# CREATE AND DISPLAY BOM
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

st.dataframe(
    bom_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# STEP 7 — COMMERCIAL SUMMARY
# ============================================================


# ============================================================
# STEP 7 — COMMERCIAL SUMMARY
# ============================================================

st.header("7️⃣ Commercial Pricing Summary")


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

        "Unit Price":
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
# TOTALS
# ============================================================

st.subheader("💰 Total Commercial Value")


total_col1, total_col2 = st.columns(2)


with total_col1:

    st.write(
        "**Standard Configuration:**"
    )

    st.write(
        format_price(standard_price)
    )

    st.write(
        "**Optional Components:**"
    )

    if has_unknown_optional_price:

        st.write("XXX")

    else:

        st.write(
            f"₹ {optional_total:,.2f}"
        )


with total_col2:

    st.success(
        f"### FINAL PRICE: {final_total_display}"
    )





# ============================================================
# STEP 8 — EXCEL EXPORT
# ============================================================

st.header("8️⃣ Export")


# Specifications DataFrame
export_spec_rows = []

for parameter, value in specifications.items():

    export_spec_rows.append({

        "Parameter":
            parameter,

        selected_config:
            value

    })


export_spec_df = pd.DataFrame(
    export_spec_rows
)


# Optional components DataFrame
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

            "Unit Price":
                format_price(item["unit_price"]),

            "Amount":
                format_price(item["amount"])
                if item["amount"] is not None
                else "XXX"
        }

        for item in selected_optional_items
    ])

else:

    export_optional_df = pd.DataFrame(
        columns=[
            "Part Number",
            "Component",
            "Quantity",
            "Unit Price",
            "Amount"
        ]
    )


# Price summary DataFrame


# Price summary DataFrame
price_summary_df = pd.DataFrame([

    {
        "Description":
            "Standard Configuration",

        "Price":
            format_price(standard_price)
    },

    {
        "Description":
            "Optional Components",

        "Price":
            (
                f"₹ {optional_total:,.2f}"
                if not has_unknown_optional_price
                else "XXX"
            )
    },

    {
        "Description":
            "FINAL PRICE",

        "Price":
            final_total_display
    }

])


# Create Excel
excel_file = create_excel_file({

    "Configuration":
        export_spec_df,

    "Optional Components":
        export_optional_df,

    "BOM":
        bom_df,

    "Price Summary":
        price_summary_df

})


st.download_button(

    label="📥 Download Complete BOM & Pricing Excel",

    data=excel_file,

    file_name=(
        f"{mdc_type.replace(' ', '_')}_"
        f"{selected_config.replace(' ', '_')}_BOM.xlsx"
    ),

    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    )

)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "MDC Configuration & BOM Generator | "
    "Prices and part numbers are maintained in Python code only."
)
